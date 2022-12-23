from flask import Flask, render_template, redirect, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    name = request.cookies.get("name")
    if name is None:
        return redirect("/login")
    return render_template("cookie.html", name=name)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        response = make_response(render_template("cookie.html", name=name))
        response.set_cookie("name", name)
        return response
    return render_template("cookie_login.html")


@app.route("/logout")
def logout():
    response = make_response(render_template("cookie_login.html"))
    response.set_cookie("name", expires=0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
