#!/usr/bin/env python

import webapp2
from google.appengine.ext import db


class Comment(db.Model):
	content = db.StringProperty(multiline = True)
	
class  MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write('<html><body><h1>DataStore Tutorial</h1>')
		self.response.write(""" Enter your comment:
		<form method ="post">
		<input type= "textarea" name="post"></input>
		<input type= "submit"></input>
		</form>""")
		self.response.write('</body></html>')
		
	def post(self):
		self.response.write('<html><body><h1> Datastore Tutorial</h1>')
		self.comment = Comment(content = self.request.get('post'))
		self.comment.put()
		self.response.write('<p> You entered: </p><p>%s</p>' % self.request.get('post'))
		self.response.write('</body></html>')
		self.redirect('/')

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)


