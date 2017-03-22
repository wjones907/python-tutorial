import sys
import re
import time
import datetime
import urllib
import logging
from datetime import timedelta
#from datetime import time
import random

TIME_FORMAT =     '%Y-%m-%dT%H:%M:%S'
TIME_FORMAT_MS =  '%Y-%m-%dT%H:%M:%S.%f'
TIME_FORMAT_REF = '%Y-%m-%dT%H:%M:%S'
TIME_FORMAT_Z = '%Y-%m-%dT%H:%M:%SZ'


def Init():
    print
    print 'Initializing the system'


def Log_Formatter():
    print 'Entering Log Formatter'

def datetime_examples():
    print 'datetime.datetime', datetime.datetime
    #print 'datetime.datetime.time()', datetime.datetime.time()

    print "datetime.datetime.utcnow()" , datetime.datetime.utcnow()
    print 'datetime.datetime.now()', datetime.datetime.now()
    print "datetime.datetime.today()" , datetime.datetime.today()
    print 'datetime.time()', datetime.time()
    now = datetime.datetime.now()
    print "Today's date: ", now.strftime('%Y-%m-%d')

    mydate = datetime.datetime.utcnow()
    print 'mydate=',mydate
    #print 'datetime.utcnow().strftime(time_format)', datetime.datetime.utcnow().strftime())

    print datetime.datetime.utcnow()
    print (datetime.datetime.utcnow().strftime(TIME_FORMAT))

    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS))

    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_REF))

    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_Z))

    print 'start_time = ' + datetime.datetime.utcnow().strftime(TIME_FORMAT_Z)
    print '  end_time = ' + (datetime.datetime.utcnow() + datetime.timedelta(0, (60*5))).strftime(TIME_FORMAT_Z)

    print 'curr_time:', datetime.datetime.utcnow().strftime(TIME_FORMAT_Z)
    print 'curr_time + 30 min:', datetime.datetime.utcnow().strftime(TIME_FORMAT_Z) + 1000


def test_datetime_delta():
    print 'curr_time:', datetime.datetime.utcnow().strftime(TIME_FORMAT_Z)
    print 'curr_time + 30 min:', (datetime.datetime.utcnow() + 1000).strftime(TIME_FORMAT_Z)


def datetime_comparisons():
    from datetime import datetime

    date1 = datetime(2015, 03, 04)
    date2 = datetime(2015, 03, 03)
    date3 = datetime(2015, 03, 05)
    date4 = datetime(2015, 03, 03)

    print "Date 1: ", date1
    print "Date 2: ", date2
    print "Date 3: ", date3
    print "Date 4: ", date4

    if date1 < date3:
        print "date1 is greater than date3"

    if date1 > date2:
        print "date1 is greater than date2"

    if date2 == date4:
        print "date2 and date4 are equal"


def my_datetime_comparison():
    from datetime import datetime, timedelta
    import time

    curr_datetime = datetime.now()
    run_time = datetime.now()
    end_time = curr_datetime + timedelta(seconds=60)

    print
    print 'curr_datetime:', curr_datetime
    print '     run_time:', run_time
    print '     end_time:', end_time

    while run_time < end_time:
        print '------>'
        print '      run_time:', run_time
        print '     curr_time:', datetime.now()
        time.sleep(10)
        run_time = datetime.now()
    print
    print 'we\'re done at last run_time: , curr_time', run_time, datetime.now()
    print ''


def datetime_timedelta():
    from datetime import datetime, timedelta

    now = datetime.now()

    print "Today: ", now
    print "Yesterday: ", now - timedelta(days=1)
    print "Day before Yesterday: ", now - timedelta(days=2)

    print "Tomorrow: ", now + timedelta(days=1)
    print "Day after Tomorrow: ", now + timedelta(days=2)

    print "1 week ago: ", now - timedelta(weeks=1)
    print "1 week from now: ", now + timedelta(weeks=1)

    # Calculating a 15 day trial period
    trial_started = datetime.now()
    trial_ends = trial_started + timedelta(days=14)
    print "Started Trial on ", trial_started
    print "Trial Ends  ", trial_ends
    print "Trial Expires in  ", trial_ends - now


def datetime_timestamps():
    from datetime import datetime, timedelta
    import time

    current_timestamp = time.time()
    print "Timestamp: ", current_timestamp

    datetime_ts = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    print "Timestamp to datetime: ", datetime_ts

    date_ts = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d')
    print "Timestamp to date: ", date_ts

    # timestamp to datetime object in UTC
    date_utc = datetime.utcfromtimestamp(current_timestamp)
    print "Timestamp in UTC: ", date_tc


def datetime_YYYY_DD_MM_format():
    # using datetime module
    from datetime import datetime

    now = datetime.now()
    print "Today's date: ", now.strftime('%Y-%m-%d')

    # using the time module
    import time

    print time.strftime('%Y-%m-%d')


def datatime_current_datetime():
    from datetime import datetime

    now = datetime.now()
    print "Now: ", now
    print "Today's date: ", now.strftime('%Y-%m-%d')

    print "year:", now.year
    print "month:", now.month
    print "day:", now.day
    print "hour:", now.hour
    print "minute:", now.minute
    print "second:", now.second


def time_examples():
    print time
    print time.strftime('%Y-%m-%d')
    print 'time.time()', time.time()
    print 'time.time() * 1000', time.time() * 1000
    print 'int time.time()', int(time.time())
    print 'str time.time() * 1000', str(int(time.time())*1000)

def datetime_format():
    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS)) + str(random.random())
    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS)) + str(random.random())
    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS)) + str(random.random())
"""
=============
"""

#Init()

#Log_Formatter()

#Print_Time_Examples()

#time_format()

# test_time_delta()
#time_examples()
#datetime_timedelta()
#datetime_comparisons()
my_datetime_comparison()