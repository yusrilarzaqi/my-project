from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import redirect
from functions.function import *

app = Flask(__name__)


@app.route("/")
def index():
    data = query(f"SELECT * FROM {table}")
    count = range(1, len(data) + 1)
    return render_template("index.html", data=data, count=count)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        nama = request.form["nama"]
        kelas = request.form["kelas"]
        email = request.form["email"]
        tambah(nama, kelas, email)
        return redirect("/")
    else:
        return render_template("add.html")


@app.route("/delete/<int:id>")
def delete(id):

    try:
        hapus(id)
        return redirect("/")
    except:
        return "something wrong"


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        id = request.form["id"]
        nama = request.form["nama"]
        kelas = request.form["kelas"]
        email = request.form["email"]
        ubah(id, nama, kelas, email)
        return redirect("/")
    else:
        data = query(f"SELECT * FROM {table} WHERE id={id}")
        return render_template("update.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
