from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

# Modern HTML/CSS Template for the Home Page
HOME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask CI/CD Pipeline</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.08);
            text-align: center;
            max-width: 600px;
            width: 90%;
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.1em;
            color: #7f8c8d;
        }
        .version {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 6px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            margin-top: 15px;
        }
        .endpoints {
            margin-top: 35px;
            text-align: left;
            background: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
        }
        .endpoints strong {
            display: block;
            margin-bottom: 15px;
            color: #2c3e50;
        }
        .endpoints a {
            color: #2980b9;
            text-decoration: none;
            display: block;
            margin: 10px 0;
            font-weight: 500;
            transition: color 0.2s;
        }
        .endpoints a:hover {
            color: #1abc9c;
            text-decoration: underline;
        }
        .timestamp {
            margin-top: 30px;
            font-size: 0.85em;
            color: #95a5a6;
            border-top: 1px solid #eee;
            padding-top: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Flask CI/CD Pipeline</h1>
        <p>Your continuous integration and deployment setup is running successfully!</p>
        <div class="version">Version 1.0.0</div>
        
        <div class="endpoints">
            <strong>Available API Endpoints:</strong>
            <a href="/api/health">✅ /api/health (Kubernetes Probes)</a>
            <a href="/api/info">ℹ️ /api/info (App Information)</a>
            <a href="/api/pipeline">⚙️ /api/pipeline (Pipeline Configuration)</a>
            <a href="/api/echo/hello">🗣️ /api/echo/&lt;message&gt; (Echo Test)</a>
        </div>

        <div class="timestamp">Live Server Time: {{ timestamp }}</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    # Inject the live timestamp into the HTML template
    current_time = str(datetime.datetime.now())
    return HOME_HTML.replace("{{ timestamp }}", current_time)

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy", "service": "flask-cicd-app"})

@app.route("/api/info")
def info():
    return jsonify({
        "app": "Flask CI/CD Demo",
        "author": "Bhavesh Suresh Kathore",
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