#!/usr/bin/env python3.2

from logging import getLogger
from logging.config import fileConfig
from time import sleep

class my_class(object):
    def __init__(self):
        l = getLogger('my_class')
        l.debug('my_class instantiated')

    def my_method(self):
        l = getLogger('my_class.my_method')
        l.debug('debug output in my_method')
        l.info('info input in my_method')

    def my_interesting_method(self):
        l = getLogger('my_class.my_interesting_method')
        l.debug('debug output in my_interesting_method')
        l.info('info input in my_interesting_method')


def my_function():
    l = getLogger('my_function')
    l.debug('debug output in my_function')
    l.info('info output in my_function')

while 1:
    fileConfig('logging_config.ini')

    my_function()

    c = my_class()
    c.my_method()
    c.my_interesting_method()
    sleep(1.0)
