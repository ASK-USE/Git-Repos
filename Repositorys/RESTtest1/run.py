# run.py

from app import create_app
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test_route():
    return "Hallo Testsubjekt"

app = create_app()

if __name__ == '__main__':
    app.run()