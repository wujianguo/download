#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import datetime
import logging
from statistics import Statistics


class MainPage(webapp2.RequestHandler):

    def get(self):
        pass
app = webapp2.WSGIApplication([('/.*', MainPage)],
                              debug=False)
