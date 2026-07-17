from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask CI/CD Pipeline",
        "version": "1.0.0",
        "timestamp": str(datetime.datetime.now())
    })

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy", "service": "flask-cicd-app"})

@app.route("/api/info")
def info():
    return jsonify({
        "app": "Flask CI/CD Demo",
        "author": "Vijay Chowdary",
        "environment": os.environ.get("FLASK_ENV", "production"),
        "python_version": os.sys.version
    })

@app.route("/api/echo/<message>")
def echo(message):
    return jsonify({"echo": message, "timestamp": str(datetime.datetime.now())})

@app.route("/api/pipeline")
def pipeline():
    return jsonify({
        "pipeline": "Jenkins CI/CD",
        "registry": "DockerHub",
        "orchestrator": "Kubernetes (Minikube)",
        "stages": ["Checkout", "Test", "Build", "Docker Build", "Push", "Deploy"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
