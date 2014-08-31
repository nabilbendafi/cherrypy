import random
import re
import string

import cherrypy

def is64bits(string=''):
    return re.match(r'x86_64', string)

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        some_string = ''
        if cherrypy.serving.request.headers.has_key('User-Agent'):
            some_string = cherrypy.serving.request.headers['User-Agent']
            print(some_string)
        return "Hello world!\nAre you running on 64bits ? %s" % ('Yes' if is64bits(some_string) else 'No')

if __name__ == '__main__':
   cherrypy.config.update("myapp.config")
   cherrypy.quickstart(HelloWorld())
