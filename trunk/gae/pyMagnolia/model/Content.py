import logging
from google.appengine.ext import db

class Content(db.Expando):
    name = db.StringProperty(required=True)
    template = db.StringProperty()

    def __init__(self, name, **kwds):
        logging.debug(kwds)
        _name=name.lower().replace(" ","-")
        db.Expando.__init__(self,name=_name,**kwds)
