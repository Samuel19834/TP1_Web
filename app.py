from flask import Flask, render_template
import bd


app = Flask(__name__)

class Objet:
    def __init__(self, titre, description, photo, categorie):
        self.titre = titre
        self.description = description
        self.photo = photo
        self.categorie = categorie

@app.route("/")
def bonjour():
    objets = []

    objets.append(Objet("Tigre", "Jésus Marie Joseph de batèche de sacristi de bout d'ciarge de saint-ciboire de sacrament de mosus de cul de viande à chien de charogne de colon de gériboire de boswell d'esprit de marde de câline de bine.", "templateImage.jpeg", 4))
    objets.append(Objet("Deuxième Tigre", "Sapristi d'ostifie de cibouleau de sainte-viarge de batince de saint-cimonaque de saint-ciboire de tabarnouche.", "templateImage.jpeg", 5))
    objets.append(Objet("Wow, un autre tigre", "Crucifix de tabarslaque de cibole de calvince de baptême de saint-sacrament de ciboire de charrue.", "templateImage.jpeg", 3))
    objets.append(Objet("Deuxième Tigre", "Sapristi d'ostifie de cibouleau de sainte-viarge de batince de saint-cimonaque de saint-ciboire de tabarnouche.", "templateImage.jpeg", 5))

    return render_template("base.jinja", titre="Accueil", objets=objets)


if __name__ == "__main__":
    bd.creer_connexion()
    app.run()