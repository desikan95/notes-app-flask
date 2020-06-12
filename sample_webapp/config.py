import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    POSTGRES = {
        'user': 'user',
        'pw': 'pass',
        'db': 'db',
        'host': 'pg_db',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    print(SQLALCHEMY_DATABASE_URI)
    print(" was the URI")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
