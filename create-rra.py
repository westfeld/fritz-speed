#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
create-rra.py

creates RRD file with 60 seconds primary step length
four datasources which are counters
three RRA for one day, one week and one mont
"""

import rrdtool
import os

from common import read_configuration

def main():
    rrdtool.create(prefs['rra_filename'], '--step', '60',
        'DS:bytes-up:COUNTER:500:0:'+prefs['max_transferrate'],
        'DS:bytes-down:COUNTER:500:0:'+prefs['max_transferrate'],
        'RRA:AVERAGE:0.8:1:1440',
        'RRA:AVERAGE:0.8:10:1008',
        'RRA:AVERAGE:0.8:60:5040' )

if __name__ == '__main__':
    prefs = read_configuration('fritz-speed.ini')
    main()
