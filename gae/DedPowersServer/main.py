#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os,cgi,sys
import pdb
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import logging

from PowerModel import *

from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        logging.debug("main handler (index.html)")
        characters=Character.all().order("name")
        template_values={"characters":characters}
        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        name=cgi.escape(self.request.get('name'))
        level=long(cgi.escape(self.request.get('level')))
        character_class=cgi.escape(self.request.get('class'))
        id=cgi.escape(self.request.get('name')).lower().replace(" ","")
        chara = Character(parent=None,key_name=id,id=id,name=name, level=level,character_class=character_class)
        chara.put()
        self.redirect('/')

class DeleteCharacter(webapp.RequestHandler):
    def get(self,id):
        chara=Character.all().filter("id =",id)
        if not chara and chara=='all':
            chara=Character.all()
        for c in chara:
            c.delete()
        self.redirect('/?chara='+id)

class ViewCharacter(webapp.RequestHandler):
    def get(self,chara):
        logging.debug("View character %s " % (chara))
        chara=DB_utils.get_chara(chara)
        path = os.path.join(os.path.dirname(__file__), 'template/view-character.html')
        self.response.out.write(template.render(path, {"chara":chara}))
        
    def post(self,chara):
        chara=DB_utils.get_chara(chara)
        name=cgi.escape(self.request.get('pageName'))
        page=Page(name=name.lower().replace(" ",""),character=chara,title=name)
        page.put()
        self.redirect(self.request.path)
        
class ViewPage(webapp.RequestHandler):
    def get(self,chara,page):
        logging.debug("View page %s %s" % (chara,page))
        chara=DB_utils.get_chara(chara)
        page=DB_utils.get_page(page)
        path = os.path.join(os.path.dirname(__file__), 'template/view-page.html')
        self.response.out.write(template.render(path, {"chara":chara,"page":page}))

class DB_utils:
    @staticmethod
    def get_chara(chara_id):
        return Character.gql("WHERE id = :1",chara_id).get()
    @staticmethod
    def get_page(page):
        return Page.gql("WHERE name = :1",page).get()

class Test(webapp.RequestHandler):
    def get(self):
        home=Content(title="cCiica asfaDaf",template="view-page.html")
        home.put()
        chara=Content(title="sven-laargston",template="chara.html",chara_name="Sven Laargston",parent=home)
        chara.put()
        chara2=Content(title="sven-laarg2s2ton",template="chara.html",chara_name="Sv2e2n 2L2aargston",parent=home)
        chara2.put()
        logging.warn(chara.parent().title)
        q = db.Query()
        q.ancestor(home)
        logging.warn(q.count())
        for c in q.fetch(limit=5):
            logging.warn(c.title)

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = webapp.WSGIApplication([('/', MainHandler),
        (r'/delete/(.*)',DeleteCharacter),
        (r'/chara/([^/]*)',ViewCharacter),
        (r'/chara/([^/]*)/([^/]*)',ViewPage),
        (r'/test',Test)],
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
