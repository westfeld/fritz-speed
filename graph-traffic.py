#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
graph-traffic.py
"""

import rrdtool
import os

# path to rra file generated with rrdtool where the data is stored
rrd_file = "/var/rrdtool/wan_traffic.rra"

# template for file name, placeholder will be substituted with suffix
# of individual graph
graph_file_template = "/var/www/t-base/htdocs/pics/traffic_{}.png"

# height of graph in pixels
graph_height = 300

# width of graph in pixels
graph_width = 400

# graph definition consisting of file name suffix and starting point
# start is given in seconds from the end of data recording
# e.g. start of 3600 means plot the last 3600 seconds (60 minutes = 1 hour)
graphs = [
            {
                'suffix' : '1d',
                'start' : 3600 * 24,
            },
            {
                'suffix' : '1w',
                'start' : 3600 * 24 * 7,
            },
            {
                'suffix' : '1m',
                'start' : 3600 * 24 * 30,
            },
        ]

def main():
    for g in graphs:
        graph_file = graph_file_template.format(g['suffix'])
        start = g['start']

        # graph the data for information about parameters see https://oss.oetiker.ch/rrdtool/doc/rrdgraph.en.html
        rrdtool.graph(graph_file,"-w", str(graph_width), "-h", str(graph_height), "-s", "end-"+str(start)+"s",
                "DEF:bytes-up="+rrd_file+":bytes-up:AVERAGE",
                "DEF:bytes-down="+rrd_file+":bytes-down:AVERAGE",
                "LINE1:bytes-up#ff0000:Uploadrate",
                "LINE1:bytes-down#0000ff:Downloadrate",
                "-v", "Transfer rate [B/s]")

if __name__ == '__main__':
    main()
