from . import app,db
from datetime import datetime

class Words(db.Document):
    name = db.StringField(required=True,max_length=30)
    content = db.StringField(max_length=100)
    time = db.DateTimeField(default = datetime.now())
