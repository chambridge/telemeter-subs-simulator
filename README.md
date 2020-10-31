# telemeter-subs-simulator
Simulate the metric data in telemeter for subscription association

## Prerequisites
You need:

- Python 3.8.x
- Pipenv
- Docker (Local Development Only)
- Docker Compose (Local Development Only)

## Development
This section covers the steps to get started and run the project.

### Getting Started
To get started developing you need to clone a local copy of the git repository.

0. Clone the repository
```bash
git clone https://github.com/chambridge/telemeter-subs-simulator.git
```

1. Change to the cloned directory:
```bash
cd telemeter-subs-simulator
```
2. Copy .env.example into a .env:

```bash
cp .env.example .env
```

3. Update the environment variables:
```
NAMESPACE=NAMESPACE
PROMETHEUS_PUSH_GATEWAY=PROMETHEUS_PUSH_GATEWAY
```

4. Install the requirements:

```bash
pipenv install --dev
```

5. Activate the virtual environment:
```bash
pipenv shell
```

6. Install pre-commit hooks for the repository:
```bash
pre-commit install
```

### Linting
You can execute linting using pre-commit with a make command:
```bash
make lint
```

### Developing with Docker Compose

1. Launch Prometheus, Prometheus Push Gateway, and Grafana monitoring stack components:
```bash
make docker-up
```

2. Execute pendo-prom-emittter:
```bash
make run-job
```

3. Review metrics using local containers:

 - Launch the Prometheus console at http://localhost:9090
 - Launch the Prometheus Push Gateway console at http://localhost:9091
 - Launch the Grafana console at http://localhost:3000
    - Login with `admin/password`
    - Create a Prometheus datasource using the address above
