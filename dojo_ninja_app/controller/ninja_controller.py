from flask import redirect, request, session, render_template
from dojo_ninja_app import app
from dojo_ninja_app.model.ninja import Ninja
from dojo_ninja_app.model.dojo import Dojo


@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("add_ninja.html", dojos=dojos)

@app.route('/show_ninjas')
def show_ninjas():
    return render_template("show_dojo.html", ninjas=Ninja.get_all())