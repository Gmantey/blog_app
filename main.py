import os
import click
from flask_migrate import Migrate
from blog_app.models import Members, Post, Admins
from blog_app import db, create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


#Shell context processor function for database
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Members=Members, Post=Post, Admins=Admins)









