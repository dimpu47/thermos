#! /usr/bin/env python

import os

from thermos import create_app, db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('THERMOS_ENV') or 'dev')
manager = Manager(app)


migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()




"""#! /usr/bin/env python

from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    gaurav = User(username="gaurav",email="dimpu47@gmail.com",
    password="123456")
    db.session.add(gaurav)

    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description,
        user=gaurav, tags=tags))

    for name in ["python","flask","webdev","programming","emacs", "go","golang","javascript","dev","angularjs","django","databases","orm","training"]:
        db.session.add(Tag(name=name))
    db.session.commit()

    add_bookmark("http://www.pluralsight.com", "Pluralsight. Hardcore developer training.","training,programming,python,flask,webdev")
    add_bookmark("http://www.python.org", "Python - my favorite language","python")
    add_bookmark("http://flask.pocoo.org", "Flask: Web development one drop at a time.", "python,flask,webdev")
    add_bookmark("http://www.reddit.com", "Reddit. Frontpage of the internet","news,coolstuff,fun")
    add_bookmark("http://www.sqlalchemyorg", "Nice ORM framework","python,orm,databases")
    add_bookmark("https://golang.org/doc/effective_go.html","Effective Go: The Go programming language","go,golang,programming,dev")
    add_bookmark("https://angularjs.org/", "AngularJS: The Superhoic javascript MVW framework","javascript,angularjs")
    add_bookmark("https://emacswiki.org/", "Wiki for my favorite editor","emacs")

    anonymous = User(username="anonymous", email="anonymous@example.com", password="qwert")
    db.session.add(anonymous)
    db.session.commit()


    print 'Database Initialized.'

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to loose all your data?"):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()
"""
