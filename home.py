__author__ = 'Leon'
#coding:utf-8

import web
from web.contrib.template import render_mako

import hashlib
import urls

render = render_mako(
    directories=['templates'],
    input_encoding='utf-8',
    output_encoding='utf-8',
)

class home():
    def GET(self):
    #render画面对象
        return render.home()

    def POST(self):
        pass