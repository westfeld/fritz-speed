#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
graph-traffic.py
"""

import os

import rrdtool

from common import read_configuration

def main():
    prefs = read_configuration('fritz-speed.ini')
    for g in prefs['graphs']:
        # graph the data for information about parameters see https://oss.oetiker.ch/rrdtool/doc/rrdgraph.en.html
        rrdtool.graph(g['filename'],
            "-t", g['title'],
            "-w", g['graph_width'],
            "-h", g['graph_height'],
            "-s", "end-"+g['interval']+"s",
            "DEF:bytes-up="+g['rra_filename']+":bytes-up:AVERAGE",
            "DEF:bytes-down="+g['rra_filename']+":bytes-down:AVERAGE",
            "LINE1:bytes-up#ff0000:Uploadrate",
            "LINE1:bytes-down#0000ff:Downloadrate",
            "-v", "Transfer rate [B/s]")

if __name__ == '__main__':
    main()
