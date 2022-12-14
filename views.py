from flask import Blueprint, render_template

<<<<<<< HEAD
views = Blueprint( "views", __name__,)
=======
views = Blueprint(__name__, "views")
>>>>>>> 59eb81bf444082dd8049eb0dbc9abc5e8a5aadea


@views.route("/")
def home():
    return render_template("index.html")
<<<<<<< HEAD

    
=======
>>>>>>> 59eb81bf444082dd8049eb0dbc9abc5e8a5aadea
