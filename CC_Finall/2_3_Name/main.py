import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        response_text = ""
        for _ in range(5):
            response_text+="Name<br>"
            response_text+="Roll number<br>"
            response_text+="IT<br>"
            response_text+="<br>"

        self.response.write(response_text)



app = webapp2.WSGIApplication([("/", MainPage)])
