#BAKER

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def start() :

    response = open("homepage.html")
    return Response(response, mimetype='text/plain')



