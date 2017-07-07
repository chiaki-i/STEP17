#!/usr/bin/env python
# coding:utf-8

import webapp2
import common

MAIN_PAGE_HTML = """\
<html>
  <head>
    <title>乗り換え案内</title>
    <link rel="stylesheet" type="text/css" href="/stylesheets/main.css" />
    <link rel="icon" type="image/x-icon" href="/img/favicon.ico" />
  </head>
  <body>
    <h1>東京近郊 乗り換え案内</h1>
    必ず出発駅と到着駅を指定してください。また、出発駅と到着駅に同じ駅は指定できません。
    <form action="/warp" method="post">
      <div class="input_pata">
        出発:
        <input type="text" name="from" rows="1" cols="60">駅
      </div>
      <div class="input_pata">
        到着:
        <input type="text" name="to" rows="1" cols="60">駅<br/>
        (霞ヶ関駅は、「霞ケ関」と入力してください)
      </div>
      <div class="input_pata">
        出発時間(現在は使えません):
        <input type="datetime-local" name="when" rows="1" cols="60" disabled="disabled">
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
      <img src="/img/gopher.png" width="200" alt="gopherくん" /><p class="result">
"""

RESULT_HTML2 = """\
      </p>
    </div>
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(MAIN_PAGE_HTML)

class Transfer(webapp2.RequestHandler):

    def post(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(RESULT_HTML1)
        station1 = (self.request.get('from')).encode('utf-8') # unicode文字列をstrに
        station2 = (self.request.get('to')).encode('utf-8')
        assert isinstance(station1, str)
        
        path = common.bf_search(station1, station2)
        result = common.result(path)
        # message = common.message(result)
        for item in result:
            self.response.write(item[0] + ' (' + item[1] + ') <br/>')
        self.response.write(RESULT_HTML2)


        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/warp', Transfer),
], debug=True)
