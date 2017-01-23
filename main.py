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
import webapp2, random

def get_lucky():
    return str(random.randrange(1,101))

def get_fortune():
    fortune_list = ["You are going to have a good day",
    "Tonight you will eat tasty foods",
    "Please eat fewer cookies"]
    return random.choice(fortune_list)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        lucky_number = '<p>Your lucky number is: <strong>' + get_lucky() + '<strong></p>'
        fortune = "<p>Your fortune is : <strong>" + get_fortune() + "</strong></p>"
        cookie_button = """<a href="."><button>Try another cookie</button></a>"""
        self.response.write(header + fortune + lucky_number + cookie_button)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
