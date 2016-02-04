#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
create-rra.py

creates RRD file with 60 seconds primary step length
four datasources which are counters
three RRA for one day, one week and one mont
"""

import fritzconnection
import rrdtool
import os

from common import read_configuration

def get_link_speed():
    fc = fritzconnection.FritzConnection()
    status = fc.call_action('WANCommonInterfaceConfig', 'GetCommonLinkProperties')
    downstream = status['NewLayer1DownstreamMaxBitRate'] / 8.
    upstream = status['NewLayer1UpstreamMaxBitRate'] / 8.
    return (upstream, downstream)

def main():
    link_speeds = get_link_speed()
    max_speeds = tuple([speed*1.1 for speed in link_speeds])
    rrdtool.create(prefs['rra_filename'], '--step', '60',
        'DS:bytes-up:COUNTER:500:0:'+str(max_speeds[0]),
        'DS:bytes-down:COUNTER:500:0:'+str(max_speeds[1]),
        'RRA:AVERAGE:0.8:1:1440',
        'RRA:AVERAGE:0.8:10:1008',
        'RRA:AVERAGE:0.8:60:5040' )

if __name__ == '__main__':
    prefs = read_configuration('fritz-speed.ini')
    main()
