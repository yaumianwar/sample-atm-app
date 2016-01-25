""" Configuration File """
import os

# Development (Debug -> True)
DEBUG =True
SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/task2'
SQLALCHEMY_TRACK_MODIFICATIONS = True
