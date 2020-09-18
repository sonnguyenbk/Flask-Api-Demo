from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


from database.config import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url_connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from route.user_route import *
from route.post_route import *


if __name__ == "__main__":
    app.run(debug=True)
