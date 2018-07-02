#BAKER

from flask import Flask, Response, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

f = open( "key", 'r' )

app.secret_key = f.read();
f.close

@app.route("/")
def start() :
    if 'username' in session:
        return redirect("/puzzle")
    else:
        return render_template("homepage.html")

@app.route("/")
def loginOrRegister():
    if 'username' in session:
        return redirect("/puzzle")
    else:
        return render_template("homepage.html")

@app.route("/authOrCreate", methods=["POST"])
def authOrCreate():
    formDict = request.form
    if formDict["logOrReg"] == "login":
        username = formDict["username"]
        password = formDict["password"]
        loginStatus = "login failed"
        statusNum = accountManager.authenticate(username,password) #returns 0,1 or 2 for login status messate
        if statusNum == 0:
            loginStatus = "user does not exist"
        elif statusNum == 1:
            session["username"]=username
            loginStatus = username + " logged in"
            return render_template("board.html")
        elif statusNum == 2:
            loginStatus = "wrong password"
        return render_template("homepage.html") #,status=loginStatus)

    elif formDict["logOrReg"] == "register":
        username = formDict["username"]
        password = formDict["password"]
        pwd = formDict["pwd"]  #confirm password
        registerStatus = "register failed"
        statusNum = accountManager.register(username,password,pwd) #returns true or false
        if statusNum == 0:
            registerStatus = "username taken"
        elif statusNum == 1:
            registerStatus = "passwords do not match"
        elif statusNum == 2:
            registerStatus = username +" account created"
        elif statusNum == 3:
            registerStatus = "password too short"
        elif statusNum == 4:
            registerStatus = "username left blank"
        return redirect("/") #render_template("homepage.html") #,status = registerStatus) #status is the login/creation messate
    else:
        return redirect(url_for("loginOrRegister"))


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


if __name__ == "__main__":
    app.debug = True
    app.run()


