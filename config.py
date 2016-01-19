""" Configuration File """
import os

# Development (Debug -> True)
DEBUG =True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/task2'
SQLALCHEMY_TRACK_MODIFICATIONS = True