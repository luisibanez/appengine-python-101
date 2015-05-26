
from google.appengine.api import users

import webapp2


class MainPage(webapp2.RequestHandler):

  def get(self):

      user = users.get_current_user()

      return_uri = '/'

      if user:
        greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                    (user.nickname(), users.create_logout_url(return_uri)))
      else:
        greeting = ('<a href="%s">Sign in or register</a>.' %
                    (users.create_login_url(return_uri)))

      self.response.set_status(200)
      self.response.headers['Content-Type'] = 'text/html; charset=utf-8'

      self.response.write('<html><body>%s</body></html>' % greeting)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
