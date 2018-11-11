#!/usr/bin/python
# -*- coding: utf-8 -*-

# Filename: tornado_server.py
# Author: GuoJint
# Date:   2018-5-21
# Virsion: 1.0

"""
creat tornado server

"""

import os.path
import sys
sys.path.append("..")

import json
from tornado import httpserver
from tornado import ioloop
from tornado import web
from tornado.options import define, options
from tornado import websocket
import time

DEBUG = 1

define("port", default=8888, help="run on the given port", type=int)

class root(web.RequestHandler):
    """ root """
    def get(self):
        self.render("index.html")

class data_request(web.RequestHandler):
    """docstring for data_request"""
    def get(self):
        print("data_request get:", self.request)

    def post(self):
        # self.write("test")
        self.redirect("/")


def main():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }

    application = web.Application(
        [
            (r"/", root),
            (r"/data_request", data_request)
        ],
        # template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        )

    # server = httpserver.HTTPServer(application)
    application.listen(options.port)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()