from flask import Flask, request
import datetime
import os

app = Flask(_name_)

@app.route("/ehome", methods=["POST"])
def ehome():
    try:
        data = request.json
    except:
        data = {"error": "No se recibió JSON"}
    print("Evento recibido:", data)
    with open("eventos.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
    return {"status": "ok"}, 200

@app.route("/")
def home():
    try:
        with open("eventos.txt") as f:
            logs = f.read()
    except:
        logs = "No hay eventos aún."
    return f"<pre>{logs}</pre>"

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)