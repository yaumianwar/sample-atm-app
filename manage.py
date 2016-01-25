import os
from flask.ext.script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from app import app
from app.core.db import database

manager = Manager(app)
migrate = Migrate(app, database)

def _make_context():
    return {'app': app}

# Adding Shell Command
# python manage.py [arg]
manager.add_command('db', MigrateCommand)
manager.add_command('run', Server(host='0.0.0.0', port=9000))
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
