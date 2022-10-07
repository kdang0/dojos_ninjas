from flask import redirect, render_template, request, session
from dojo_ninja_app import app
from dojo_ninja_app.model.dojo import Dojo


@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojo')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id" : id
    }

    return render_template("show_dojo.html", dojo = Dojo.get_dojo_w_ninjas(data))


@app.route('/dojo')
def index():
    dojos = Dojo.get_all()
    return render_template("home.html", dojos = dojos)


@app.route('/ninjas')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("add_ninja.html", dojos=dojos)

