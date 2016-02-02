.. Fritz Speed documentation master file, created by
   sphinx-quickstart on Mon Feb  1 18:57:46 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Fritz Speed's documentation!
=======================================

What it does
------------

A small suite of `Python <https://www.python.org>`_ scripts to graph the
incoming and outgoing transfer speeds from a `Fritz!Box
<http://avm.de/produkte/fritzbox/>`_. It can be run on a small embedded device
such as a `RaspberryPi <https://www.raspberrypi.org>`_. It uses the `RRDtool
<https://oss.oetiker.ch/rrdtool>`_ bindings for python to output the graphs
suitable for embedding into a website.

The scripts can be run without superuser privileges as a normal user, he only
has to have the right file permissions to read and write to the round robin
archive and to write the images.

How It Works
------------

The `Fritz!Box <http://avm.de/produkte/fritzbox/>`_ does not provide a standard
SNMP interface common to most routers. Instead it relies on the `TR-064
standard <http://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/AVM_TR-064_overview.pdf>`_.

The script ``monitor-traffic.py`` uses this interface to retrieve the counters
for uploaded and downloaded bytes from the router and stores them in a round
robin archive based on RRDtool. A second script ``graph-traffic.py`` reads this
archive and generates graphs of the traffic for configured intervals of time.


Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   license


Disclaimer
----------

The product Fritz! and Fritz!Box is a trademark of the AVM GmbH, Berlin,
Germany.
