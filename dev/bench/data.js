window.BENCHMARK_DATA = {
  "lastUpdate": 1784613663880,
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
        "date": 1782120067815,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.316257901500954,
            "unit": "iter/sec",
            "range": "stddev: 0.00013562856921471854",
            "extra": "mean: 301.5447018000003 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3149382481733913,
            "unit": "iter/sec",
            "range": "stddev: 0.00016543965771773477",
            "extra": "mean: 301.66474460000074 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.3170211410707076,
            "unit": "iter/sec",
            "range": "stddev: 0.00007297305410728732",
            "extra": "mean: 301.475317000002 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 289829.0512326787,
            "unit": "iter/sec",
            "range": "stddev: 7.238065323365112e-7",
            "extra": "mean: 3.4503097455099017 usec\nrounds: 19332"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 483212.52482455637,
            "unit": "iter/sec",
            "range": "stddev: 4.4389436344831896e-7",
            "extra": "mean: 2.069482781645773 usec\nrounds: 94376"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15318.881670322373,
            "unit": "iter/sec",
            "range": "stddev: 0.000013043060800768798",
            "extra": "mean: 65.27891666774366 usec\nrounds: 24"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 472271.8300908678,
            "unit": "iter/sec",
            "range": "stddev: 5.46452704722357e-7",
            "extra": "mean: 2.117424619223201 usec\nrounds: 124813"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 7479020.438784617,
            "unit": "iter/sec",
            "range": "stddev: 1.616622999022973e-8",
            "extra": "mean: 133.70734953660664 nsec\nrounds: 87513"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15002.25156716113,
            "unit": "iter/sec",
            "range": "stddev: 0.000004036108318668887",
            "extra": "mean: 66.65666120337093 usec\nrounds: 4454"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 310547.31656111195,
            "unit": "iter/sec",
            "range": "stddev: 5.474528048668455e-7",
            "extra": "mean: 3.2201212075300996 usec\nrounds: 6592"
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
        "date": 1782197990330,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.729415070231305,
            "unit": "iter/sec",
            "range": "stddev: 0.0010963302655651052",
            "extra": "mean: 268.1385635999959 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.738241745627719,
            "unit": "iter/sec",
            "range": "stddev: 0.00009772979315043032",
            "extra": "mean: 267.505439200022 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7385705542587235,
            "unit": "iter/sec",
            "range": "stddev: 0.00009240899654099735",
            "extra": "mean: 267.4819119999938 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 278434.9291317971,
            "unit": "iter/sec",
            "range": "stddev: 7.938344118551678e-7",
            "extra": "mean: 3.591503419194401 usec\nrounds: 24713"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 481567.3552736782,
            "unit": "iter/sec",
            "range": "stddev: 5.129682789168714e-7",
            "extra": "mean: 2.0765527169749554 usec\nrounds: 118681"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12933.512167195511,
            "unit": "iter/sec",
            "range": "stddev: 0.000010614459223642952",
            "extra": "mean: 77.31851851783884 usec\nrounds: 27"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 417696.68555327645,
            "unit": "iter/sec",
            "range": "stddev: 7.057396415510918e-7",
            "extra": "mean: 2.394081721465927 usec\nrounds: 146779"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 10132838.523745034,
            "unit": "iter/sec",
            "range": "stddev: 1.0169633014510839e-8",
            "extra": "mean: 98.68902950112405 nsec\nrounds: 99217"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 12021.290180685724,
            "unit": "iter/sec",
            "range": "stddev: 0.000006933507009370212",
            "extra": "mean: 83.18574670185338 usec\nrounds: 4473"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304838.2515428896,
            "unit": "iter/sec",
            "range": "stddev: 7.321445653470826e-7",
            "extra": "mean: 3.2804282104974076 usec\nrounds: 7125"
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
        "date": 1782284247193,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.673622129166139,
            "unit": "iter/sec",
            "range": "stddev: 0.009665601375813489",
            "extra": "mean: 272.21090380000135 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.738722061714272,
            "unit": "iter/sec",
            "range": "stddev: 0.00020185940782357494",
            "extra": "mean: 267.47107260000007 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7389472475656906,
            "unit": "iter/sec",
            "range": "stddev: 0.00013056908806219792",
            "extra": "mean: 267.4549635999995 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 270678.4050026543,
            "unit": "iter/sec",
            "range": "stddev: 8.303918240795541e-7",
            "extra": "mean: 3.694421060262247 usec\nrounds: 20769"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 461924.5865774771,
            "unit": "iter/sec",
            "range": "stddev: 5.389112770225276e-7",
            "extra": "mean: 2.1648555393192375 usec\nrounds: 93721"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12725.877971117534,
            "unit": "iter/sec",
            "range": "stddev: 0.000012442843252950926",
            "extra": "mean: 78.58003999956509 usec\nrounds: 25"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 495248.1767774194,
            "unit": "iter/sec",
            "range": "stddev: 4.6534591525673937e-7",
            "extra": "mean: 2.019189664678831 usec\nrounds: 132381"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 10121857.373929946,
            "unit": "iter/sec",
            "range": "stddev: 1.0947028405257207e-8",
            "extra": "mean: 98.79609671003857 nsec\nrounds: 100031"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11329.074352055768,
            "unit": "iter/sec",
            "range": "stddev: 0.000010594752902911946",
            "extra": "mean: 88.26846474165302 usec\nrounds: 4779"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 301856.49456198164,
            "unit": "iter/sec",
            "range": "stddev: 6.567828629436208e-7",
            "extra": "mean: 3.3128324817098322 usec\nrounds: 6262"
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
        "date": 1782370647636,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7325006122476796,
            "unit": "iter/sec",
            "range": "stddev: 0.0008728285005385821",
            "extra": "mean: 267.9169017999996 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.69441218590453,
            "unit": "iter/sec",
            "range": "stddev: 0.0036824092146413305",
            "extra": "mean: 270.6790551999987 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7373720523852434,
            "unit": "iter/sec",
            "range": "stddev: 0.0003657568758476619",
            "extra": "mean: 267.56768819999763 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 281731.86951209704,
            "unit": "iter/sec",
            "range": "stddev: 7.587337019541415e-7",
            "extra": "mean: 3.5494741923652406 usec\nrounds: 21544"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 489880.8629581922,
            "unit": "iter/sec",
            "range": "stddev: 4.584301747308044e-7",
            "extra": "mean: 2.041312644795726 usec\nrounds: 101441"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12445.165996415519,
            "unit": "iter/sec",
            "range": "stddev: 0.0000134921867790233",
            "extra": "mean: 80.35248387108874 usec\nrounds: 31"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 503568.3837777344,
            "unit": "iter/sec",
            "range": "stddev: 5.334625244006127e-7",
            "extra": "mean: 1.9858276099426073 usec\nrounds: 132206"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8978522.040738815,
            "unit": "iter/sec",
            "range": "stddev: 1.0926892300531665e-8",
            "extra": "mean: 111.37690540410067 nsec\nrounds: 88968"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11958.43363599273,
            "unit": "iter/sec",
            "range": "stddev: 0.000006284765595337528",
            "extra": "mean: 83.62299197699105 usec\nrounds: 4861"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304741.2610854682,
            "unit": "iter/sec",
            "range": "stddev: 8.41405273811603e-7",
            "extra": "mean: 3.281472277295389 usec\nrounds: 6060"
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
        "date": 1782457399908,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.738676460304166,
            "unit": "iter/sec",
            "range": "stddev: 0.00012177821118814348",
            "extra": "mean: 267.47433499999715 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.6906786998618064,
            "unit": "iter/sec",
            "range": "stddev: 0.007977917778921184",
            "extra": "mean: 270.9528737999989 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7290425839711245,
            "unit": "iter/sec",
            "range": "stddev: 0.0012476756410721972",
            "extra": "mean: 268.16534739999724 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 273297.9488625552,
            "unit": "iter/sec",
            "range": "stddev: 8.01845500738884e-7",
            "extra": "mean: 3.659010263933272 usec\nrounds: 22506"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 472808.44871014135,
            "unit": "iter/sec",
            "range": "stddev: 5.854931941117815e-7",
            "extra": "mean: 2.1150214272356567 usec\nrounds: 90819"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12546.68037258037,
            "unit": "iter/sec",
            "range": "stddev: 0.00001108284840799225",
            "extra": "mean: 79.70235714184679 usec\nrounds: 28"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 496422.33051481034,
            "unit": "iter/sec",
            "range": "stddev: 4.5396447763564615e-7",
            "extra": "mean: 2.014413813663376 usec\nrounds: 134157"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8890877.168520749,
            "unit": "iter/sec",
            "range": "stddev: 2.3090735709982695e-8",
            "extra": "mean: 112.47484146340743 nsec\nrounds: 86573"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11653.683919204874,
            "unit": "iter/sec",
            "range": "stddev: 0.000007764748149915946",
            "extra": "mean: 85.80977542663862 usec\nrounds: 4395"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304001.62388165004,
            "unit": "iter/sec",
            "range": "stddev: 8.829617992180732e-7",
            "extra": "mean: 3.2894561128703277 usec\nrounds: 7018"
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
        "date": 1782542243378,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.3156956978521954,
            "unit": "iter/sec",
            "range": "stddev: 0.00015497919887635524",
            "extra": "mean: 301.59583120000093 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.317152385625176,
            "unit": "iter/sec",
            "range": "stddev: 0.00009013492341820326",
            "extra": "mean: 301.4633889999999 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.3158344832752453,
            "unit": "iter/sec",
            "range": "stddev: 0.00028884149162760985",
            "extra": "mean: 301.58320779999883 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 287097.65330769646,
            "unit": "iter/sec",
            "range": "stddev: 6.889648620299334e-7",
            "extra": "mean: 3.4831354017660727 usec\nrounds: 19660"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 492100.0565445639,
            "unit": "iter/sec",
            "range": "stddev: 4.5199032082443936e-7",
            "extra": "mean: 2.0321070617666988 usec\nrounds: 88052"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15279.072254256113,
            "unit": "iter/sec",
            "range": "stddev: 0.000013197221501030502",
            "extra": "mean: 65.44900000204146 usec\nrounds: 29"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 482440.0261907796,
            "unit": "iter/sec",
            "range": "stddev: 4.973290276744079e-7",
            "extra": "mean: 2.072796504667614 usec\nrounds: 112322"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8777604.21796866,
            "unit": "iter/sec",
            "range": "stddev: 1.871423353373542e-8",
            "extra": "mean: 113.92630325629139 nsec\nrounds: 83487"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 14430.894807193567,
            "unit": "iter/sec",
            "range": "stddev: 0.000016374345292993697",
            "extra": "mean: 69.29577225533625 usec\nrounds: 4527"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 311460.2336818079,
            "unit": "iter/sec",
            "range": "stddev: 6.244406054341377e-7",
            "extra": "mean: 3.2106827513062677 usec\nrounds: 5699"
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
        "date": 1782630626561,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.9417028828751217,
            "unit": "iter/sec",
            "range": "stddev: 0.0002363361009383777",
            "extra": "mean: 253.69745759999773 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.937198325909222,
            "unit": "iter/sec",
            "range": "stddev: 0.0007516112259313727",
            "extra": "mean: 253.98771340000226 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.9438754623640437,
            "unit": "iter/sec",
            "range": "stddev: 0.0000962315186384316",
            "extra": "mean: 253.55770220000267 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 281266.8465187987,
            "unit": "iter/sec",
            "range": "stddev: 4.3410401882347433e-7",
            "extra": "mean: 3.5553425950369313 usec\nrounds: 22782"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 487301.14485301595,
            "unit": "iter/sec",
            "range": "stddev: 2.9433325902300026e-7",
            "extra": "mean: 2.052119127078244 usec\nrounds: 110571"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 14237.983142230056,
            "unit": "iter/sec",
            "range": "stddev: 0.000008109886717475014",
            "extra": "mean: 70.23466666665634 usec\nrounds: 36"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 512814.2744793485,
            "unit": "iter/sec",
            "range": "stddev: 3.3693016105471773e-7",
            "extra": "mean: 1.9500237215808447 usec\nrounds: 112893"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 10971510.765886363,
            "unit": "iter/sec",
            "range": "stddev: 8.460426890511978e-9",
            "extra": "mean: 91.14515050281796 nsec\nrounds: 105978"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 12322.77784720007,
            "unit": "iter/sec",
            "range": "stddev: 0.000002957971513313742",
            "extra": "mean: 81.15053378384289 usec\nrounds: 5180"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 325002.9191222719,
            "unit": "iter/sec",
            "range": "stddev: 3.500682835975661e-7",
            "extra": "mean: 3.0768954405107425 usec\nrounds: 7479"
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
          "id": "860b01d60785f13d11804f07ca24a202657d2409",
          "message": "fix: copy README.md in Dockerfile so hatchling wheel build can find it",
          "timestamp": "2026-06-30T23:18:17+03:00",
          "tree_id": "1bde059f4296d42e849f20b652d215c516f46ce9",
          "url": "https://github.com/ssrjkk/qualix/commit/860b01d60785f13d11804f07ca24a202657d2409"
        },
        "date": 1782850980511,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 4.2709202900712455,
            "unit": "iter/sec",
            "range": "stddev: 0.0003888438203273785",
            "extra": "mean: 234.14157419999952 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 4.269680121730728,
            "unit": "iter/sec",
            "range": "stddev: 0.00010929755166779597",
            "extra": "mean: 234.20958279999837 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 4.276540873385818,
            "unit": "iter/sec",
            "range": "stddev: 0.00005063569719004923",
            "extra": "mean: 233.83384599999886 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 375413.7017592173,
            "unit": "iter/sec",
            "range": "stddev: 5.533180032666788e-7",
            "extra": "mean: 2.6637280294084196 usec\nrounds: 22348"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 640347.6520592673,
            "unit": "iter/sec",
            "range": "stddev: 3.3220643165209584e-7",
            "extra": "mean: 1.5616517008911357 usec\nrounds: 117468"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 20636.99525353887,
            "unit": "iter/sec",
            "range": "stddev: 0.000009143192647222909",
            "extra": "mean: 48.45666666655448 usec\nrounds: 36"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 625689.3983469654,
            "unit": "iter/sec",
            "range": "stddev: 3.346577743297054e-7",
            "extra": "mean: 1.5982370847930956 usec\nrounds: 161031"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 11711899.481932854,
            "unit": "iter/sec",
            "range": "stddev: 8.918726239241768e-9",
            "extra": "mean: 85.38324646165479 nsec\nrounds: 112196"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 19706.601252116063,
            "unit": "iter/sec",
            "range": "stddev: 0.000002795276014367847",
            "extra": "mean: 50.744417426755504 usec\nrounds: 5153"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 409303.08132168505,
            "unit": "iter/sec",
            "range": "stddev: 4.549398915900796e-7",
            "extra": "mean: 2.4431773070725225 usec\nrounds: 6892"
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
          "id": "1e70ab8d0188b0fb257046699f86a2e30217acb2",
          "message": "chore: update coverage badge [skip ci]",
          "timestamp": "2026-06-30T20:24:11Z",
          "url": "https://github.com/ssrjkk/qualix/commit/1e70ab8d0188b0fb257046699f86a2e30217acb2"
        },
        "date": 1782890478409,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7379254718619035,
            "unit": "iter/sec",
            "range": "stddev: 0.00006779956329359218",
            "extra": "mean: 267.52807339999976 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.732499127143893,
            "unit": "iter/sec",
            "range": "stddev: 0.00042363909605932414",
            "extra": "mean: 267.9170083999992 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.737339962692744,
            "unit": "iter/sec",
            "range": "stddev: 0.00005064519758201232",
            "extra": "mean: 267.5699855999994 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 272330.1129782833,
            "unit": "iter/sec",
            "range": "stddev: 8.979994063369692e-7",
            "extra": "mean: 3.6720140459815545 usec\nrounds: 19009"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 468053.76859867247,
            "unit": "iter/sec",
            "range": "stddev: 5.714171504180469e-7",
            "extra": "mean: 2.136506673141305 usec\nrounds: 82495"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12381.061757025369,
            "unit": "iter/sec",
            "range": "stddev: 0.000012446076360213982",
            "extra": "mean: 80.768517242277 usec\nrounds: 29"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 494260.8646692916,
            "unit": "iter/sec",
            "range": "stddev: 4.752541550191772e-7",
            "extra": "mean: 2.0232231023775205 usec\nrounds: 123840"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9072798.043682981,
            "unit": "iter/sec",
            "range": "stddev: 1.368512983450127e-8",
            "extra": "mean: 110.21958112428824 nsec\nrounds: 87329"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11030.539166942302,
            "unit": "iter/sec",
            "range": "stddev: 0.00001578198573660524",
            "extra": "mean: 90.65739986644759 usec\nrounds: 4494"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 299763.9022151593,
            "unit": "iter/sec",
            "range": "stddev: 0.0000012836055113761983",
            "extra": "mean: 3.3359587082044233 usec\nrounds: 6224"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T19:38:31+03:00",
          "tree_id": "0a5a5f1469c4330e325fc98fc2346df400c379cf",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1782924212841,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.313202950549552,
            "unit": "iter/sec",
            "range": "stddev: 0.000600996735155211",
            "extra": "mean: 301.82274220000096 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3094810276576947,
            "unit": "iter/sec",
            "range": "stddev: 0.001020338938896956",
            "extra": "mean: 302.1621793999998 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.3103683722045636,
            "unit": "iter/sec",
            "range": "stddev: 0.0008697242432168366",
            "extra": "mean: 302.0811847999994 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 291742.49959636136,
            "unit": "iter/sec",
            "range": "stddev: 6.680555779755345e-7",
            "extra": "mean: 3.4276802364535306 usec\nrounds: 20978"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 495274.3805026629,
            "unit": "iter/sec",
            "range": "stddev: 7.865898696224801e-7",
            "extra": "mean: 2.0190828344181297 usec\nrounds: 98377"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15422.994914565359,
            "unit": "iter/sec",
            "range": "stddev: 0.000011640731858653755",
            "extra": "mean: 64.8382499987475 usec\nrounds: 28"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 485668.9624592957,
            "unit": "iter/sec",
            "range": "stddev: 4.553275780865784e-7",
            "extra": "mean: 2.0590156614832287 usec\nrounds: 135300"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8847653.43397113,
            "unit": "iter/sec",
            "range": "stddev: 1.1052930565382823e-8",
            "extra": "mean: 113.02431853404613 nsec\nrounds: 84531"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15121.4421710302,
            "unit": "iter/sec",
            "range": "stddev: 0.000005394559645775134",
            "extra": "mean: 66.13125842691178 usec\nrounds: 4628"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 310372.2801245357,
            "unit": "iter/sec",
            "range": "stddev: 5.75077590679355e-7",
            "extra": "mean: 3.221937215523093 usec\nrounds: 6371"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1782975048396,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.298980268836021,
            "unit": "iter/sec",
            "range": "stddev: 0.0024275162076713244",
            "extra": "mean: 303.12397119999446 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.315172603430643,
            "unit": "iter/sec",
            "range": "stddev: 0.00021518909985601675",
            "extra": "mean: 301.6434193999942 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.315364387678298,
            "unit": "iter/sec",
            "range": "stddev: 0.00012891791137240442",
            "extra": "mean: 301.62597020000135 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 289268.85068325413,
            "unit": "iter/sec",
            "range": "stddev: 7.25243641598943e-7",
            "extra": "mean: 3.456991645101075 usec\nrounds: 19031"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 495098.76618468814,
            "unit": "iter/sec",
            "range": "stddev: 4.5528944308387954e-7",
            "extra": "mean: 2.0197990144596063 usec\nrounds: 101062"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15517.236602039484,
            "unit": "iter/sec",
            "range": "stddev: 0.000011646584406880888",
            "extra": "mean: 64.4444642848693 usec\nrounds: 28"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 484152.67495971697,
            "unit": "iter/sec",
            "range": "stddev: 4.6250416696471805e-7",
            "extra": "mean: 2.065464163929701 usec\nrounds: 132785"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9085082.381404137,
            "unit": "iter/sec",
            "range": "stddev: 1.24758099282793e-8",
            "extra": "mean: 110.07054840216495 nsec\nrounds: 86980"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15159.124542747446,
            "unit": "iter/sec",
            "range": "stddev: 0.000004219701326968415",
            "extra": "mean: 65.96687013026938 usec\nrounds: 4235"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 307200.068411052,
            "unit": "iter/sec",
            "range": "stddev: 5.776644879679337e-7",
            "extra": "mean: 3.255207608423903 usec\nrounds: 6151"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783060910436,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.717495913696911,
            "unit": "iter/sec",
            "range": "stddev: 0.0014752386379046504",
            "extra": "mean: 268.9982781999987 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.737693664168015,
            "unit": "iter/sec",
            "range": "stddev: 0.00009109559825606786",
            "extra": "mean: 267.54466520000193 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7314060798048674,
            "unit": "iter/sec",
            "range": "stddev: 0.0006093983560732827",
            "extra": "mean: 267.9954897999991 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 282431.72707742016,
            "unit": "iter/sec",
            "range": "stddev: 7.622923656388163e-7",
            "extra": "mean: 3.5406786990538075 usec\nrounds: 22107"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 485238.695334324,
            "unit": "iter/sec",
            "range": "stddev: 5.19343813393988e-7",
            "extra": "mean: 2.0608414160189996 usec\nrounds: 101637"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12905.890248347114,
            "unit": "iter/sec",
            "range": "stddev: 0.000010909525093091438",
            "extra": "mean: 77.48399999977315 usec\nrounds: 26"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 506086.657709967,
            "unit": "iter/sec",
            "range": "stddev: 5.344960255238865e-7",
            "extra": "mean: 1.9759461838511652 usec\nrounds: 143823"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8955961.894282285,
            "unit": "iter/sec",
            "range": "stddev: 1.1687979401437061e-8",
            "extra": "mean: 111.65746480435848 nsec\nrounds: 89358"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11881.609444261754,
            "unit": "iter/sec",
            "range": "stddev: 0.000007244689353741679",
            "extra": "mean: 84.16368209131397 usec\nrounds: 4992"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 311177.8848891079,
            "unit": "iter/sec",
            "range": "stddev: 6.440635864637951e-7",
            "extra": "mean: 3.213595980178227 usec\nrounds: 6866"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783146579805,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7362977649856814,
            "unit": "iter/sec",
            "range": "stddev: 0.00016861183390140232",
            "extra": "mean: 267.6446212000002 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.738205596866897,
            "unit": "iter/sec",
            "range": "stddev: 0.00005071734614690235",
            "extra": "mean: 267.5080259999959 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7376663439436126,
            "unit": "iter/sec",
            "range": "stddev: 0.00005383680129415023",
            "extra": "mean: 267.5466207999989 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 274645.2424847575,
            "unit": "iter/sec",
            "range": "stddev: 8.524581071400358e-7",
            "extra": "mean: 3.6410607041754925 usec\nrounds: 23458"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 474804.85127306497,
            "unit": "iter/sec",
            "range": "stddev: 5.310851691237634e-7",
            "extra": "mean: 2.1061284384916488 usec\nrounds: 104844"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12675.661242314374,
            "unit": "iter/sec",
            "range": "stddev: 0.000011123907473458268",
            "extra": "mean: 78.89134782663345 usec\nrounds: 23"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 490757.13304904243,
            "unit": "iter/sec",
            "range": "stddev: 4.815101569723642e-7",
            "extra": "mean: 2.0376677844437316 usec\nrounds: 144030"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8936317.69927629,
            "unit": "iter/sec",
            "range": "stddev: 1.164829430128913e-8",
            "extra": "mean: 111.9029150094994 nsec\nrounds: 87245"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11408.399675690287,
            "unit": "iter/sec",
            "range": "stddev: 0.000007392982550866719",
            "extra": "mean: 87.65471305593027 usec\nrounds: 4297"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 295948.4565260158,
            "unit": "iter/sec",
            "range": "stddev: 6.748764405593459e-7",
            "extra": "mean: 3.3789667692086556 usec\nrounds: 7162"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783234268558,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7385934234183282,
            "unit": "iter/sec",
            "range": "stddev: 0.00010643947762401266",
            "extra": "mean: 267.48027579999984 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.7362575636377926,
            "unit": "iter/sec",
            "range": "stddev: 0.00025986526244023574",
            "extra": "mean: 267.647500999999 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7382729955573497,
            "unit": "iter/sec",
            "range": "stddev: 0.00004302810726245397",
            "extra": "mean: 267.5032030000011 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 273238.537580906,
            "unit": "iter/sec",
            "range": "stddev: 8.468653594262095e-7",
            "extra": "mean: 3.6598058562800637 usec\nrounds: 20969"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 471624.68846471165,
            "unit": "iter/sec",
            "range": "stddev: 5.25553475712865e-7",
            "extra": "mean: 2.120330051540173 usec\nrounds: 92937"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12823.636526817416,
            "unit": "iter/sec",
            "range": "stddev: 0.0000123091264871675",
            "extra": "mean: 77.98100000017554 usec\nrounds: 26"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 489221.6967026455,
            "unit": "iter/sec",
            "range": "stddev: 5.47867472412362e-7",
            "extra": "mean: 2.0440630633105616 usec\nrounds: 33506"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9026560.237365266,
            "unit": "iter/sec",
            "range": "stddev: 1.0740089420227118e-8",
            "extra": "mean: 110.78417178899664 nsec\nrounds: 86874"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11396.357152997072,
            "unit": "iter/sec",
            "range": "stddev: 0.000009899551304041552",
            "extra": "mean: 87.74733773037421 usec\nrounds: 4776"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 298196.0021704894,
            "unit": "iter/sec",
            "range": "stddev: 8.906792245760716e-7",
            "extra": "mean: 3.3534990164900464 usec\nrounds: 6609"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783322571591,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.314711553422725,
            "unit": "iter/sec",
            "range": "stddev: 0.00043548640497252964",
            "extra": "mean: 301.68537560000175 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3170594724734626,
            "unit": "iter/sec",
            "range": "stddev: 0.000251221348068995",
            "extra": "mean: 301.4718332000001 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.3169316216941147,
            "unit": "iter/sec",
            "range": "stddev: 0.00014819466362786217",
            "extra": "mean: 301.4834533999988 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 279092.1561016076,
            "unit": "iter/sec",
            "range": "stddev: 6.851138011537748e-7",
            "extra": "mean: 3.583045879784365 usec\nrounds: 18919"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 454764.19738316984,
            "unit": "iter/sec",
            "range": "stddev: 5.668689761591653e-7",
            "extra": "mean: 2.1989417939104645 usec\nrounds: 95557"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 14731.389481189715,
            "unit": "iter/sec",
            "range": "stddev: 0.000014220308349929831",
            "extra": "mean: 67.88225925849592 usec\nrounds: 27"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 474682.362685772,
            "unit": "iter/sec",
            "range": "stddev: 4.683734670466584e-7",
            "extra": "mean: 2.106671910753034 usec\nrounds: 118864"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8993035.671097985,
            "unit": "iter/sec",
            "range": "stddev: 1.0971978469535908e-8",
            "extra": "mean: 111.19715706386243 nsec\nrounds: 87283"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15412.94650684028,
            "unit": "iter/sec",
            "range": "stddev: 0.00000323951509841053",
            "extra": "mean: 64.88052103186104 usec\nrounds: 4303"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 306804.6300167325,
            "unit": "iter/sec",
            "range": "stddev: 6.056822276587336e-7",
            "extra": "mean: 3.25940322330032 usec\nrounds: 6329"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783407375003,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7363223960326244,
            "unit": "iter/sec",
            "range": "stddev: 0.00037520395018068495",
            "extra": "mean: 267.642856800002 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.7370180347100455,
            "unit": "iter/sec",
            "range": "stddev: 0.0002152696342029075",
            "extra": "mean: 267.5930355999981 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.727682757533106,
            "unit": "iter/sec",
            "range": "stddev: 0.0015254917255723337",
            "extra": "mean: 268.2631717999996 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 276989.7727178734,
            "unit": "iter/sec",
            "range": "stddev: 8.756229362711631e-7",
            "extra": "mean: 3.610241599131334 usec\nrounds: 21962"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 479161.6249001788,
            "unit": "iter/sec",
            "range": "stddev: 4.98404290487969e-7",
            "extra": "mean: 2.0869784808170406 usec\nrounds: 90245"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12605.259544514653,
            "unit": "iter/sec",
            "range": "stddev: 0.000011493496645118541",
            "extra": "mean: 79.33196428590503 usec\nrounds: 28"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 490010.4240142616,
            "unit": "iter/sec",
            "range": "stddev: 5.684157801675668e-7",
            "extra": "mean: 2.040772912151141 usec\nrounds: 122926"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9002808.297715789,
            "unit": "iter/sec",
            "range": "stddev: 1.2327045615572611e-8",
            "extra": "mean: 111.07645158385992 nsec\nrounds: 88803"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11312.632568462504,
            "unit": "iter/sec",
            "range": "stddev: 0.000007586826277930166",
            "extra": "mean: 88.39675415498 usec\nrounds: 4633"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 300752.4999607243,
            "unit": "iter/sec",
            "range": "stddev: 6.910348125679814e-7",
            "extra": "mean: 3.324993142635859 usec\nrounds: 5979"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783490894566,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.316414454850802,
            "unit": "iter/sec",
            "range": "stddev: 0.00018503847825291419",
            "extra": "mean: 301.53046720000134 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3164583926595332,
            "unit": "iter/sec",
            "range": "stddev: 0.0001697928013358824",
            "extra": "mean: 301.5264723999991 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.317271159455635,
            "unit": "iter/sec",
            "range": "stddev: 0.00017636380581338826",
            "extra": "mean: 301.4525951999957 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 286362.9849135372,
            "unit": "iter/sec",
            "range": "stddev: 6.463340957512073e-7",
            "extra": "mean: 3.4920714361946397 usec\nrounds: 18898"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 482219.719282559,
            "unit": "iter/sec",
            "range": "stddev: 5.994632480381958e-7",
            "extra": "mean: 2.0737434825099825 usec\nrounds: 88684"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15230.01124481856,
            "unit": "iter/sec",
            "range": "stddev: 0.000013597265191335593",
            "extra": "mean: 65.65983333336096 usec\nrounds: 24"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 474888.3990554342,
            "unit": "iter/sec",
            "range": "stddev: 5.369233581381681e-7",
            "extra": "mean: 2.105757904360323 usec\nrounds: 107251"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9042080.846999548,
            "unit": "iter/sec",
            "range": "stddev: 1.0560209868294459e-8",
            "extra": "mean: 110.5940122545832 nsec\nrounds: 88130"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 14889.928612946042,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037094284487151278",
            "extra": "mean: 67.15948920873606 usec\nrounds: 4170"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 308372.7995123362,
            "unit": "iter/sec",
            "range": "stddev: 5.949595689432658e-7",
            "extra": "mean: 3.2428281663668455 usec\nrounds: 6419"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783580713706,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 4.083022163832483,
            "unit": "iter/sec",
            "range": "stddev: 0.001274001224625126",
            "extra": "mean: 244.91662299999888 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.9678197439170635,
            "unit": "iter/sec",
            "range": "stddev: 0.0029898118184376746",
            "extra": "mean: 252.02757800000057 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 4.058776012127216,
            "unit": "iter/sec",
            "range": "stddev: 0.0017665105277650491",
            "extra": "mean: 246.37969600000105 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 381797.81841110694,
            "unit": "iter/sec",
            "range": "stddev: 9.665949456118212e-7",
            "extra": "mean: 2.6191873074644807 usec\nrounds: 18830"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 691400.1450992115,
            "unit": "iter/sec",
            "range": "stddev: 3.24332720891555e-7",
            "extra": "mean: 1.4463404543493499 usec\nrounds: 107101"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 18714.987377476707,
            "unit": "iter/sec",
            "range": "stddev: 0.00001613527474983681",
            "extra": "mean: 53.43311111197914 usec\nrounds: 45"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 569820.5308978069,
            "unit": "iter/sec",
            "range": "stddev: 4.4015422570328776e-7",
            "extra": "mean: 1.7549385214751811 usec\nrounds: 139626"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 14298721.343257718,
            "unit": "iter/sec",
            "range": "stddev: 7.503483820402416e-9",
            "extra": "mean: 69.93632339520558 nsec\nrounds: 141443"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 16545.078200989286,
            "unit": "iter/sec",
            "range": "stddev: 0.000004576416900959924",
            "extra": "mean: 60.440935234758 usec\nrounds: 5049"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 420551.65275436174,
            "unit": "iter/sec",
            "range": "stddev: 5.356920464791673e-7",
            "extra": "mean: 2.3778291999344154 usec\nrounds: 6774"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783666538363,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7387642423315817,
            "unit": "iter/sec",
            "range": "stddev: 0.00007732897923254947",
            "extra": "mean: 267.4680550000062 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.7187126898070044,
            "unit": "iter/sec",
            "range": "stddev: 0.003205935772328546",
            "extra": "mean: 268.91026099999635 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.731723565707595,
            "unit": "iter/sec",
            "range": "stddev: 0.0012509625066245884",
            "extra": "mean: 267.9726893999941 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 276852.41526297986,
            "unit": "iter/sec",
            "range": "stddev: 8.811551812837105e-7",
            "extra": "mean: 3.6120327830628027 usec\nrounds: 22542"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 477690.3083805946,
            "unit": "iter/sec",
            "range": "stddev: 5.605237649384405e-7",
            "extra": "mean: 2.093406507220282 usec\nrounds: 96815"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12544.12153526671,
            "unit": "iter/sec",
            "range": "stddev: 0.000011864239382166306",
            "extra": "mean: 79.71861538399375 usec\nrounds: 26"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 507479.91512414976,
            "unit": "iter/sec",
            "range": "stddev: 4.5546888847596775e-7",
            "extra": "mean: 1.9705213353229165 usec\nrounds: 134355"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8760274.47338319,
            "unit": "iter/sec",
            "range": "stddev: 1.4531080083412825e-8",
            "extra": "mean: 114.15167447530936 nsec\nrounds: 87944"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11870.360081722765,
            "unit": "iter/sec",
            "range": "stddev: 0.000007540477998166744",
            "extra": "mean: 84.2434427528224 usec\nrounds: 4926"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304850.49473116104,
            "unit": "iter/sec",
            "range": "stddev: 7.770338129164056e-7",
            "extra": "mean: 3.280296464277913 usec\nrounds: 6618"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783749033365,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7305971641492546,
            "unit": "iter/sec",
            "range": "stddev: 0.0007815740326343191",
            "extra": "mean: 268.05360000000036 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.738330505065741,
            "unit": "iter/sec",
            "range": "stddev: 0.00009382045144902762",
            "extra": "mean: 267.49908780000027 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.733795919383413,
            "unit": "iter/sec",
            "range": "stddev: 0.000784073550988264",
            "extra": "mean: 267.823957600001 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 280026.90484161937,
            "unit": "iter/sec",
            "range": "stddev: 9.509564568018344e-7",
            "extra": "mean: 3.5710854304003066 usec\nrounds: 18717"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 483503.7233432443,
            "unit": "iter/sec",
            "range": "stddev: 5.346628750123562e-7",
            "extra": "mean: 2.0682363996814344 usec\nrounds: 88803"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12672.14452888109,
            "unit": "iter/sec",
            "range": "stddev: 0.00001202157256110534",
            "extra": "mean: 78.9132413792235 usec\nrounds: 29"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 494833.34922662016,
            "unit": "iter/sec",
            "range": "stddev: 5.724723232238823e-7",
            "extra": "mean: 2.0208823870964028 usec\nrounds: 122325"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8962032.3277898,
            "unit": "iter/sec",
            "range": "stddev: 1.1068166994183468e-8",
            "extra": "mean: 111.58183360923205 nsec\nrounds: 88803"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11240.30776868935,
            "unit": "iter/sec",
            "range": "stddev: 0.000007095046793468036",
            "extra": "mean: 88.96553551545702 usec\nrounds: 4491"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 307291.4090124327,
            "unit": "iter/sec",
            "range": "stddev: 6.373491885188938e-7",
            "extra": "mean: 3.254240016711763 usec\nrounds: 7162"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783836809684,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.316427158288075,
            "unit": "iter/sec",
            "range": "stddev: 0.00038047112060604545",
            "extra": "mean: 301.52931219999886 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.301062609611255,
            "unit": "iter/sec",
            "range": "stddev: 0.0018521163949218914",
            "extra": "mean: 302.9327577999993 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.309930213583628,
            "unit": "iter/sec",
            "range": "stddev: 0.0015197349951932692",
            "extra": "mean: 302.1211734000005 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 289457.2543249856,
            "unit": "iter/sec",
            "range": "stddev: 6.989831189850933e-7",
            "extra": "mean: 3.4547415380277835 usec\nrounds: 15747"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 435129.28201127966,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010043858357013857",
            "extra": "mean: 2.2981675592544413 usec\nrounds: 83278"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 13888.458583950474,
            "unit": "iter/sec",
            "range": "stddev: 0.000017544575035529383",
            "extra": "mean: 72.00223076991436 usec\nrounds: 13"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 487699.5274691866,
            "unit": "iter/sec",
            "range": "stddev: 6.832853902373121e-7",
            "extra": "mean: 2.0504428314484704 usec\nrounds: 108425"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 9072942.033195728,
            "unit": "iter/sec",
            "range": "stddev: 1.909180253255383e-8",
            "extra": "mean: 110.21783191617875 nsec\nrounds: 86671"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 13722.913213381862,
            "unit": "iter/sec",
            "range": "stddev: 0.000019688564098278852",
            "extra": "mean: 72.87082447077292 usec\nrounds: 3874"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 317116.23414298875,
            "unit": "iter/sec",
            "range": "stddev: 6.605078418572732e-7",
            "extra": "mean: 3.1534178712184655 usec\nrounds: 3805"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1783924212465,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.733245954670995,
            "unit": "iter/sec",
            "range": "stddev: 0.0004497552934671978",
            "extra": "mean: 267.86341219999485 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.735977052164574,
            "unit": "iter/sec",
            "range": "stddev: 0.0000712379421908921",
            "extra": "mean: 267.66759699999056 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7382583054261924,
            "unit": "iter/sec",
            "range": "stddev: 0.00014252987142920304",
            "extra": "mean: 267.50425420000283 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 279523.62235313654,
            "unit": "iter/sec",
            "range": "stddev: 7.978171644942003e-7",
            "extra": "mean: 3.5775151723550884 usec\nrounds: 21948"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 488827.6181885905,
            "unit": "iter/sec",
            "range": "stddev: 5.017657292219082e-7",
            "extra": "mean: 2.04571092710682 usec\nrounds: 85456"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12325.348470729847,
            "unit": "iter/sec",
            "range": "stddev: 0.000014193036466749672",
            "extra": "mean: 81.13360870686887 usec\nrounds: 23"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 504091.0394259087,
            "unit": "iter/sec",
            "range": "stddev: 4.731033084812247e-7",
            "extra": "mean: 1.9837686484942565 usec\nrounds: 111657"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8774238.621375123,
            "unit": "iter/sec",
            "range": "stddev: 1.2476852000823434e-8",
            "extra": "mean: 113.97000277196443 nsec\nrounds: 86573"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11930.884663448172,
            "unit": "iter/sec",
            "range": "stddev: 0.0000072105292799273264",
            "extra": "mean: 83.81608138947406 usec\nrounds: 4116"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 308517.897895931,
            "unit": "iter/sec",
            "range": "stddev: 7.073291728076118e-7",
            "extra": "mean: 3.241303038883401 usec\nrounds: 6646"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784007685844,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.717124267982805,
            "unit": "iter/sec",
            "range": "stddev: 0.0034979601868885928",
            "extra": "mean: 269.0251732000007 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.7397121705546654,
            "unit": "iter/sec",
            "range": "stddev: 0.000028658575866938647",
            "extra": "mean: 267.4002582 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7325500699438994,
            "unit": "iter/sec",
            "range": "stddev: 0.0010028130563242872",
            "extra": "mean: 267.91335180000146 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 279961.1551182843,
            "unit": "iter/sec",
            "range": "stddev: 7.915786429243309e-7",
            "extra": "mean: 3.571924110605621 usec\nrounds: 23218"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 491691.32644445024,
            "unit": "iter/sec",
            "range": "stddev: 4.816362306855379e-7",
            "extra": "mean: 2.0337962990546608 usec\nrounds: 107216"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12864.854303462615,
            "unit": "iter/sec",
            "range": "stddev: 0.000010545007756642511",
            "extra": "mean: 77.73115625031579 usec\nrounds: 32"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 498772.4486401567,
            "unit": "iter/sec",
            "range": "stddev: 4.609569372016471e-7",
            "extra": "mean: 2.00492229016735 usec\nrounds: 137666"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8740568.483759016,
            "unit": "iter/sec",
            "range": "stddev: 1.0908203457819302e-8",
            "extra": "mean: 114.40903436179414 nsec\nrounds: 87859"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11745.238372037635,
            "unit": "iter/sec",
            "range": "stddev: 0.00000655046581697354",
            "extra": "mean: 85.1408858913192 usec\nrounds: 5004"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 304241.78095074464,
            "unit": "iter/sec",
            "range": "stddev: 7.38119234695385e-7",
            "extra": "mean: 3.2868595393934252 usec\nrounds: 7034"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784094145221,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 4.134785691030949,
            "unit": "iter/sec",
            "range": "stddev: 0.0002783934299682576",
            "extra": "mean: 241.8505032000013 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 4.13969340074509,
            "unit": "iter/sec",
            "range": "stddev: 0.00005338533996655335",
            "extra": "mean: 241.5637834000009 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 4.118277791478424,
            "unit": "iter/sec",
            "range": "stddev: 0.0009554444249906465",
            "extra": "mean: 242.81994819999966 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 397682.1206221854,
            "unit": "iter/sec",
            "range": "stddev: 8.24084875752539e-7",
            "extra": "mean: 2.5145711817153624 usec\nrounds: 19099"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 685727.3683226709,
            "unit": "iter/sec",
            "range": "stddev: 3.961676026599913e-7",
            "extra": "mean: 1.4583055106084772 usec\nrounds: 112474"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 18857.258694460816,
            "unit": "iter/sec",
            "range": "stddev: 0.0000075553125106896595",
            "extra": "mean: 53.0299772730881 usec\nrounds: 44"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 557020.243990854,
            "unit": "iter/sec",
            "range": "stddev: 5.497715911413185e-7",
            "extra": "mean: 1.7952668880314868 usec\nrounds: 130107"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 14551558.607796678,
            "unit": "iter/sec",
            "range": "stddev: 7.739483550689397e-9",
            "extra": "mean: 68.7211608703004 nsec\nrounds: 135631"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 17077.984136341445,
            "unit": "iter/sec",
            "range": "stddev: 0.000004645140709233735",
            "extra": "mean: 58.554920300694604 usec\nrounds: 5320"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 435018.76108373347,
            "unit": "iter/sec",
            "range": "stddev: 5.418706845682176e-7",
            "extra": "mean: 2.2987514320273594 usec\nrounds: 6634"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784181046425,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.317331695148278,
            "unit": "iter/sec",
            "range": "stddev: 0.000143799758051395",
            "extra": "mean: 301.4470941999974 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.3181448042161854,
            "unit": "iter/sec",
            "range": "stddev: 0.00007146130518795481",
            "extra": "mean: 301.3732248000011 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.3176514914401034,
            "unit": "iter/sec",
            "range": "stddev: 0.00010429959802098939",
            "extra": "mean: 301.41803700000054 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 255275.11533543697,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013684016308135884",
            "extra": "mean: 3.9173422708515027 usec\nrounds: 18275"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 475776.47113259765,
            "unit": "iter/sec",
            "range": "stddev: 6.19956663738026e-7",
            "extra": "mean: 2.101827351023634 usec\nrounds: 95448"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 14997.57539207903,
            "unit": "iter/sec",
            "range": "stddev: 0.000015195782806058572",
            "extra": "mean: 66.67744444399659 usec\nrounds: 18"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 477496.49893107166,
            "unit": "iter/sec",
            "range": "stddev: 5.432787956262267e-7",
            "extra": "mean: 2.0942561929534764 usec\nrounds: 110327"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8781395.986239685,
            "unit": "iter/sec",
            "range": "stddev: 1.1584240290184177e-8",
            "extra": "mean: 113.87711037823428 nsec\nrounds: 84890"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15390.120259432175,
            "unit": "iter/sec",
            "range": "stddev: 0.0000034789994662360118",
            "extra": "mean: 64.97675022306132 usec\nrounds: 4484"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 310485.04376487905,
            "unit": "iter/sec",
            "range": "stddev: 5.455925739892182e-7",
            "extra": "mean: 3.2207670549093175 usec\nrounds: 6010"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784267457376,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 4.107884401871966,
            "unit": "iter/sec",
            "range": "stddev: 0.0012268088999516907",
            "extra": "mean: 243.43430879999914 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 4.093950099001053,
            "unit": "iter/sec",
            "range": "stddev: 0.0021934281511546807",
            "extra": "mean: 244.26286980000214 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 4.123880614876862,
            "unit": "iter/sec",
            "range": "stddev: 0.001000017427105452",
            "extra": "mean: 242.49004600000035 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 400400.1884172102,
            "unit": "iter/sec",
            "range": "stddev: 4.3112248840258924e-7",
            "extra": "mean: 2.497501322247174 usec\nrounds: 21176"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 694590.4699374095,
            "unit": "iter/sec",
            "range": "stddev: 3.3017122354429807e-7",
            "extra": "mean: 1.4396972651958664 usec\nrounds: 86551"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 19150.541556489366,
            "unit": "iter/sec",
            "range": "stddev: 0.000007918119170100618",
            "extra": "mean: 52.217844443210495 usec\nrounds: 45"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 571226.1684579261,
            "unit": "iter/sec",
            "range": "stddev: 4.2984282456318926e-7",
            "extra": "mean: 1.750620078732712 usec\nrounds: 137439"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 14437730.390420748,
            "unit": "iter/sec",
            "range": "stddev: 8.961078972767282e-9",
            "extra": "mean: 69.26296398106226 nsec\nrounds: 139704"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 17150.061412878986,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036666657773289154",
            "extra": "mean: 58.30882910127898 usec\nrounds: 5553"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 455095.4019970126,
            "unit": "iter/sec",
            "range": "stddev: 3.97272054840568e-7",
            "extra": "mean: 2.19734147084739 usec\nrounds: 6636"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784353015615,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7045005747062145,
            "unit": "iter/sec",
            "range": "stddev: 0.003368592592998857",
            "extra": "mean: 269.9419206000002 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.7286741733920707,
            "unit": "iter/sec",
            "range": "stddev: 0.0016455417243870835",
            "extra": "mean: 268.1918434000025 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.719622043907392,
            "unit": "iter/sec",
            "range": "stddev: 0.0012527658647541956",
            "extra": "mean: 268.8445191999989 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 272746.5905107379,
            "unit": "iter/sec",
            "range": "stddev: 7.825773905750848e-7",
            "extra": "mean: 3.6664069681950076 usec\nrounds: 23191"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 468776.1243820449,
            "unit": "iter/sec",
            "range": "stddev: 5.260145061504638e-7",
            "extra": "mean: 2.1332144449938246 usec\nrounds: 93721"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12282.705774781933,
            "unit": "iter/sec",
            "range": "stddev: 0.000013567302826646433",
            "extra": "mean: 81.41528571441776 usec\nrounds: 28"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 496019.59168520075,
            "unit": "iter/sec",
            "range": "stddev: 4.80728327254249e-7",
            "extra": "mean: 2.016049399586319 usec\nrounds: 141985"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8918327.802363243,
            "unit": "iter/sec",
            "range": "stddev: 1.027690376976202e-8",
            "extra": "mean: 112.12864363821802 nsec\nrounds: 86791"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11588.142613250273,
            "unit": "iter/sec",
            "range": "stddev: 0.000006959186741916498",
            "extra": "mean: 86.29510641822498 usec\nrounds: 4830"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 301578.62015750114,
            "unit": "iter/sec",
            "range": "stddev: 7.129608071604073e-7",
            "extra": "mean: 3.3158849240630666 usec\nrounds: 6978"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784441350990,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.736760685849926,
            "unit": "iter/sec",
            "range": "stddev: 0.000269909017170995",
            "extra": "mean: 267.6114646000002 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.7245097587586096,
            "unit": "iter/sec",
            "range": "stddev: 0.001149157961150031",
            "extra": "mean: 268.4917115999994 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.7369462264977296,
            "unit": "iter/sec",
            "range": "stddev: 0.00009180041207256998",
            "extra": "mean: 267.5981776000029 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 271851.4445024344,
            "unit": "iter/sec",
            "range": "stddev: 8.456920300953794e-7",
            "extra": "mean: 3.6784796263646307 usec\nrounds: 20983"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 465273.2796239382,
            "unit": "iter/sec",
            "range": "stddev: 5.435683390991402e-7",
            "extra": "mean: 2.1492745098284174 usec\nrounds: 76959"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12504.48749758588,
            "unit": "iter/sec",
            "range": "stddev: 0.000011273888796753987",
            "extra": "mean: 79.97129032221915 usec\nrounds: 31"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 494471.8890499063,
            "unit": "iter/sec",
            "range": "stddev: 5.715022982017996e-7",
            "extra": "mean: 2.02235965713123 usec\nrounds: 119119"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8714331.002780752,
            "unit": "iter/sec",
            "range": "stddev: 1.254187615367479e-8",
            "extra": "mean: 114.75350198206827 nsec\nrounds: 86274"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11470.28261716397,
            "unit": "iter/sec",
            "range": "stddev: 0.00001113133450342328",
            "extra": "mean: 87.18181001953815 usec\nrounds: 4611"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 298359.01601918566,
            "unit": "iter/sec",
            "range": "stddev: 9.453546571773522e-7",
            "extra": "mean: 3.3516667716041004 usec\nrounds: 6353"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784528828795,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.7365432160640744,
            "unit": "iter/sec",
            "range": "stddev: 0.0003207258534994373",
            "extra": "mean: 267.6270398 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.7280499353976686,
            "unit": "iter/sec",
            "range": "stddev: 0.0011809898773113433",
            "extra": "mean: 268.23675039999983 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.739239466258213,
            "unit": "iter/sec",
            "range": "stddev: 0.00007440662390338582",
            "extra": "mean: 267.4340622000017 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 282947.95919895946,
            "unit": "iter/sec",
            "range": "stddev: 7.523982159914942e-7",
            "extra": "mean: 3.534218811229643 usec\nrounds: 21434"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 490995.4397859372,
            "unit": "iter/sec",
            "range": "stddev: 5.060924850975085e-7",
            "extra": "mean: 2.036678793668587 usec\nrounds: 94967"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 12625.747590039804,
            "unit": "iter/sec",
            "range": "stddev: 0.000011691545309410412",
            "extra": "mean: 79.20323076859859 usec\nrounds: 26"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 505994.5946681541,
            "unit": "iter/sec",
            "range": "stddev: 5.171565695083884e-7",
            "extra": "mean: 1.976305696814467 usec\nrounds: 120541"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8855711.352581559,
            "unit": "iter/sec",
            "range": "stddev: 1.1969937608819743e-8",
            "extra": "mean: 112.92147634288989 nsec\nrounds: 87859"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 11887.651552890604,
            "unit": "iter/sec",
            "range": "stddev: 0.0000068979788103549185",
            "extra": "mean: 84.12090441503896 usec\nrounds: 4394"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 308783.10186397244,
            "unit": "iter/sec",
            "range": "stddev: 7.688972694482108e-7",
            "extra": "mean: 3.238519186974577 usec\nrounds: 5707"
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
          "id": "9c866cdd361d5e9e1be7b998e1da8bb41a063ffb",
          "message": "fix: ruff format",
          "timestamp": "2026-07-01T16:38:31Z",
          "url": "https://github.com/ssrjkk/qualix/commit/9c866cdd361d5e9e1be7b998e1da8bb41a063ffb"
        },
        "date": 1784613661224,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/unit/test_performance.py::test_benchmark_hash_password",
            "value": 3.309580426074975,
            "unit": "iter/sec",
            "range": "stddev: 0.0015557171087765818",
            "extra": "mean: 302.15310439999143 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_password",
            "value": 3.2883734528650943,
            "unit": "iter/sec",
            "range": "stddev: 0.006091503921942304",
            "extra": "mean: 304.101713 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_wrong_password",
            "value": 3.3126867679135397,
            "unit": "iter/sec",
            "range": "stddev: 0.0012129944926172014",
            "extra": "mean: 301.8697721999956 msec\nrounds: 5"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_create_token",
            "value": 291072.24516799,
            "unit": "iter/sec",
            "range": "stddev: 7.447349288439945e-7",
            "extra": "mean: 3.435573183636448 usec\nrounds: 18235"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_verify_token",
            "value": 498202.9622500971,
            "unit": "iter/sec",
            "range": "stddev: 4.4367155489278726e-7",
            "extra": "mean: 2.007214078943998 usec\nrounds: 96016"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_email",
            "value": 15044.875519931438,
            "unit": "iter/sec",
            "range": "stddev: 0.000014366686311214002",
            "extra": "mean: 66.46781481675943 usec\nrounds: 27"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_sanitize_string",
            "value": 486143.1229740124,
            "unit": "iter/sec",
            "range": "stddev: 4.416402976661448e-7",
            "extra": "mean: 2.057007397085933 usec\nrounds: 125455"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_validate_amount",
            "value": 8959945.30321419,
            "unit": "iter/sec",
            "range": "stddev: 1.0047254231160793e-8",
            "extra": "mean: 111.60782417290775 nsec\nrounds: 88371"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_create_model",
            "value": 15416.167766919645,
            "unit": "iter/sec",
            "range": "stddev: 0.0000038078631463655527",
            "extra": "mean: 64.86696402888286 usec\nrounds: 4031"
          },
          {
            "name": "tests/unit/test_performance.py::test_benchmark_user_response_model",
            "value": 308816.80759301037,
            "unit": "iter/sec",
            "range": "stddev: 6.102246348886665e-7",
            "extra": "mean: 3.238165719651826 usec\nrounds: 5280"
          }
        ]
      }
    ]
  }
}