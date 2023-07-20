from flask import Flask
from app.views import home_views, ayudante_views

app = Flask(__name__)
app.register_blueprint(home_views)
app.register_blueprint(ayudante_views)

if __name__ == '__main__':
    app.run(debug=True)