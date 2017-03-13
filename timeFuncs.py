import sys
import re
import time
import datetime
import urllib
import logging
from datetime import timedelta
#from datetime import time

TIME_FORMAT =     '%Y-%m-%dT%H:%M:%S'
TIME_FORMAT_MS =  '%Y-%m-%dT%H:%M:%S.%f'
TIME_FORMAT_REF = '%Y-%m-%dT%H:%M:%S'
TIME_FORMAT_Z = '%Y-%m-%dT%H:%M:%SZ'

def Init():
    print
    print 'Initializing the system'

def Log_Formatter():
    print 'Entering Log Formatter'

def Print_Time_Examples():
    print ("datetime.datetime.utcnow()" , datetime.datetime.utcnow() )

    print ("datetime.datetime.today()" , datetime.datetime.today() )

    print ('datetime.datetime.now()', datetime.datetime.now())
    print ('datetime.time()', datetime.time())

    mydate = datetime.datetime.utcnow()
    print ('mydate=',mydate)

    print ('time.time()', int(time.time()))

    print ('time.time()', str(int(time.time())*1000))

    #print ('datetime.utcnow().strftime(time_format)', datetime.datetime.utcnow().strftime())

    print (datetime.datetime.utcnow().strftime(TIME_FORMAT))

    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS))

    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_REF))

    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_Z))

    print 'start_time = ' + datetime.datetime.utcnow().strftime(TIME_FORMAT_Z)
    print '  end_time = ' + (datetime.datetime.utcnow() + datetime.timedelta(0, (60*5))).strftime(TIME_FORMAT_Z)
import random
def time_format():
    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS)) + str(random.random())
    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS)) + str(random.random())
    print (datetime.datetime.utcnow().strftime(TIME_FORMAT_MS)) + str(random.random())
"""
=============
"""

#Init()

#Log_Formatter()

#Print_Time_Examples()

time_format()
