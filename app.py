from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="10.200.14.26",
        user="talhaa",
        password="Fotball2008",
        database="lab"
    )

@app.route("/")  # Øvelse 11 – forside
def forside():
    return render_template("forside.html")



@app.route("/bruker/<navn>")  # Øvelse 12 – route med parameter
def bruker(navn):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT brukernavn FROM brukere WHERE brukernavn = %s", (navn,))
    resultat = cursor.fetchone()
    conn.close()
    if resultat:
        navn = resultat["brukernavn"]
    else:
        navn = None
    return render_template("bruker.html", navn=navn)


@app.route("/brukere")  # Øvelse 20 – hent data fra databasen og vis på nettsiden
def brukere():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT brukernavn FROM brukere")
    alle = cursor.fetchall()
    conn.close()
    return render_template("brukere.html", brukere=alle)  # Øvelse 15 – send variabel til template


@app.route("/registrer", methods=["GET", "POST"]) 
def registrer():
    melding = None
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]  # Øvelse 14 – hent data fra skjema
        passord = request.form["passord"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO brukere (brukernavn, password_hash) VALUES (%s, %s)",
                       (brukernavn, passord))  # Øvelse 21 – lagre skjemadata til databasen
        conn.commit()  
        conn.close()
        melding = f"Bruker '{brukernavn}' ble registrert!"
    return render_template("registrer.html", melding=melding)


if __name__ == "__main__":
    app.run(debug=True)