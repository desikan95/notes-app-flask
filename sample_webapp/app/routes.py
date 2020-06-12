from app import app

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Welcome to notes applications"

from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import jsonify, request
from .models import Notes
from . import db
import json

api = Api(app)

NOTES = {
   "notes":[
   {
      "id":1,
      "message":"The contents of note 1",
      "title":"Note 1"
   },
   {
      "id":2,
      "message":"The contents of note 2",
      "title":"Note 2"
   },
   {
      "id":3,
      "message":"The contents of note 3",
      "title":"Note 3"
   },
   {
      "id":4,
      "message":"The contents of note 4",
      "title":"Note 4"
   },
   {
      "id":5,
      "message":"The contents of note 5",
      "title":"Note 5"
   }]
}


def abort_if_note_doesnt_exist(id):
    if id not in NOTES:
        abort(404, message="note {} doesn't exist".format(id))

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('topic')
parser.add_argument('contents')


# note
# shows a single note item and lets you delete a note item
class Note(Resource):
    def get(self, note_id):
        note_result = Notes.query.get(note_id)
        print("Get/ID results")
        print("ID: ",note_result.id," Topic: ",note_result.topic," Contents:",note_result.contents)
        print("Note id in get request is ",note_id)
        result=[]
        # for key,val in NOTES.items():
        #     print(" Key is "+key)
        #     print(" Val is ")
        #     return val[int(note_id)-1]
        return json.dumps(note_result.serialize() )

    def delete(self, note_id):
        # abort_if_note_doesnt_exist(note_id)
        print("Received delete request for ",note_id)
        obj = Notes.query.filter_by(id=int(note_id)).one()
        db.session.delete(obj)
        db.session.commit()

        return 'Deleted', 204

    def put(self, note_id):
        args = parser.parse_args()
        print(" Received put request")
        return note_id, 201

    # def options (self):
    #     return {'Allow' : 'PUT' }, 200, \
    #     { 'Access-Control-Allow-Origin': '*', \
    #       'Access-Control-Allow-Methods' : 'PUT,GET,POST,DELETE' }


# noteList
# shows a list of all notes, and lets you POST to add new tasks
class NoteList(Resource):
    def get(self):
        note_db_results = Notes.query.all()
        return json.dumps(Notes.serialize_list(note_db_results))
        #return NOTES

    def post(self):
        args = parser.parse_args()
        print("Received post request",args)
        new_note = Notes(id=int(args['id']),topic=args['topic'], contents=args['contents'])
        print(" Object to be added : ", new_note)
        db.session.add(new_note)
        db.session.commit()
        return "HELLO", 201

    # def options (self):
    #     return {'Allow' : 'PUT' }, 200, \
    #     { 'Access-Control-Allow-Origin': '*', \
    #       'Access-Control-Allow-Methods' : 'PUT,GET,POST,DELETE' }

##
## Actually setup the Api resource routing here
##
api.add_resource(NoteList, '/notes')
api.add_resource(Note, '/notes/<note_id>')
