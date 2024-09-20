SECRET_KEY = 'aprendendoflasksupermodulo'


SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        password='mengaocone10',
        server='localhost',
        database='times'
    )
