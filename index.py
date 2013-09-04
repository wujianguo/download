#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

PAGE = '''\
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html">
        <meta charset="utf-8">
        <title>download</title>
        <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
        <script type="text/javascript" src="https://www.dropbox.com/static/api/1/dropins.js" id="dropboxjs" data-app-key="ammgwdrjnxhzrie"></script>
        <script type="text/javascript">
function download()
{
    var url = document.getElementById("downloadurl").value
    Dropbox.save(url);
}
        </script>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="input-append">
                    <input class="span5 offset4 form-control" id="downloadurl" type="text">
                    <button class="btn btn-success" type="button" onclick="download()">download</button>
                </div>
                <div class="span3"></div>
            </div>
        </div>
    </body>
</html>'''
class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(PAGE)
app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=False)
