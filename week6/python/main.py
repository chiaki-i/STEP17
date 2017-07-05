#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

MAIN_PAGE_HTML = """\
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/stylesheets/main.css" />
  </head>
  <body>
    <form action="/pata" method="post">
      <div class="input_pata">
        input1:
        <input type="text" name="content1" rows="1" cols="60">
      </div>
      <div class="input_pata">
        input2:
        <input type="text" name="content2" rows="1" cols="60">
        <input type="submit" value="submit">
      </div>
    </form>
  </body>
</html>
"""

GUEST_BOOK_HTML1 = """\
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/stylesheets/main.css" />
  </head>
  <body>
    <img src="/img/gopher.png" width="200" alt="gopherくん" />
    <div class="relative">
      <img src="./img/fukidashi4.png" alt="" />
      <p class="absolute"><h1> 
"""

GUEST_BOOK_HTML2 = """\
      </h1></p>
    </div>
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write('hello!')
        self.response.write(MAIN_PAGE_HTML)

class Pata(webapp2.RequestHandler):

    def post(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(GUEST_BOOK_HTML1)
        patoca = self.request.get('content1')
        taxi   = self.request.get('content2')
        s = "".join(i+j for i, j in zip(patoca, taxi))
        self.response.write(s)
        self.response.write(GUEST_BOOK_HTML2)
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/pata', Pata),
], debug=True)
