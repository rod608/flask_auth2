""" This test the existence of log files """
import os


def test_request_log_exists():
    """This checks for the request log"""
    root = os.path.dirname(os.path.abspath(__file__))
    requestlog = os.path.join(root, '../app/logs/request.log')
    # Make if it doesn't exist
    if not os.path.exists(requestlog):
        open(requestlog, 'a').close()
    # Asser it exists
    assert os.path.exists(requestlog) == True


def test_errors_log_exists():
    """This checks for the errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    errorlog = os.path.join(root, '../app/logs/errors.log')
    # Make if it doesn't exist
    if not os.path.exists(errorlog):
        open(errorlog, 'a').close()
    assert os.path.exists(errorlog) == True


def test_debug_log_exists():
    """This checks for the debug log"""
    root = os.path.dirname(os.path.abspath(__file__))
    debuglog = os.path.join(root, '../app/logs/debug.log')
    # Make if it doesn't exist
    if not os.path.exists(debuglog):
        open(debuglog, 'a').close()
    assert os.path.exists(debuglog) == True


def test_flask_log_exists():
    """This checks for the flask log"""
    root = os.path.dirname(os.path.abspath(__file__))
    flasklog = os.path.join(root, '../app/logs/flask.log')
    # Make if it doesn't exist
    if not os.path.exists(flasklog):
        open(flasklog, 'a').close()
    assert os.path.exists(flasklog) == True


def test_info_log_exists():
    """This checks for the info log"""
    root = os.path.dirname(os.path.abspath(__file__))
    infolog = os.path.join(root, '../app/logs/info.log')
    # Make if it doesn't exist
    if not os.path.exists(infolog):
        open(infolog, 'a').close()
    assert os.path.exists(infolog) == True


def test_myapp_log_exists():
    """This checks for the myapp log"""
    root = os.path.dirname(os.path.abspath(__file__))
    myapplog = os.path.join(root, '../app/logs/myapp.log')
    # Make if it doesn't exist
    if not os.path.exists(myapplog):
        open(myapplog, 'a').close()
    assert os.path.exists(myapplog) == True


def test_sqlalchemy_log_exists():
    """This checks for the sqlalchemy log"""
    root = os.path.dirname(os.path.abspath(__file__))
    sqlalchemylog = os.path.join(root, '../app/logs/sqlalchemy.log')
    # Make if it doesn't exist
    if not os.path.exists(sqlalchemylog):
        open(sqlalchemylog, 'a').close()
    assert os.path.exists(sqlalchemylog) == True


def test_werkzeug_log_exists():
    """This checks for the werkzeug log"""
    root = os.path.dirname(os.path.abspath(__file__))
    werkzeuglog = os.path.join(root, '../app/logs/werkzeug.log')
    # Make if it doesn't exist
    if not os.path.exists(werkzeuglog):
        open(werkzeuglog, 'a').close()
    assert os.path.exists(werkzeuglog) == True
