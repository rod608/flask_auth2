import functools
import logging

from flask.testing import FlaskClient
from flask_login import login_user

from app import db, auth
from app.db.models import User, Song
import pytest
from faker import Faker


def test_adding_user(application):
    with application.app_context():
        user_count = db.session.query(User).count()
        song_count = db.session.query(Song).count()
        # showing how to add a record
        # create a record
        user = User('keith@webizly.com', 'testtest', True)
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        assert db.session.query(User).count() == user_count + 1
        # finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        # asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        # this is how you get a related record ready for insert
        user.songs = [Song("test", "smap", "1941", "rock"), Song("test2", "te", "1942", "rock")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == song_count + 2
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        # changing the title of the song
        song1.title = "SuperSongTitle"
        # saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='SuperSongTitle').first()
        assert song2.title == "SuperSongTitle"
        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == user_count
        assert db.session.query(Song).count() == song_count


# To-Do
def test_login(application, client):
    with client:
        user = User('keith@webizly.com', 'testtest', True)
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        db.session.commit()
        current_user = user

        # assert current_user is None
        # assert current_user.id is 5
        response = client.get("/login")
        assert response.status_code == 200
        print("Hi")


# To-Do
def test_registration(application):
    print("Hi")


# To-Do
def test_dashboard_access_logged_in(client):
    response = client.get("/dashboard")
    assert b"<h1>Redirecting...</h1>" in response.data


# Complete
def test_dashboard_access_logged_out(client):
    db.session.query(User).count() == 0
    with client:
        response = client.get("/dashboard")
        assert b"<h1>Redirecting...</h1>" in response.data


# To-Do
def test_deny_access_csv(client):
    with client:
        response = client.get("/songs")
        assert response.status_code == 200


# def test_dashboard_permissions(client, application):
#     with client:
#         client.post('/login', follow_redirects=True)
#         db.drop_all()
#         with application.app_context():
#             response = client.get("/dashboard")
#             assert response.status_code == 200

