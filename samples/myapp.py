import random
import re
import string

import cherrypy

def is64bits(user_agent=''):
    """
    :param: user_agent string

    :return True if user_agent is 64 bits
    """
    ua = ['x86_64', 'x86-64', 'Win64', 'x64;', 'amd64', 'AMD64', 'WOW64', 'x64_64']
    if re.match('|'.join(ua), user_agent):
        return True
    return False

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
