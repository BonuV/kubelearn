from flask import Flask
import os
import sys

app = Flask(__name__)
msg = None

@app.route("/")
def hello():
    return msg


if __name__ == "__main__":
    msg = sys.argv[1]
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)