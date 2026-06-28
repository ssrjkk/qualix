import os
import sys


def main() -> None:
    print("[entrypoint] Starting QA Sentinel", flush=True)
    print(f"[entrypoint] CWD: {os.getcwd()}", flush=True)
    print(f"[entrypoint] Python: {sys.version}", flush=True)

    try:
        from app.main import app  # noqa: F401

        print("[entrypoint] App imported successfully", flush=True)
    except Exception:
        print("[entrypoint] FATAL: Failed to import app", flush=True)
        import traceback

        traceback.print_exc(file=sys.stdout)
        sys.stdout.flush()
        sys.exit(1)

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        log_level="debug",
    )


if __name__ == "__main__":
    main()
