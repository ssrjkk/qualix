window.BENCHMARK_DATA = {
  "lastUpdate": 1781645990231,
  "repoUrl": "https://github.com/ssrjkk/qualix",
  "entries": {
    "QA Sentinel Benchmarks": [
      {
        "commit": {
          "author": {
            "email": "ssrjk@github.com",
            "name": "ssrjk"
          },
          "committer": {
            "email": "ssrjk@github.com",
            "name": "ssrjk"
          },
          "distinct": true,
          "id": "5702767555ed3f19f02a3e04251e90eca7b5f6b7",
          "message": "fix: add DATABASE_URL to coverage badge job, add permissions to benchmark job\n\n- Coverage badge job was trying to use Docker testcontainers on\n  GitHub runner instead of SQLite, causing test failures\n- Benchmark job was missing permissions: contents: write needed\n  to push to gh-pages",
          "timestamp": "2026-06-17T00:35:44+03:00",
          "tree_id": "dedebbc6a2ef98b2569a18168d84cf40297546a4",
          "url": "https://github.com/ssrjkk/qualix/commit/5702767555ed3f19f02a3e04251e90eca7b5f6b7"
        },
        "date": 1781645989859,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.314944019509349,
            "unit": "iter/sec",
            "range": "stddev: 0.00019910086436673134",
            "extra": "mean: 301.6642194000042 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.2862923953432825,
            "unit": "iter/sec",
            "range": "stddev: 0.0038554322463883765",
            "extra": "mean: 304.29428660000326 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.298390772995601,
            "unit": "iter/sec",
            "range": "stddev: 0.003014624589598706",
            "extra": "mean: 303.17814620000263 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 289171.8180645096,
            "unit": "iter/sec",
            "range": "stddev: 6.942665471930467e-7",
            "extra": "mean: 3.4581516507840195 usec\nrounds: 20112"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 497088.5129852743,
            "unit": "iter/sec",
            "range": "stddev: 4.1569821534117045e-7",
            "extra": "mean: 2.0117141593043084 usec\nrounds: 99454"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15384.922206644294,
            "unit": "iter/sec",
            "range": "stddev: 0.000013976878581353997",
            "extra": "mean: 64.99870370278047 usec\nrounds: 27"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 480158.4258774364,
            "unit": "iter/sec",
            "range": "stddev: 4.653654932743523e-7",
            "extra": "mean: 2.082645947892325 usec\nrounds: 126391"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9113211.245628282,
            "unit": "iter/sec",
            "range": "stddev: 1.1433552325531214e-8",
            "extra": "mean: 109.73080432868403 nsec\nrounds: 87974"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15018.089194709943,
            "unit": "iter/sec",
            "range": "stddev: 0.000005419704262314055",
            "extra": "mean: 66.58636708272086 usec\nrounds: 4168"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 310151.80045054364,
            "unit": "iter/sec",
            "range": "stddev: 5.853401785775681e-7",
            "extra": "mean: 3.2242276154687626 usec\nrounds: 6366"
          }
        ]
      }
    ]
  }
}