"""Lightweight mutation testing for qualix core modules.

Mutates the source file in-place (text-based), runs tests, restores original.

Usage:
    python scripts/mutation_test.py
"""

from __future__ import annotations

import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

BASE_TEST_ARGS = "-x -q --no-header -o addopts= -o asyncio_mode=auto --timeout=120"

TARGETS: list[tuple[Path, list[str]]] = [
    (
        REPO / "app" / "services" / "validators.py",
        [
            "-k",
            "validator",
            "tests/unit/test_validators.py",
            "tests/unit/test_validators_extended.py",
            "tests/unit/test_property_based.py",
        ],
    ),
    (
        REPO / "app" / "security.py",
        [
            "tests/unit/test_security.py",
            "tests/unit/test_property_based.py::TestPasswordHashing",
        ],
    ),
]


def replace_in_file(text: str, old: str, new: str) -> str:
    """Replace first occurrence only (most targeted mutation)."""
    return text.replace(old, new, 1)


def run_tests(test_args: list[str]) -> tuple[bool, str, float]:
    # Quote -k values to prevent shell word splitting
    quoted: list[str] = []
    for a in test_args:
        if a.startswith("-") and len(quoted) > 0 and quoted[-1] == "-k":
            a = f'"{a}"'
        quoted.append(a)
    cmd = f"{sys.executable} -m pytest {BASE_TEST_ARGS} {' '.join(quoted)}"
    start = time.perf_counter()
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO), shell=True)
    elapsed = time.perf_counter() - start
    return result.returncode == 0, result.stdout + result.stderr, elapsed


def test_module(module_path: Path, test_args: list[str]) -> list[dict]:
    original = module_path.read_text(encoding="utf-8")

    # [(name, search, replace), ...]
    mutations: list[tuple[str, str, str]] = []
    text = original

    # == -> !=
    for m in re.finditer(r"(?<=[^=!<>])==(?=[^=])", text):
        mutations.append((f"eq_to_neq@L{m.string[: m.start()].count(chr(10)) + 1}", "==", "!="))
        break  # just the first match

    # != -> ==
    for m in re.finditer(r"!==", text):
        mutations.append((f"neq_to_eq@L{m.string[: m.start()].count(chr(10)) + 1}", "!=", "=="))
        break

    # and -> or
    for m in re.finditer(r"\band\b", text):
        mutations.append((f"and_to_or@{text[: m.start()].count(chr(10)) + 1}", " and ", " or "))
        break

    # or -> and
    for m in re.finditer(r"\bor\b", text):
        mutations.append((f"or_to_and@{text[: m.start()].count(chr(10)) + 1}", " or ", " and "))
        break

    # remove if body (replace block with pass)
    for m in re.finditer(r"^\s+if\s+", text, re.MULTILINE):
        line_start = m.start()
        indent = m.group()
        cond = m.group() + text[m.end() : text.index(":", line_start)] + ":"
        mutations.append(
            (
                f"remove_if@{text[:line_start].count(chr(10)) + 1}",
                cond,
                f"{indent}pass  # removed by mutator\n",
            )
        )
        break

    # flip boolean return True -> False
    for m in re.finditer(r"return\s+True", text):
        line = text[: m.start()].count(chr(10)) + 1
        mutations.append((f"ret_true_false@{line}", "return True", "return False"))
        break

    # flip boolean return False -> True
    for m in re.finditer(r"return\s+False", text):
        line = text[: m.start()].count(chr(10)) + 1
        mutations.append((f"ret_false_true@{line}", "return False", "return True"))
        break

    # flip > to <
    for m in re.finditer(r"(?<![=<])\>(?=[^=])", text):
        line = text[: m.start()].count(chr(10)) + 1
        mutations.append((f"gt_to_lt@{line}", ">", "<"))
        break

    # flip < to >
    for m in re.finditer(r"(?<![=<])\<(?=[^=])", text):
        line = text[: m.start()].count(chr(10)) + 1
        mutations.append((f"lt_to_gt@{line}", "<", ">"))
        break

    # remove not
    for m in re.finditer(r"not\s+", text):
        line = text[: m.start()].count(chr(10)) + 1
        mutations.append((f"remove_not@{line}", m.group(), ""))
        break

    # Pre-check
    print("\n  Pre-check: original tests...", end=" ", flush=True)
    ok, out, _ = run_tests(test_args)
    if not ok:
        print(f"FAILED: {out[:300]}")
        return []
    print("OK")

    results = []
    for name, old, new in mutations:
        mutated = replace_in_file(original, old, new)
        if mutated == original:
            continue
        module_path.write_text(mutated, encoding="utf-8")
        try:
            passed, out, elapsed = run_tests(test_args)
        finally:
            module_path.write_text(original, encoding="utf-8")
        status = "SURVIVED" if passed else "KILLED"
        results.append({"mutant": name, "status": status, "time": f"{elapsed:.1f}s"})
        mark = "S" if passed else "K"
        print(f"  [{mark}] {name}: {status} ({elapsed:.1f}s)")

    return results


def main() -> None:
    all_survived = 0
    all_killed = 0
    for module_path, test_args in TARGETS:
        print(f"\n{'=' * 60}")
        print(f"Module: {module_path.relative_to(REPO)}")
        print(f"{'=' * 60}")
        results = test_module(module_path, test_args)
        survived = [r for r in results if r["status"] == "SURVIVED"]
        killed = [r for r in results if r["status"] == "KILLED"]
        all_survived += len(survived)
        all_killed += len(killed)
        print(f"\n  => {len(results)} mutants: {len(survived)} survived, {len(killed)} killed")

    total = all_survived + all_killed
    score = 100.0 * all_killed / total if total else 100.0
    print(f"\n{'=' * 60}")
    print(f"TOTAL: {all_survived} survived, {all_killed} killed")
    print(f"Mutation score: {score:.1f}%")
    if all_survived > 0:
        print("! Review surviving mutants above -- add missing tests.")
        sys.exit(1)


if __name__ == "__main__":
    main()
