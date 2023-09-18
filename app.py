from flask import Flask, render_template


app = Flask(__name__)

class Objet:
    def __init__(self, titre, description, photo, categorie):
        self.titre = titre
        self.description = description
        self.photo = photo
        self.categorie = categorie

@app.route("/")
def bonjour():
    return render_template("Main.jinja", pagePrincipale=True)

if __name__ == "__main__":
    app.run()