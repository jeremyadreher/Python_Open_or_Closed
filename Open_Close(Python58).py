import sys, os, time
from datetime import datetime, timedelta
import pytz
from pytz import timezone

def getDatetime():
    HQ = '{:%H}'.format(datetime.now(timezone('US/Pacific')))
    NYC = '{:%H}'.format(datetime.now(timezone('US/Eastern')))
    LON = '{:%H}'.format(datetime.now(timezone('Europe/London')))

    check_time(HQ, NYC, LON)

def check_time(HQ, NYC, LON):
    print 'Portland: {}\nNew York: {}\nLondon: {}'.format(HQ, NYC, LON)

    if int(HQ) >=9 and int(HQ) <=21:
        print 'The Portland HQ is open'
    else:
        print 'The Portland HQ is closed'

    if int(NYC) >=9 and int(NYC) <=21:
        print 'The New York City office is open'
    else:
        print 'The New York City office is closed'

    if int(LON) >=9 and int(LON) <=21:
        print 'The London office is open'
    else:
        print 'The London office is closed'

if __name__ == "__main__":
    getDatetime()




