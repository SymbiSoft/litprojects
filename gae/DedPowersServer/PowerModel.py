from google.appengine.ext import db
import logging

class ActionType(db.Model):
    symbol = db.StringProperty(required=True)
    name = db.StringProperty(required=True)

class PowerType(db.Model):
    name = db.StringProperty()
    has_checkbox = db.BooleanProperty()
    
class Character(db.Model):
    name = db.StringProperty(required=True)
    character_class = db.StringProperty()
    id = db.StringProperty(required=False)
    level = db.IntegerProperty()
    user = db.UserProperty()
    
class Page(db.Model):
    order = db.IntegerProperty()
    name = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    title_text_color=db.StringProperty(default="black")
    title_background_color=db.StringProperty(default="white")
    text_color=db.StringProperty(default="black")
    text_background_color=db.StringProperty(default="white")
    character=db.ReferenceProperty(Character)

class Power(db.Model):
    name = db.StringProperty(required=True)
    page = db.ReferenceProperty(Page)
    level = db.IntegerProperty()
    power_type = db.ReferenceProperty(PowerType)
    action_type = db.ReferenceProperty(ActionType)
    is_utility = db.BooleanProperty()
    order = db.IntegerProperty()
    text = db.TextProperty()
    
class Content(db.Expando):
    title = db.StringProperty(required=True)
    template = db.StringProperty()
    
    def __init__(self, title, **kwds):
        _title=kwds.pop('title').lower().replace(" ","-")
        db.Expando.__init__(self,title=_title,**kwds)
    



    
    
