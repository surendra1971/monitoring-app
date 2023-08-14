import psutil
from flask import Flask

app = Flask(__name__ , static_folder='../static')

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return ("CPU utilization: {cpu_metric} and Menory utilization: {mem_metric}")

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')