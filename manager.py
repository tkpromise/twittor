from flask_script import Manager
from flask_migrate import MigrateCommand

from twittor import create_app, db
from twittor.models import User, Tweet

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Tweet=Tweet)

if __name__ == "__main__":
    manager.run()
