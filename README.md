# 🚀 Flask CI/CD Project

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.1-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red?logo=jenkins)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5?logo=kubernetes)
![License](https://img.shields.io/badge/License-MIT-green)

A complete **Flask CI/CD project** demonstrating how to automate application testing, Docker image creation, Docker Hub publishing, and Kubernetes deployment using **Jenkins, Docker, and Minikube**.

The project is designed as a practical DevOps example showing how source code changes can automatically flow through a CI/CD pipeline and reach a running Kubernetes application.

---

## 📌 Project Overview

This project contains a lightweight Flask application with a complete CI/CD pipeline.

### 🔄 CI/CD Flow

```text
Developer
    │
    ▼
  GitHub
    │
    │ GitHub Webhook
    ▼
  Jenkins
    │
    ├── Checkout Code
    ├── Install Dependencies
    ├── Run Unit Tests
    ├── Build Application
    ├── Build Docker Image
    ├── Push Image to Docker Hub
    │
    ▼
 Docker Image
    │
    ▼
  Minikube
    │
    ├── Kubernetes Deployment
    ├── Kubernetes Service
    ├── Health Checks
    │
    ▼
 Flask Application
```

---

## 🛠️ Technology Stack

| Technology      | Purpose                      |
| --------------- | ---------------------------- |
| 🐍 Python 3.12  | Application runtime          |
| 🌶️ Flask 3.1.1 | Web application framework    |
| 🧪 Pytest       | Unit testing                 |
| 🦄 Gunicorn     | Production WSGI server       |
| 🐳 Docker       | Application containerization |
| 🔨 Jenkins      | CI/CD automation             |
| 📦 Docker Hub   | Container image registry     |
| ☸️ Kubernetes   | Container orchestration      |
| ⛵ Minikube      | Local Kubernetes cluster     |
| 🐙 GitHub       | Source code management       |

The repository currently pins Flask 3.1.1, Gunicorn 23.0.0, and Pytest 8.3.5.

---

## ✨ Features

* ✅ Flask-based web application
* ✅ REST API endpoints
* ✅ Application health check
* ✅ Application information endpoint
* ✅ Echo API for testing
* ✅ CI/CD pipeline using Jenkins
* ✅ Automated dependency installation
* ✅ Automated unit testing
* ✅ Docker image creation
* ✅ Docker Hub image publishing
* ✅ Kubernetes deployment
* ✅ Minikube integration
* ✅ Kubernetes readiness probe
* ✅ Kubernetes liveness probe
* ✅ Deployment rollout verification
* ✅ Automated application health verification

---

## 📁 Project Structure

```text
flask-cicd-project/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── .gitignore
│
├── tests/
│   └── test_app.py
│
└── kubernetes/
    └── deployment.yaml
```

The repository contains the Flask application, Dockerfile, Jenkins pipeline, test suite, and Kubernetes deployment configuration.

---

# 🌶️ Flask Application

The application is implemented in `app.py`.

It provides the following endpoints:

| Endpoint              | Description                             |
| --------------------- | --------------------------------------- |
| `/`                   | Flask CI/CD application home page       |
| `/api/health`         | Application health check                |
| `/api/info`           | Application and environment information |
| `/api/echo/<message>` | Echo API                                |
| `/api/pipeline`       | CI/CD pipeline information              |

### Example Health Check

```bash
curl http://localhost:5000/api/health
```

Expected response:

```json
{
  "status": "healthy",
  "service": "flask-cicd-app"
}
```

The application exposes the health endpoint specifically for Kubernetes probes and also provides pipeline information showing Jenkins, Docker Hub, and Kubernetes/Minikube as the deployment stack.

---

# 💻 Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/GitBhaveshKathore/flask-cicd-project.git
cd flask-cicd-project
```

## 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
python3 app.py
```

The application will start on:

```text
http://localhost:5000
```

---

# 🧪 Run Tests

The project uses **Pytest** for automated testing.

Run:

```bash
pytest tests/ -v
```

The test suite validates:

* Home endpoint
* Health endpoint
* Info endpoint
* Echo endpoint
* Pipeline endpoint

The repository's test file contains these endpoint-level tests.

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t flask-cicd-app:latest .
```

## Run Container

```bash
docker run -d \
  --name flask-cicd-app \
  -p 5000:5000 \
  flask-cicd-app:latest
```

Test the application:

```bash
curl http://localhost:5000/api/health
```

The Docker image uses Python 3.12 Alpine and runs the Flask application through Gunicorn with four workers.

---

# 🔨 Jenkins CI/CD Pipeline

The project uses a Jenkins Pipeline defined in `Jenkinsfile`.

### Pipeline Stages

```text
1. Checkout
       ↓
2. Install Dependencies
       ↓
3. Unit Tests
       ↓
4. Build
       ↓
5. Docker Build
       ↓
6. Push to Docker Hub
       ↓
7. Deploy to Minikube
       ↓
8. Verify Deployment
       ↓
9. AWS Prechecks
```

The Jenkins pipeline is triggered through a GitHub push webhook.

### Pipeline Details

#### 1️⃣ Checkout

Jenkins checks out the `main` branch from GitHub.

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Unit Tests

```bash
python3 -m pytest tests/ -v
```

#### 4️⃣ Build Validation

```bash
python3 -c "import app; print('Build OK')"
```

#### 5️⃣ Docker Build

Jenkins creates a Docker image using the Jenkins build number:

```text
kubebhavesh/flask-cicd-app:<BUILD_NUMBER>
```

and also tags the image as:

```text
kubebhavesh/flask-cicd-app:latest
```

#### 6️⃣ Push to Docker Hub

Jenkins securely authenticates to Docker Hub using Jenkins credentials and pushes both the build-number and `latest` tags.

#### 7️⃣ Deploy to Kubernetes

The Docker image is loaded into Minikube and the Kubernetes deployment is updated.

```bash
kubectl apply -f kubernetes/deployment.yaml
```

#### 8️⃣ Verify Deployment

Jenkins verifies:

```bash
kubectl get pods
kubectl get svc
```

and performs an application health check.

---

# ☸️ Kubernetes Deployment

The project uses Kubernetes to deploy the Flask application.

The deployment configuration contains:

* **2 replicas**
* Container port `5000`
* Readiness probe
* Liveness probe
* CPU and memory requests
* CPU and memory limits
* NodePort service

The Kubernetes service exposes port `80` and forwards traffic to container port `5000` through NodePort `30090`.

### Kubernetes Architecture

```text
                 Kubernetes / Minikube
                         │
                         ▼
              ┌─────────────────────┐
              │ Kubernetes Service  │
              │     NodePort        │
              │       :30090        │
              └──────────┬──────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       ┌─────────────┐       ┌─────────────┐
       │ Flask Pod 1 │       │ Flask Pod 2 │
       │    :5000    │       │    :5000    │
       └─────────────┘       └─────────────┘
```

---

# ⛵ Run on Minikube

Start Minikube:

```bash
minikube start
```

Apply the Kubernetes configuration:

```bash
kubectl apply -f kubernetes/deployment.yaml
```

Check the deployment:

```bash
kubectl get deployments
```

Check pods:

```bash
kubectl get pods
```

Check service:

```bash
kubectl get svc
```

Get the Minikube IP:

```bash
minikube ip
```

The application is exposed through NodePort:

```text
30090
```

You can also access it using:

```bash
minikube service flask-cicd-app-service --url
```

---

# ❤️ Kubernetes Health Checks

The application exposes:

```text
/api/health
```

which is used by Kubernetes for both readiness and liveness checks.

### Readiness Probe

```yaml
readinessProbe:
  httpGet:
    path: /api/health
    port: 5000
```

### Liveness Probe

```yaml
livenessProbe:
  httpGet:
    path: /api/health
    port: 5000
```

This allows Kubernetes to determine whether the application is ready to receive traffic and whether the application is still running correctly.

---

# 🔐 Jenkins Credentials

For Docker Hub authentication, create a Jenkins credential with the ID:

```text
dockerhub-creds
```

The pipeline expects:

```text
Username
Password / Access Token
```

⚠️ **Never hard-code Docker Hub passwords, API tokens, AWS credentials, or other secrets inside the repository.**

Use Jenkins Credentials or another secrets-management solution instead.

---

# 🔄 Complete CI/CD Workflow

A typical deployment looks like this:

```text
Developer pushes code
        │
        ▼
      GitHub
        │
        │ Webhook
        ▼
     Jenkins
        │
        ├── Checkout
        │
        ├── Install Dependencies
        │
        ├── Run Tests
        │
        ├── Build Application
        │
        ├── Build Docker Image
        │
        ├── Push to Docker Hub
        │
        ▼
    Docker Image
        │
        ▼
     Minikube
        │
        ├── Deployment
        │
        ├── 2 Flask Pods
        │
        └── NodePort Service
        │
        ▼
 Flask CI/CD Application
```

---

# 📡 API Examples

### Health

```bash
curl http://localhost:5000/api/health
```

### Application Information

```bash
curl http://localhost:5000/api/info
```

### Echo

```bash
curl http://localhost:5000/api/echo/hello
```

### Pipeline Information

```bash
curl http://localhost:5000/api/pipeline
```

---

# 🎯 Learning Objectives

This project demonstrates practical implementation of:

* Python Flask development
* REST API development
* Unit testing with Pytest
* Docker containerization
* Jenkins Pipeline
* CI/CD automation
* Docker Hub integration
* Kubernetes Deployment
* Kubernetes Services
* Kubernetes health probes
* Minikube
* Automated deployment verification
* GitHub webhook integration

---

# 🚀 Future Improvements

Possible enhancements for the project:

* [ ] Add SonarQube code-quality analysis
* [ ] Add Trivy container vulnerability scanning
* [ ] Add Kubernetes ConfigMaps
* [ ] Add Kubernetes Secrets
* [ ] Add Horizontal Pod Autoscaler
* [ ] Add Ingress
* [ ] Add HTTPS/TLS
* [ ] Add Prometheus monitoring
* [ ] Add Grafana dashboards
* [ ] Add centralized logging
* [ ] Add Slack/Teams Jenkins notifications
* [ ] Add production Kubernetes deployment
* [ ] Add automated rollback strategy
* [ ] Add separate Dev/QA/Production environments

---

# 👨‍💻 Author

**Bhavesh Suresh Kathore**

Automation / DevOps Engineer

### GitHub

[GitBhaveshKathore](https://github.com/GitBhaveshKathore)

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

**Repository:**
https://github.com/GitBhaveshKathore/flask-cicd-project

---

## 📄 License

This project is available under the MIT License.
