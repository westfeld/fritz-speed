#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
traffic-monitor.py
"""

import fritzconnection
import rrdtool

rrd_file = "/var/rrdtool/wan_traffic.rra"

def update_rra (*args):
    data = ":".join(args)
    rrdtool.update(rrd_file, "N:"+data)

def main():
    fc = fritzconnection.FritzConnection()
    status = fc.call_action('WANCommonInterfaceConfig', 'GetTotalBytesSent')
    bytes_up =  status['NewTotalBytesSent']

    status = fc.call_action('WANCommonInterfaceConfig', 'GetTotalBytesReceived')
    bytes_down =  status['NewTotalBytesReceived']
    update_rra(str(bytes_up), str(bytes_down))

if __name__ == '__main__':
    main()
