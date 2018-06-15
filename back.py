#BAKER

from flask import Flask, Response

app = Flask(__name__)

f = open( "utils/key", 'r' )

app.secret_key = f.read();
f.close

@app.route("/")
def start() :
    if 'username' in session:
        return redirect("/puzzle")
    else:
        return render_template("homepage.html")

 #   response = open("homepage.html")
 #   return Response(response, mimetype='text/plain')

@app.route("/puzzle")
def crossword() :
     if 'username' not in session:
        return redirect("/")
    else:
        return render_template("board.html")



@app.route('/logout', methods=["POST", "GET"])
def logout():
    if "username" in session:
        session.pop('username')
    return redirect(url_for('/'))


