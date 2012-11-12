#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import, division
from time import sleep

from hottie import smartreload

from demo import DemoClass, demo_function


def _main():
    dc = DemoClass()

    while True:
        dc.demo_method()
        demo_function()

        smartreload()
        sleep(0.5)

if __name__ == '__main__':
    _main()
