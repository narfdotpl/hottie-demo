#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import, division

from hottie import hot


@hot
class DemoClass(object):

    def demo_method(self):
        print 'edit demo_method'


@hot
def demo_function():
    print 'edit demo_function'
