#!/usr/bin/env python
#
# getcaaml.py
#
# A simple script to pull CAAML data from the avalanche.ca
# website. Note their pho engine is of the form d=<date> and
# r=<region>. Date form supports at least YYYY-MM-DD format. Banff is
# region 1.
#
# Note that right now we just get the data and put each day into a
# file. We will process this data down the road.

import urllib2

def getday(date, region):
    print date
    resp = urllib2.urlopen('http://avalanche.pc.gc.ca/CAAML-eng.aspx?d=%s&r=%d' \
                    % (date, region))
    print resp
    data = resp.read()
    resp.close()

    print data

if __name__=="__main__":
    print "Hello"
    getday("2017-03-21", 1)
