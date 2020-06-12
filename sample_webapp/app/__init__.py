from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

app = Flask(__name__)
app.config.from_object(Config)
logging.getLogger('flask_cors').level = logging.DEBUG
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = "Content-Type"


#CORS(app, origins="http://127.0.0.1:4500", allow_headers=[
#    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
#    supports_credentials=True)

# POSTGRES = {
#     'user': 'user',
#     'pw': 'pass',
#     'db': 'db',
#     'host': 'pg_db',
#     'port': '5432',
# }
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port='5002')

print("Hello, Desddikan")
db.create_all()

from app import routes, models
from .models import Notes

# sample_note = Notes(id=2,topic="sample_topic_2", contents="sample_contents_2")
# print(" Going to add : ")
# print(sample_note)
# db.session.add(sample_note)
db.session.commit()
