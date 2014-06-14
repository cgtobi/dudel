from raven.contrib.flask import Sentry
from flask import Flask
from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.markdown import Markdown
from flask.ext.login import LoginManager, current_user
from flask.ext.gravatar import Gravatar
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

app = Flask(__name__)
app.config.from_pyfile("../config.py.example", silent=True)
app.config.from_pyfile("../config.py", silent=True)
manager = Manager(app)
db = SQLAlchemy(app)
markdown = Markdown(app, safe_mode="escape")
login_manager = LoginManager(app)
sentry = Sentry(app)
gravatar = Gravatar(app, size=48, rating='g', default='identicon', force_default=False, use_ssl=False, base_url=None)
babel = Babel(app)
supported_languages = ['en', 'de']
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

from dudel.util import load_icons
ICONS = load_icons("dudel/icons.txt")

import dudel.models
import dudel.forms
import dudel.filters
import dudel.views
import dudel.admin

login_manager.login_view = "login"
