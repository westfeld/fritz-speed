#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
graph-traffic.py
"""

import os

import rrdtool

from common import read_configuration

def main():
    prefs = read_configuration(os.path.join(os.path.dirname(__file__),'fritz-speed.ini'))
    for g in prefs['graphs']:
        # graph the data for information about parameters see https://oss.oetiker.ch/rrdtool/doc/rrdgraph.en.html
        rrdtool.graph(g['filename'],
            "-t", g['title'],
            "-w", g['graph_width'],
            "-h", g['graph_height'],
            "-s", "end-"+g['interval']+"s",
            "DEF:bytes-up="+g['rra_filename']+":bytes-up:AVERAGE",
            "DEF:bytes-down="+g['rra_filename']+":bytes-down:AVERAGE",
            prefs['graph_type_down']+":bytes-down#0000ff:Downloadrate",
            prefs['graph_type_up']+":bytes-up#ff0000:Uploadrate",
            "-v", "Transfer rate [B/s]")

if __name__ == '__main__':
    main()
