from flask import Flask

app = Flask(__name__)

from views.home_views import home_views

app.register_blueprint(home_views)


if __name__ == '__main__':
    app.run(debug=True)