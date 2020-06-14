import os
import tempfile
from app import app
import json
import pytest


@pytest.fixture(scope='module')
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.test_client() as client:
        response = c.get('/notes')
        print("RESPONSE is ",response)

def test_getNotes():
     client = app.test_client()
     response = client.get('/notes')
     print(response)
     assert response.status_code==200

def test_getNote():
     client = app.test_client()
     response = client.get('/notes/1')
     print(response)
     assert response.status_code==200

def test_postNotes():
    client = app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'id': 131,
        'topic': 'test topic',
        'contents': 'test contents'
    }
    url = '/notes'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.content_type == mimetype
    assert response.status_code==201

def test_putNotes():
    client = app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'id': 131,
        'topic': 'test topic_edited',
        'contents': 'test contents'
    }
    url = '/notes/131'

    response = client.put(url, data=json.dumps(data), headers=headers)

    assert response.content_type == mimetype
    assert response.status_code==201

def test_delNotes():
    client = app.test_client()
    response = client.delete('/notes/131')

    assert response.status_code==204
