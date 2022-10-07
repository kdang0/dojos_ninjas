from flask import redirect, request, session, render_template
from dojo_ninja_app import app
from dojo_ninja_app.model.ninja import Ninja



@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojo')
