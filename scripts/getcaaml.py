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

import argparse
import urllib2
import time

def getday(args, date):
    resp = urllib2.urlopen('%s?d=%s&r=%d' \
                    % (args.www, date, args.region))
    print resp
    data = resp.read()
    resp.close()

    print data

if __name__=="__main__":

    parser = argparse.ArgumentParser(
        description='Pull CAAML data from a web server.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-d', '--days', type=int, default=1,
                        help='Number of days to recover from CAAML server')
    parser.add_argument('-s', '--start', default=time.strftime("%Y-%m-%d"),
                        help='Start date for CAAML data (work backwards from here)')
    parser.add_argument('-r', '--region', type=int, default=1,
                        help='The region to pull the data from')
    parser.add_argument('-w', '--www',
                        default='http://avalanche.pc.gc.ca/CAAML-eng.aspx',
                        help='The region to pull the data from')
    args = parser.parse_args()

    date = args.start
    getday(args, date)

