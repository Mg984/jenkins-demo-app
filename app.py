from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Jenkins CI/CD Pipeline with AWS ECR!'

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'python-flask-app'}), 200

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'Python Flask Application',
        'version': '1.0.0',
        'deployed_via': 'Jenkins CI/CD Pipeline',
        'container_registry': 'AWS ECR'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
