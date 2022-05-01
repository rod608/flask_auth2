import os
from io import BytesIO
from werkzeug.datastructures import FileStorage

from app import db
from app.auth.forms import *
from app.db.models import User, Song

from flask_login import FlaskLoginClient


def test_csv_upload_and_verification(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)

    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'

    with application.test_client(user=user) as client:
        # This request already has a user logged in.
        response = client.get('/songs/upload')
        assert response.status_code == 200

        # Checking to see that the form validates with music_csv.
        root = os.path.dirname(os.path.abspath(__file__))
        music_csv = os.path.join(root, '../sample_csv/music.csv')

        form = csv_upload()
        form.file = music_csv
        assert form.validate()
        assert db.session.query(Song).count() == 0
