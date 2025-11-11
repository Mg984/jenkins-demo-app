from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Jenkins CI/CD Pipeline with SonarQube and AWS ECR!'

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'python-app'}), 200

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'Python Flask App',
        'version': '1.0.0',
        'deployed_via': 'Jenkins Pipeline'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

Click **"Commit changes"**

3. **Create `requirements.txt`**:

**Filename**: `requirements.txt`
```
flask==3.0.0
werkzeug==3.0.1
