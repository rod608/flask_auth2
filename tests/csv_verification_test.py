import logging

import os
from app import db
from app.db.models import User, Song
from app.songs import songs_upload
from faker import Faker


def song_csv_upload(application):
    print("hi")


def test_csv_verification(application):
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

        ''' Testing CSV Upload '''
        # Step 1: Get the csv path as a var
        root = os.path.dirname(os.path.abspath(__file__))
        music_csv = os.path.join(root, '../sample_csv/music.csv')
        assert os.path.exists(music_csv)

        # Step 2: Upload a CSV as the current user

        # Step 3: Make use of songs_upload() function

        ''' End: We're done so cascade delete on user ; we don't need him anymore '''
        db.session.delete(user)
        assert db.session.query(User).count() == user_original_count
        assert db.session.query(Song).count() == song_original_count
