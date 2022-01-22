# Locust Load Test

Locust is an open source load testing tool that uses Python to define tests.

See https://locust.io/ for more details and documentation.

Define your testing files as python files, e.g. `sample_load.py`

## Running Tests

Specify a host and locust file.

locust --host https://api.k8s.staging.globomantics.net -f sample_load.py

This will bring up a web console at http://0.0.0.0:8089/ (your local machine) where you can specify parameters for number of users to simulate then provides real time statistics, charts, and errors for the requests.