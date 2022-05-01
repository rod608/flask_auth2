import logging
import os

from werkzeug.datastructures import FileStorage

from app import db
from app.db.models import User, Song
from io import BytesIO
from app.auth.forms import *


def test_populate_from_files(application, client, auth):
    @application.route("/songs", methods=["POST"])
    def index():
        form = csv_upload()
        # print(form.file.data)
        # assert form.file.data is not None
        print(type(form.file.data))
        return 'Ok'

    auth.login()
    root = os.path.dirname(os.path.abspath(__file__))
    music_csv = os.path.join(root, '../sample_csv/music.csv')
    assert os.path.exists(music_csv)

    index()
    client.post("/songs", data={"file": (BytesIO(), music_csv)})


def test_csv_upload(auth, client):
    auth.login()

    data = {
        'field': 'value',
        'file': (BytesIO(b'FILE CONTENT'), 'test.csv')
    }

    rv = client.post('/songs', buffered=True,
                     content_type='multipart/form-data',
                     data=data)
    # assert rv.status_code == 400


def test_csv_verification(application, client):
    with application.app_context():
        ''' Adding a user to perform these tests on. '''
        # Step 1: Placeholder for current num of users and songs
        user_original_count = db.session.query(User).count()
        song_original_count = db.session.query(Song).count()

        # Step 2: Adding a test user to db
        user = User('keith@webizly.com', 'testtest', True)
        db.session.add(user)
        db.session.commit()

        # Step 3: Add some songs for the test user
        user.songs = [Song("test", "smap", "1941", "rock"), Song("test2", "te", "1942", "rock")]
        db.session.commit()

        ''' Testing CSV Upload - keep songs_upload() in mind '''
        # Step 1: Get the path of the csv we're uploading as a variable
        root = os.path.dirname(os.path.abspath(__file__))
        music_csv = os.path.join(root, '../sample_csv/music.csv')
        assert os.path.exists(music_csv)

        # Step 2: Upload a CSV as the current user
        # data = {}
        # response = client.post('/songs/upload')

        # Step 3: Make sure the uploaded CSV appears in uploads folder

        #
        # response = client.get('/songs/upload')
        # assert b'Submit' in response.data

        # Checking CSV file upload: Either the log or a new csv entry in uploads

        # Checking CSV file processed:

        ''' End: We're done so cascade delete on user ; we don't need him anymore '''
        db.session.delete(user)
        assert db.session.query(User).count() == user_original_count
        assert db.session.query(Song).count() == song_original_count
