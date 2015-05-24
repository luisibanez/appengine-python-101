
from google.appengine.api import users

import webapp2


class MainPage(webapp2.RequestHandler):

  def get(self):

      self.response.set_status(200)
      self.response.headers['Content-Type'] = 'text/html; charset=utf-8'

      if users.get_current_user():
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
      else:
        url = users.create_login_url(self.request.uri)
        url_linktext = 'Login'


      self.response.out.write('Hello World')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
