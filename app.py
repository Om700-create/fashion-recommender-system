from flask import Flask, render_template
from fashion_recommendation_system.pipeline.pipeline import run_pipeline
from fashion_recommendation_system.utils.common import load_config

app = Flask(__name__)

@app.route('/')
def index():
    config = load_config('config/config.yaml')
    accuracy, report = run_pipeline(config)
    return render_template('index.html', accuracy=accuracy, report=report)

if __name__ == '__main__':
    app.run(debug=True)

