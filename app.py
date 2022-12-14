from flask import Flask
<<<<<<< HEAD
from .views import views
=======
from views import views
>>>>>>> 59eb81bf444082dd8049eb0dbc9abc5e8a5aadea

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

<<<<<<< HEAD
app.register_blueprint(views, url_prefix="/views")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

=======
   
if __name__ == '__main__':
    app.run(debug=True, port=5000)


>>>>>>> 59eb81bf444082dd8049eb0dbc9abc5e8a5aadea
