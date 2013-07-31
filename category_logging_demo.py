#!/usr/bin/env python3.2

from logging import getLogger, StreamHandler, Formatter, CRITICAL, ERROR, WARNING, INFO, DEBUG

class my_class(object):
    def __init__(self, foo):
        l = getLogger('my_class')
        l.debug('my_class %s instantiated', foo)
        l.warn('my_class %s, %d exploding!!!' % (foo, 1))

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



root_logger = getLogger()
my_handler = StreamHandler()
my_formatter = Formatter('%(asctime)s %(name)s %(levelname)s %(filename)s:%(lineno)d: %(message)s')
my_handler.setFormatter(my_formatter)
root_logger.addHandler(my_handler)

# by default, I only want to see INFO and higher priority logging messages
root_logger.setLevel(INFO)

# my_class is really boring, so only see WARNING messages and higher
class_logger = getLogger('my_class')
class_logger.setLevel(WARNING)

# except for that interesting method.
interesting_logger = getLogger('my_class.my_interesting_method')
interesting_logger.setLevel(DEBUG)


my_function()

c = my_class('bar')
c.my_method()
c.my_interesting_method()
