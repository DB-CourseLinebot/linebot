from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migrate = Migrate()

from datetime import datetime, timedelta, date, time
from urllib.parse import parse_qsl
