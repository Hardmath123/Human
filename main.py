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
import webapp2
import json

from google.appengine.ext import db

class Definition(db.Model):
	term = db.StringProperty()
	definition = db.TextProperty()

class APIHandler(webapp2.RequestHandler):
    def get(self):
    	q = db.Query(Definition)
    	q.filter("term =", self.request.get("term"))
    	x = []
    	for d in q.run():
    		x.append(d.definition)
        self.response.write(json.dumps(x))

class GenDef(webapp2.RequestHandler):
	def post(self):
		d = Definition()
		d.term = self.request.get("term")
		d.definition = self.request.get("definition")
		d.put()
		self.response.write("true")

app = webapp2.WSGIApplication([
    ('/api', APIHandler),
    ('/gen', GenDef)
], debug=True)
