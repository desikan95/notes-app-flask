from app import app

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Welcome to notes applications"

from flask_restful import Resource, Api
from flask_restful import reqparse

api = Api(app)

NOTES = {
    'note1': {'task': 'build an API'},
    'note2': {'task': '?????'},
    'note3': {'task': 'profit!'},
}


def abort_if_note_doesnt_exist(id):
    if id not in NOTES:
        abort(404, message="note {} doesn't exist".format(id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# note
# shows a single note item and lets you delete a note item
class Note(Resource):
    def get(self, note_id):
        abort_if_note_doesnt_exist(note_id)
        return NOTES[note_id]

    def delete(self, note_id):
        abort_if_note_doesnt_exist(note_id)
        del NOTES[note_id]
        return '', 204

    def put(self, note_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        NOTES[note_id] = task
        return task, 201


# noteList
# shows a list of all notes, and lets you POST to add new tasks
class NoteList(Resource):
    def get(self):
        return NOTES

    def post(self):
        args = parser.parse_args()
        note_id = int(max(NOTES.keys()).lstrip('note')) + 1
        note_id = 'note%i' % note_id
        NOTES[note_id] = {'task': args['task']}
        return NOTES[note_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(NoteList, '/notes')
api.add_resource(Note, '/notes/<note_id>')
