Installation
============

Prerequisites
-------------

Fritz Speed is working on a standard Python 2.7 environment and relies on the
following packages for querying the Fritz!Box.

* `fritzconnection <https://pypi.python.org/pypi/fritzconnection/0.4.6>`_
* `lxml <https://pypi.python.org/pypi/lxml/3.5.0>`_
* `requests <https://pypi.python.org/pypi/requests/2.9.1>`_

For storing the data in a round robin database it uses the python bindings to
RRDtool.

* `python-rrdtool <https://pypi.python.org/pypi/python-rrdtool/1.4.7>`_


To get the scripts you need `Git <https://git-scm.com/>`_ to clone the
repository using the URL ``https://github.com/westfeld/fritz-speed.git``

Installation on a RaspberryPi Running Raspian
---------------------------------------------


1. Downloading the Scripts
--------------------------

To install the Fritz Speed scripts clone the GitHub repository::

    git clone https://github.com/westfeld/fritz-speed.git

2. Installing the Dependencies
------------------------------

There are many ways to install the dependencies but for the common packages we
rely on aptitude::

    aptitude install python-rrdtool python-requests python-lxml python-pip

The fritzconnection package is not in the raspbian repository so it will be
installed using pip by running::

    pip install fritzconnection

3. Configuration
----------------

Configuration basically means setting the location of the round robin archive
(rra) file in which the data is stored. In addition the properties and location
of the individual graphs have to be defined.

The first step is to copy the example configuration file ``fritz-speed.ini.example``
to ``fritz-speed.ini`` to enable further updates easily.

Starting from the default ``fritz-speed.ini`` file typically only two variables
have to be edited: ``rra_filename`` which defines the round robin archive
filename in which the traffic data is stored and ``graph_basedir`` which is the
output directory under which all graph files will be stored.

.. note::
   The user under which both the ``monitor-traffic.py`` and ``graph-traffic.py``
   scripts are executed has to have read/write permissions to the
   ``rra_filename`` and the ``graph_basedir`` directory.

An example of a typical ``fritz-speed.ini`` file is shown here::

    [DEFAULT]
    rra_filename: /var/rrdtool/wan_traffic.rra
    graph_height: 300
    graph_width: 500
    graph_basedir: /var/www/htdocs/pics
    # graph type for up/downstream: LINEx (where x = line width), AREA
    # more information about plotting
    # https://oss.oetiker.ch/rrdtool/doc/rrdgraph_graph.en.html
    graph_type_up: LINE1
    graph_type_down: LINE1
    # graph color for up/downstream in RGB from 00 to FF in 000000 format
    graph_color_up: ff0000
    graph_color_down: 0000ff

    # definitions of graphs to be plotted
    # each section corresponds to one graph
    [day]
    # interval in seconds to be plotted
    interval: 86400
    # title of plot
    title: Traffic of last day
    # filename of plot
    filename: %(graph_basedir)s/traffic_1d.png

    [week]
    # interval in seconds to be plotted
    interval: 604800
    # title of plot
    title: Traffic of last week
    # filename of plot
    filename: %(graph_basedir)s/traffic_1w.png

    [month]
    # interval in seconds to be plotted
    interval: 2592000
    # title of plot
    title: Traffic of last month
    # filename of plot
    filename: %(graph_basedir)s/traffic_1m.png

4. Create Round Robin Archive
-----------------------------

To create the empty archive simply run the following script::

  ./create-rra.py

During this setup step the maximum up- and downlink speed is queried from the
router and set as the maximum valid value in the archive (an error margin of 10%
is added to the determined value). This setting is important because if the
router's transferred bytes counter is reset this would otherwise lead to a spike
in the traffic graph.

5. Running as a Cronjob
-----------------------

To monitor the traffic on the Fritz!Box the ``monitor-traffic.py`` script is
executed periodically, which then reads the traffic counter on the router and
stores the value in the round robin archive.

To generate the graphs from the stored data the script ``graph-traffic.py`` is
executed. It would also update already existing images.

Typically one would add the following line to the user's crontab to record the
data and update the graphs every minute. To do so the command ``crontab -e``
opens the user's crontab and the following line is added ::

  */1 * * * * [absolute path to script]/monitor-traffic.py && [absolute path to script]/graph-traffic.py


