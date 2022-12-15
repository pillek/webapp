from flask import Flask, render_template, request
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/views")

app = Flask(name)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/', methods=["GET", 'POST'])
def inputTask():
   task = request.form["nm"]
   return render_template('index.html'), 



# @app.route('/', methods=["GET", 'POST'])
# def showTask():
#       task = request.args.get('nm')
#       return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

