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

import os
import argparse
import urllib2
import time
import datetime
from datetime import datetime, timedelta

CAAML_DATE_FMT = "%Y-%m-%d"

def getdays(args):
    start = datetime.strptime(args.start, CAAML_DATE_FMT)
    for date in (start - timedelta(x) for x in range(args.days)):
        day = __getday(args, date.strftime(CAAML_DATE_FMT))
        if day:
            __writeday(args, day, date.strftime(CAAML_DATE_FMT))

def __getday(args, date):
    try:
        resp = urllib2.urlopen('%s?d=%s&r=%d' \
                               % (args.www, date, args.region))
    except IOError:
        return None

    return resp

def __writeday(args, day, date):
    file = open(os.path.join(args.odir, date+".xml"),'w')
    file.write(day.read())
    file.close()

if __name__=="__main__":

    parser = argparse.ArgumentParser(
        description='Pull CAAML data from a web server.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-d', '--days', type=int, default=1,
                        help='Number of days to recover from CAAML server')
    parser.add_argument('-s', '--start', default=time.strftime(CAAML_DATE_FMT),
                        help='Start date for CAAML data (work backwards from here)')
    parser.add_argument('-r', '--region', type=int, default=1,
                        help='The region to pull the data from')
    parser.add_argument('-l', '--log', default=None,
                        help='Logfile to record information')
    parser.add_argument('-o', '--odir', default='.',
                        help='Folder for the output data')
    parser.add_argument('-w', '--www',
                        default='http://avalanche.pc.gc.ca/CAAML-eng.aspx',
                        help='The region to pull the data from')
    args = parser.parse_args()

    getdays(args)

