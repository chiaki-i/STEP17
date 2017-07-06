#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

MAIN_PAGE_HTML = """\
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/stylesheets/main.css" />
    <link rel="icon" type="image/x-icon" href="/img/favicon.ico" />
  </head>
  <body>
    <form action="/warp" method="post">
      <div class="input_pata">
        出発:
        <input type="text" name="from" rows="1" cols="60">駅
      </div>
      <div class="input_pata">
        到着:
        <input type="text" name="to" rows="1" cols="60">駅
      </div>
      <div class="input_pata">
        出発時間(任意):
        <input type="datetime-local" name="when" rows="1" cols="60">
        <input type="submit" value="検索">
      </div>
    </form>
  </body>
</html>
"""

RESULT_HTML1 = """\
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/stylesheets/main.css" />
  </head>
  <body>
    <div>
      <img src="/img/gopher.png" width="200" alt="gopherくん" /><h1>
"""

RESULT_HTML2 = """\
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

class Transfer(webapp2.RequestHandler):

    def post(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(RESULT_HTML1)
        station1 = (self.request.get('from')).encode('utf-8') # unicode文字列をstrに
        station2 = (self.request.get('to')).encode('utf-8')
        assert isinstance(station1, str)
        
        result = self.search(station1, station2)
        for item in result:
            self.response.write(item)
        self.response.write(RESULT_HTML2)

    def search(self, station1, station2):
        f = open('networks/tokyo.txt', 'w')
        
        result = [station1, station2]
        if station1 == '荻窪':
            print(result)
        return result 
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/warp', Transfer),
], debug=True)
