from flask import Flask, render_template_string
from datetime import datetime
import socket
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GCP DevOps Demo</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .container {
            background: rgba(255, 255, 255, 0.12);
            padding: 40px;
            border-radius: 18px;
            backdrop-filter: blur(10px);
            text-align: center;
            width: 500px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
        }

        h1 {
            margin-bottom: 10px;
            font-size: 38px;
        }

        p {
            font-size: 18px;
            margin: 10px 0;
        }

        .info {
            margin-top: 25px;
            background: rgba(255,255,255,0.15);
            padding: 15px;
            border-radius: 12px;
        }

        .footer {
            margin-top: 25px;
            font-size: 14px;
            opacity: 0.8;
        }

        .badge {
            display: inline-block;
            padding: 8px 18px;
            background: #00c853;
            border-radius: 25px;
            margin-top: 15px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 GCP DevOps Demo</h1>
        <p>Python Flask Application</p>

        <div class="badge">
            Successfully Deployed with GitHub Actions
        </div>

        <div class="info">
            <p><strong>Hostname:</strong> {{ hostname }}</p>
            <p><strong>Environment:</strong> {{ environment }}</p>
            <p><strong>Time:</strong> {{ current_time }}</p>
        </div>

        <div class="footer">
            Powered by Docker • GitHub Actions • GCP
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=socket.gethostname(),
        environment=os.getenv("ENVIRONMENT", "Production"),
        current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
