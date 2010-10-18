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
import os,cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from PowerModel import *

from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        characters=Character.all().order("name")
        template_values={"characters":characters}
        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        self.response.out.write(template.render(path, template_values))
        
class AddCharacter(webapp.RequestHandler):
	def post(self):
		name=cgi.escape(self.request.get('name'))
		level=long(cgi.escape(self.request.get('level')))
		character_class=cgi.escape(self.request.get('class'))
		id=cgi.escape(self.request.get('name')).lower().replace(" ","")
		chara = Character(name=name, level=level,character_class=character_class,id=id)
		chara.put()
		self.redirect('/')
		
class DeleteCharacter(webapp.RequestHandler):
	def get(self,chara):
		self.response.out.write("ciao %s" % chara)

def main():
    application = webapp.WSGIApplication([('/', MainHandler),
		('/add',AddCharacter),
		(r'/delete/(.*)',DeleteCharacter)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
