from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


if __name__ == "__main__":
    app.run(port=8000)