Changelog
=========

Version 0.1.2
-------------

* add the possibility to change the graphing style (line or area and its color)
  directly from the configuration file.
* renamed the default configuration file so that changes to this file do not
  interfere with updates coming from the repo.
  
  *Pull request contributed by Olaf Peters (http://magicolf.de)*

Version 0.1.1
-------------

*  When creating a new rra for traffic data, the maximum line speed is queried
   from the router and used as a valid upper limit. This avoids spikes in the
   traffic graph originating from traffic counter resets on reconnects.

Version 0.1
-----------

Inital version
