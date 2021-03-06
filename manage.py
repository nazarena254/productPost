from flask import Flask
from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand

# from app.models import User

# Use "python manage.py" for a list of available commands.
# Creating app instance
app = create_app('development')  # during development stage
#app = create_app('production')  # during production/deployment to heroku stage
# app = create_app('test')

#Manager class keeps track of all the commands  
# and handles how they are called from the command line
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
migrate.add_command('server',Server)

# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db=db)

if __name__ == '__main__':
    manager.run()
