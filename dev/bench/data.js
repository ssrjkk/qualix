window.BENCHMARK_DATA = {
  "lastUpdate": 1782029366898,
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
      },
      {
        "commit": {
          "author": {
            "name": "github-actions[bot]",
            "username": "github-actions[bot]",
            "email": "github-actions[bot]@users.noreply.github.com"
          },
          "committer": {
            "name": "github-actions[bot]",
            "username": "github-actions[bot]",
            "email": "github-actions[bot]@users.noreply.github.com"
          },
          "id": "bba792a43ff235a2571963fd77711bbf7c39452d",
          "message": "chore: update coverage badge [skip ci]",
          "timestamp": "2026-06-16T21:53:26Z",
          "url": "https://github.com/ssrjkk/qualix/commit/bba792a43ff235a2571963fd77711bbf7c39452d"
        },
        "date": 1781685437567,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7363458770768787,
            "unit": "iter/sec",
            "range": "stddev: 0.0004002919511895302",
            "extra": "mean: 267.6411748000021 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.738131216575801,
            "unit": "iter/sec",
            "range": "stddev: 0.0002280889408618754",
            "extra": "mean: 267.5133487999972 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7397875396481894,
            "unit": "iter/sec",
            "range": "stddev: 0.00011288429779616327",
            "extra": "mean: 267.39486919999536 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 272284.0906980163,
            "unit": "iter/sec",
            "range": "stddev: 9.762967130276716e-7",
            "extra": "mean: 3.672634700898026 usec\nrounds: 21596"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 477261.86416807736,
            "unit": "iter/sec",
            "range": "stddev: 5.658722535415364e-7",
            "extra": "mean: 2.0952857855993074 usec\nrounds: 84154"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12610.454975201596,
            "unit": "iter/sec",
            "range": "stddev: 0.00001207759185588136",
            "extra": "mean: 79.29927999953179 usec\nrounds: 25"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 470163.4756348103,
            "unit": "iter/sec",
            "range": "stddev: 5.582957724053611e-7",
            "extra": "mean: 2.1269197881647646 usec\nrounds: 128784"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 10380564.323665397,
            "unit": "iter/sec",
            "range": "stddev: 9.94801981901803e-9",
            "extra": "mean: 96.33387635007671 nsec\nrounds: 99911"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11595.330369926776,
            "unit": "iter/sec",
            "range": "stddev: 0.000007023147104071772",
            "extra": "mean: 86.24161348550822 usec\nrounds: 4820"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304598.0140568594,
            "unit": "iter/sec",
            "range": "stddev: 6.674286711347168e-7",
            "extra": "mean: 3.2830154953450537 usec\nrounds: 7228"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "github-actions[bot]",
            "username": "github-actions[bot]",
            "email": "github-actions[bot]@users.noreply.github.com"
          },
          "committer": {
            "name": "github-actions[bot]",
            "username": "github-actions[bot]",
            "email": "github-actions[bot]@users.noreply.github.com"
          },
          "id": "bba792a43ff235a2571963fd77711bbf7c39452d",
          "message": "chore: update coverage badge [skip ci]",
          "timestamp": "2026-06-16T21:53:26Z",
          "url": "https://github.com/ssrjkk/qualix/commit/bba792a43ff235a2571963fd77711bbf7c39452d"
        },
        "date": 1781770664381,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.3171258872082965,
            "unit": "iter/sec",
            "range": "stddev: 0.00007968011344963403",
            "extra": "mean: 301.46579719999806 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.317207901412165,
            "unit": "iter/sec",
            "range": "stddev: 0.0001311944686889823",
            "extra": "mean: 301.4583438000045 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.316366156280927,
            "unit": "iter/sec",
            "range": "stddev: 0.00024487496339004223",
            "extra": "mean: 301.5348586000016 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 285696.133993972,
            "unit": "iter/sec",
            "range": "stddev: 6.754655665141716e-7",
            "extra": "mean: 3.5002223727014083 usec\nrounds: 19202"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 486351.32848436065,
            "unit": "iter/sec",
            "range": "stddev: 4.2183274696280294e-7",
            "extra": "mean: 2.056126798535426 usec\nrounds: 100151"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15377.574821178077,
            "unit": "iter/sec",
            "range": "stddev: 0.000015223667695963975",
            "extra": "mean: 65.02975999978844 usec\nrounds: 25"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 483848.4407120568,
            "unit": "iter/sec",
            "range": "stddev: 4.774942357705563e-7",
            "extra": "mean: 2.0667628865938834 usec\nrounds: 126391"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8862030.55218681,
            "unit": "iter/sec",
            "range": "stddev: 1.0885449973068785e-8",
            "extra": "mean: 112.84095604401166 nsec\nrounds: 87360"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 14229.455270168111,
            "unit": "iter/sec",
            "range": "stddev: 0.000013679824051167087",
            "extra": "mean: 70.27675908975155 usec\nrounds: 4263"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304729.85260585434,
            "unit": "iter/sec",
            "range": "stddev: 5.308537339796821e-7",
            "extra": "mean: 3.281595129091033 usec\nrounds: 5461"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ssrjkk@users.noreply.github.com",
            "name": "ssrjkk",
            "username": "ssrjkk"
          },
          "committer": {
            "email": "ssrjkk@users.noreply.github.com",
            "name": "ssrjkk",
            "username": "ssrjkk"
          },
          "distinct": true,
          "id": "e0f1a7e1003c3d5a53eaa339227164d328b7c497",
          "message": "fix: rate limit and auth in load tests\n\n- Add ENVIRONMENT=test to docker-compose.yml so rate limit is 10000\n  req/min instead of 100 — prevents 429 under 100 concurrent users\n- Add on_start + auth headers to HeavyUser so DELETE calls are\n  authenticated (was failing with 401, counting toward exit code 1)",
          "timestamp": "2026-06-18T16:43:31+03:00",
          "tree_id": "8b8005899d9a53dc740253c5516fc2618a18e906",
          "url": "https://github.com/ssrjkk/qualix/commit/e0f1a7e1003c3d5a53eaa339227164d328b7c497"
        },
        "date": 1781790470897,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.736093271711983,
            "unit": "iter/sec",
            "range": "stddev: 0.00035075022693135195",
            "extra": "mean: 267.6592706000008 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.737503850226957,
            "unit": "iter/sec",
            "range": "stddev: 0.00011448318421906816",
            "extra": "mean: 267.5582528000007 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7378583679279918,
            "unit": "iter/sec",
            "range": "stddev: 0.00010696735307179513",
            "extra": "mean: 267.5328761999964 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 275174.3507489493,
            "unit": "iter/sec",
            "range": "stddev: 8.912076389860668e-7",
            "extra": "mean: 3.6340596326593433 usec\nrounds: 20576"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 482242.126430678,
            "unit": "iter/sec",
            "range": "stddev: 5.415466592076189e-7",
            "extra": "mean: 2.073647127017945 usec\nrounds: 99217"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12602.225048760049,
            "unit": "iter/sec",
            "range": "stddev: 0.000012890321387579156",
            "extra": "mean: 79.35106666726219 usec\nrounds: 30"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 495118.4044022886,
            "unit": "iter/sec",
            "range": "stddev: 4.803411483841043e-7",
            "extra": "mean: 2.019718901799276 usec\nrounds: 126824"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9899273.25362869,
            "unit": "iter/sec",
            "range": "stddev: 9.981477431697053e-9",
            "extra": "mean: 101.01751657713244 nsec\nrounds: 98630"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11703.193209656405,
            "unit": "iter/sec",
            "range": "stddev: 0.000006826082726689947",
            "extra": "mean: 85.44676500554493 usec\nrounds: 4515"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304578.92532750726,
            "unit": "iter/sec",
            "range": "stddev: 9.156551827252284e-7",
            "extra": "mean: 3.2832212502054148 usec\nrounds: 6400"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "ssrjkk",
            "username": "ssrjkk",
            "email": "ssrjkk@users.noreply.github.com"
          },
          "committer": {
            "name": "ssrjkk",
            "username": "ssrjkk",
            "email": "ssrjkk@users.noreply.github.com"
          },
          "id": "e0f1a7e1003c3d5a53eaa339227164d328b7c497",
          "message": "fix: rate limit and auth in load tests\n\n- Add ENVIRONMENT=test to docker-compose.yml so rate limit is 10000\n  req/min instead of 100 — prevents 429 under 100 concurrent users\n- Add on_start + auth headers to HeavyUser so DELETE calls are\n  authenticated (was failing with 401, counting toward exit code 1)",
          "timestamp": "2026-06-18T13:43:09Z",
          "url": "https://github.com/ssrjkk/qualix/commit/e0f1a7e1003c3d5a53eaa339227164d328b7c497"
        },
        "date": 1781858441322,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.316104098869293,
            "unit": "iter/sec",
            "range": "stddev: 0.00008222988810537861",
            "extra": "mean: 301.5586875999986 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3143080407525183,
            "unit": "iter/sec",
            "range": "stddev: 0.00022804461360008256",
            "extra": "mean: 301.7221054000004 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.301463374168835,
            "unit": "iter/sec",
            "range": "stddev: 0.0029735807015670783",
            "extra": "mean: 302.89598479999995 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 291251.43801746855,
            "unit": "iter/sec",
            "range": "stddev: 7.240994661555393e-7",
            "extra": "mean: 3.4334594424904523 usec\nrounds: 17543"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 490881.17919761065,
            "unit": "iter/sec",
            "range": "stddev: 4.533605139381256e-7",
            "extra": "mean: 2.0371528638245815 usec\nrounds: 91853"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15563.811026540465,
            "unit": "iter/sec",
            "range": "stddev: 0.000013516198788727366",
            "extra": "mean: 64.25161538486508 usec\nrounds: 26"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 477223.9525282427,
            "unit": "iter/sec",
            "range": "stddev: 4.887488193681699e-7",
            "extra": "mean: 2.09545223935678 usec\nrounds: 100051"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8962888.278974773,
            "unit": "iter/sec",
            "range": "stddev: 1.0680409107135154e-8",
            "extra": "mean: 111.57117760195776 nsec\nrounds: 86829"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 14756.487142309858,
            "unit": "iter/sec",
            "range": "stddev: 0.0000045530124935669655",
            "extra": "mean: 67.76680590415019 usec\nrounds: 4302"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 307704.5045838302,
            "unit": "iter/sec",
            "range": "stddev: 6.477481746730297e-7",
            "extra": "mean: 3.249871175439886 usec\nrounds: 5589"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "ssrjkk",
            "username": "ssrjkk",
            "email": "ssrjkk@users.noreply.github.com"
          },
          "committer": {
            "name": "ssrjkk",
            "username": "ssrjkk",
            "email": "ssrjkk@users.noreply.github.com"
          },
          "id": "e0f1a7e1003c3d5a53eaa339227164d328b7c497",
          "message": "fix: rate limit and auth in load tests\n\n- Add ENVIRONMENT=test to docker-compose.yml so rate limit is 10000\n  req/min instead of 100 — prevents 429 under 100 concurrent users\n- Add on_start + auth headers to HeavyUser so DELETE calls are\n  authenticated (was failing with 401, counting toward exit code 1)",
          "timestamp": "2026-06-18T13:43:09Z",
          "url": "https://github.com/ssrjkk/qualix/commit/e0f1a7e1003c3d5a53eaa339227164d328b7c497"
        },
        "date": 1781939333620,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.3118653540315215,
            "unit": "iter/sec",
            "range": "stddev: 0.0003228968714829239",
            "extra": "mean: 301.9446424000009 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3127819230834983,
            "unit": "iter/sec",
            "range": "stddev: 0.00013374932057846203",
            "extra": "mean: 301.86110140000153 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.3010161911622227,
            "unit": "iter/sec",
            "range": "stddev: 0.0018236422417919058",
            "extra": "mean: 302.93701760000147 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 288482.15928421624,
            "unit": "iter/sec",
            "range": "stddev: 7.482404853024192e-7",
            "extra": "mean: 3.4664188679161523 usec\nrounds: 18815"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 480137.85855949536,
            "unit": "iter/sec",
            "range": "stddev: 4.616638729947913e-7",
            "extra": "mean: 2.0827351606894524 usec\nrounds: 89711"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15536.906951540052,
            "unit": "iter/sec",
            "range": "stddev: 0.000016774194936778107",
            "extra": "mean: 64.36287499944626 usec\nrounds: 24"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 479282.6593315919,
            "unit": "iter/sec",
            "range": "stddev: 4.813019816007351e-7",
            "extra": "mean: 2.08645145099679 usec\nrounds: 123123"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9058141.006054189,
            "unit": "iter/sec",
            "range": "stddev: 1.08823190406778e-8",
            "extra": "mean: 110.39792815453306 nsec\nrounds: 87048"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 14997.397089663775,
            "unit": "iter/sec",
            "range": "stddev: 0.0000038718454689100786",
            "extra": "mean: 66.67823716484784 usec\nrounds: 4402"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 307091.1673078099,
            "unit": "iter/sec",
            "range": "stddev: 5.734778263502709e-7",
            "extra": "mean: 3.2563619747410693 usec\nrounds: 5854"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "name": "ssrjkk",
            "username": "ssrjkk",
            "email": "ssrjkk@users.noreply.github.com"
          },
          "committer": {
            "name": "ssrjkk",
            "username": "ssrjkk",
            "email": "ssrjkk@users.noreply.github.com"
          },
          "id": "e0f1a7e1003c3d5a53eaa339227164d328b7c497",
          "message": "fix: rate limit and auth in load tests\n\n- Add ENVIRONMENT=test to docker-compose.yml so rate limit is 10000\n  req/min instead of 100 — prevents 429 under 100 concurrent users\n- Add on_start + auth headers to HeavyUser so DELETE calls are\n  authenticated (was failing with 401, counting toward exit code 1)",
          "timestamp": "2026-06-18T13:43:09Z",
          "url": "https://github.com/ssrjkk/qualix/commit/e0f1a7e1003c3d5a53eaa339227164d328b7c497"
        },
        "date": 1782029366345,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.312698345411725,
            "unit": "iter/sec",
            "range": "stddev: 0.00009523123170955168",
            "extra": "mean: 301.8687172 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.2916293484498644,
            "unit": "iter/sec",
            "range": "stddev: 0.002966629814036767",
            "extra": "mean: 303.8009125999963 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.311910075208416,
            "unit": "iter/sec",
            "range": "stddev: 0.00011214216976940165",
            "extra": "mean: 301.9405651999989 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 287866.2307659071,
            "unit": "iter/sec",
            "range": "stddev: 7.141611182262208e-7",
            "extra": "mean: 3.4738357373123088 usec\nrounds: 18373"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 488806.86621306307,
            "unit": "iter/sec",
            "range": "stddev: 4.6691131036450854e-7",
            "extra": "mean: 2.045797776425088 usec\nrounds: 97229"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15392.467911292613,
            "unit": "iter/sec",
            "range": "stddev: 0.000012923239474970781",
            "extra": "mean: 64.96684000012465 usec\nrounds: 25"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 479920.10612522654,
            "unit": "iter/sec",
            "range": "stddev: 4.7098776907345953e-7",
            "extra": "mean: 2.083680152669136 usec\nrounds: 112957"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9151638.538294477,
            "unit": "iter/sec",
            "range": "stddev: 1.1589981865614308e-8",
            "extra": "mean: 109.27004992773267 nsec\nrounds: 88527"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 14989.366555671477,
            "unit": "iter/sec",
            "range": "stddev: 0.000003816265859781344",
            "extra": "mean: 66.71395994526756 usec\nrounds: 4394"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304561.04233190615,
            "unit": "iter/sec",
            "range": "stddev: 5.235678380390329e-7",
            "extra": "mean: 3.2834140320225678 usec\nrounds: 6072"
          }
        ]
      }
    ]
  }
}