#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
traffic-monitor.py

querys the Fritz!Box via the TR-064 interface and writes traffic counters
into round robin archive (RRA).
"""

import fritzconnection
import rrdtool

from common import read_configuration

def update_rra (rra_filename, *args):
    data = ":".join(args)
    rrdtool.update(rra_filename, "N:"+data)

def main():
    fc = fritzconnection.FritzConnection()
    status = fc.call_action('WANCommonInterfaceConfig', 'GetTotalBytesSent')
    bytes_up =  status['NewTotalBytesSent']

    status = fc.call_action('WANCommonInterfaceConfig', 'GetTotalBytesReceived')
    bytes_down =  status['NewTotalBytesReceived']
    update_rra(prefs['rra_filename'], str(bytes_up), str(bytes_down))

if __name__ == '__main__':
    prefs = read_configuration('fritz-speed.ini')
    main()
