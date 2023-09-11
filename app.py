from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template("modele.jinja", message="non")


if __name__ == "__main__":
    app.run()