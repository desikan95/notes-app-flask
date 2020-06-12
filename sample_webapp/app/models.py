from app import db
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)

class Notes(db.Model, Serializer):
    __tablename__ = 'notes'
    id = db.Column(db.Integer,primary_key=True)
    topic = db.Column(db.String(200))
    contents = db.Column(db.String(500))

    def serialize(self):
        d = Serializer.serialize(self)
        return d
