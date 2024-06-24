from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calcul_montant(dollar: int, taux: int) -> int | float:
    return dollar * taux


@app.route("/", methods=["GET", "POST"])
def home():
    dollar = 5
    franc_bu = 6100
    taux = 6100
    montant_converti: int | float = 0
    if request.method == "POST" and request.form:
        try:
            dollar = int(request.form.get("dollar"))
            taux = int(request.form.get("taux"))
            montant_converti = calcul_montant(dollar, taux)
        except ValueError as error:
            return jsonify("Données invalide"), 400

    data = {
        "dollar": dollar,
        "franc_bu": franc_bu,
        "taux": taux,
        "montant_converti": montant_converti,
    }
    return render_template("index.html", data=data)
