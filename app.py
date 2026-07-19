from flask import Flask, render_template, request

from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.get("/")
def get_insert_import():
    return render_template("insert_import.html")


@app.post("/sumbit_import")
def sumbit_import():
    money = request.form.get("money", "").strip()
    pass
