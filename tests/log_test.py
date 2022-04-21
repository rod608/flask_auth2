""" This test the existence of log files """
import os


def test_request_log_exists():
    """This checks for the request log"""
    root = os.path.dirname(os.path.abspath(__file__))
    requestlog = os.path.join(root, '../app/logs/request.log')
    assert os.path.exists(requestlog) == True


def test_errors_log_exists():
    """This checks for the errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    errorlog = os.path.join(root, '../app/logs/errors.log')
    assert os.path.exists(errorlog) == True


def test_debug_log_exists():
    """This checks for the debug log"""
    root = os.path.dirname(os.path.abspath(__file__))
    debuglog = os.path.join(root, '../app/logs/debug.log')
    assert os.path.exists(debuglog) == True
