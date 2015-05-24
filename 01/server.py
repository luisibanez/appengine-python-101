
import webapp2


class MainPage(webapp2.RequestHandler):

  def get(self):

      self.response.set_status(200)
      self.response.headers['Content-Type'] = 'text/html; charset=utf-8'

      self.response.out.write('Hello World')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
