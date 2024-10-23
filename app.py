from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import random
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Example endpoint to simulate requests
@app.route('/')
def hello():
    return "Hello, World!"

# Example metric to simulate request count
@app.route('/request')
def request():
    # Simulate some processing
    time.sleep(random.uniform(0.1, 0.5))  # Simulate variable request time
    return "Request processed!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

