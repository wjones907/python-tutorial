import datetime
import time

def forloopex(ra):
    i=range(ra)
    print i
    for x in i:
        print x , "- iteration"



def ifstatementex():
#    x = int(raw_input("Please enter an integer: "))
    x=1

    if x < 0:
     x = 0
     print 'Negative changed to zero'
    elif x == 0:
        print 'Zero'
    elif x == 1:
        print 'Single'
    else:
        print 'More'

def whileloopex(n):    # write number out up to n
     a = 0
     while a <= n:
         print a,
         a = a + 1

def whileloopex2():
    status = 'PENDING'
    x=0
    while status not in ['COMPLETE','INCOMPLETE','FAILED']:
        print 'Recording not complete......'
        x+=1
        time.sleep(2)
        if x == 3:
            status = 'COMPLETE'

    print 'Recording completed with Status:',status


#forloopex(5)

#ifstatementex()

#whileloopex(5)

whileloopex2()

