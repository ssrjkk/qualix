window.BENCHMARK_DATA = {
  "lastUpdate": 1781646792740,
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
      },
      {
        "commit": {
          "author": {
            "email": "136786536+ssrjkk@users.noreply.github.com",
            "name": "ssrjkk",
            "username": "ssrjkk"
          },
          "committer": {
            "email": "ssrjk@github.com",
            "name": "ssrjk"
          },
          "distinct": true,
          "id": "794a2e14f376537a59c455807e1b34c02e23426e",
          "message": "fix: add DATABASE_URL to coverage badge job, add permissions to benchmark job\n\n- Coverage badge job was trying to use Docker testcontainers on\n  GitHub runner instead of SQLite, causing test failures\n- Benchmark job was missing permissions: contents: write needed\n  to push to gh-pages",
          "timestamp": "2026-06-17T00:48:37+03:00",
          "tree_id": "dedebbc6a2ef98b2569a18168d84cf40297546a4",
          "url": "https://github.com/ssrjkk/qualix/commit/794a2e14f376537a59c455807e1b34c02e23426e"
        },
        "date": 1781646792226,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.3085627876602386,
            "unit": "iter/sec",
            "range": "stddev: 0.0018090467154752913",
            "extra": "mean: 302.2460398000135 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3150848476540777,
            "unit": "iter/sec",
            "range": "stddev: 0.0005700874375966106",
            "extra": "mean: 301.6514043999962 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.316860970328239,
            "unit": "iter/sec",
            "range": "stddev: 0.0003142477428247281",
            "extra": "mean: 301.4898751999965 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 288305.52418588864,
            "unit": "iter/sec",
            "range": "stddev: 6.80546667145842e-7",
            "extra": "mean: 3.468542626173327 usec\nrounds: 18064"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 489099.1894521475,
            "unit": "iter/sec",
            "range": "stddev: 4.294372679845976e-7",
            "extra": "mean: 2.044575050553908 usec\nrounds: 94030"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15497.465544600858,
            "unit": "iter/sec",
            "range": "stddev: 0.000013002481367469077",
            "extra": "mean: 64.526679999517 usec\nrounds: 25"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 480848.6855334404,
            "unit": "iter/sec",
            "range": "stddev: 4.3877744116194084e-7",
            "extra": "mean: 2.0796563037094034 usec\nrounds: 143042"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9031503.165082317,
            "unit": "iter/sec",
            "range": "stddev: 1.1252508419133601e-8",
            "extra": "mean: 110.72353978307947 nsec\nrounds: 85412"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15471.036395002273,
            "unit": "iter/sec",
            "range": "stddev: 0.000003364416310538631",
            "extra": "mean: 64.63691083572381 usec\nrounds: 4116"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 310173.24426202686,
            "unit": "iter/sec",
            "range": "stddev: 6.268826535273088e-7",
            "extra": "mean: 3.22400470865638 usec\nrounds: 6371"
          }
        ]
      }
    ]
  }
}