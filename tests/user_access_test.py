from flask import session
from app.auth.forms import *


def test_login_validates(application, client):
    """ Tests login w/ proper credentials. """
    form = login_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "jimmy1941"
    assert form.validate()


def test_login_not_validates(application, client):
    """ Tests login w/ improper credentials. No password. """
    form = login_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "12345"
    assert not form.validate()


def test_register_validates(application, client):
    """ Tests register w/ proper credentials. """
    form = register_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "jimmy1941"
    form.confirm.data = "jimmy1941"
    assert form.validate()


def test_register_not_validates(application, client):
    """ Tests register w/ improper credentials. Passwords don't match. """
    form = register_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "jimmy1941"
    form.confirm.data = "jimmy1942"
    assert not form.validate()
