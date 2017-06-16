
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'hello world!'

port = int(os.getenv('PORT', 8080))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
