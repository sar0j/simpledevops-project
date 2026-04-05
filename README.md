# Simple DevOps Project — Kubernetes 🚀

A full-stack DevOps project demonstrating Kubernetes orchestration with monitoring.

## Architecture
GitHub Push → GitHub Actions → Docker Hub → Kubernetes Cluster
├── Flask App (Deployment)
├── PostgreSQL (StatefulSet)
├── Ingress (Nginx)
└── Prometheus + Grafana

## Tech Stack
- **App:** Python Flask + PostgreSQL
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Orchestration:** Kubernetes
- **Package Manager:** Helm
- **Monitoring:** Prometheus + Grafana
- **Ingress:** Nginx

## Features
- ✅ Kubernetes deployment with 2 replicas
- ✅ PostgreSQL with persistent storage
- ✅ Helm chart for easy deployment
- ✅ Nginx Ingress controller
- ✅ ConfigMaps and Secrets management
- ✅ Prometheus metrics collection
- ✅ Grafana dashboards
- ✅ Rolling updates and rollbacks

## Project Structure
simpledevops-project/
├── app/                    # Flask application
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── k8s/                    # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── postgres-pv.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-service.yaml
│   └── postgres-statefulset.yaml
├── helm/                   # Helm charts
│   └── devopsapp1-chart/
└── .github/
└── workflows/
└── ci.yml

## Quick Start

### Deploy with Helm
```bash
helm install devopsapp1 ./helm/devopsapp1-chart
```

### Deploy with kubectl
```bash
kubectl apply -f k8s/
```

### Access the app
```bash
minikube tunnel
curl http://devopsapp1.local
```

## Monitoring
```bash
# Install Prometheus + Grafana
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace

# Access Grafana
kubectl port-forward --namespace monitoring svc/monitoring-grafana 3000:80
```

Open `http://localhost:3000` with username `admin`.

## API Endpoints
| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Home page |
| `/users` | GET | Get all users |
| `/adduser/<name>` | GET | Add a user |
| `/metrics` | GET | Prometheus metrics |