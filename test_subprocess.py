

from subprocess import Popen, PIPE
from pprint import pprint

def my_test_popen():
    proc = Popen(['ls', '-lt'], stdout=PIPE, stderr=PIPE, bufsize=1)
    #stdout, stderr = proc.communicate()
    #pprint(stdout)
    #print 'size of stdout:', len(stdout)

    #with process.stdout:
    #    for line in iter(process.stdout.readline, 'b'):
    #        print line

    #for line in iter(proc.stdout.readline, ''):
    #    print 'len(line)', len(line)

    #for line in proc.stderr:
    #    print(line.decode().rstrip())

    '''

    for line in stderr:
        print(line.rstrip())
    '''

def my_test_popen1():
    # works - nothing prints out
    proc = Popen(['ls', '-lt'], stdout=PIPE, stderr=PIPE, bufsize=1)

def my_test_popen1_3():
    # does not work - prints each char on a separate line
    proc = Popen(['ls', '-lt'], stdout=PIPE, stderr=PIPE, bufsize=1)
    stdout, stderr = proc.communicate()

    for line in stdout:
        #print(line.decode().rstrip())      # prints each character on a separate line
        print line                       # prints each character on a separate line

def my_test_popen1_1():
    # works - nothing prints out - i expected the contents of ls to print out
    proc = Popen(['ls', '-lt'])  # , stdout=PIPE, stderr=PIPE, bufsize=1


def my_test_popen1_2():
    # works - prints out stdout
    proc = Popen(['ls', '-lt'], stdout=PIPE, stderr=PIPE, bufsize=1)

    for line in proc.stdout:
        #print(line.rstrip())    # strips whitespace at the end of the string
        #print line              # prints out with extra blank line after each line
        print(line.decode().rstrip())   # prints output line by line - decode used for encoding


def my_test_popen2():
    # works - prints only retcode: 0
    process = Popen(['ls', '-lt'], stdout=PIPE, stderr=PIPE,bufsize=1)
    retcode = process.wait()
    #pprint(stdout)
    print 'retcode:', retcode
    #print 'size of stdout:', len(process.stdout)


def my_test_popen3():
    # works - displays stdout directly to the screen
    process = Popen(['ls', '-lt'])  # , stdout=PIPE, stderr=PIPE,bufsize=1
    retcode = process.wait()
    #pprint(stdout)
    print 'retcode:', retcode
    #print 'size of stdout:', len(process.stdout)

def examp_popen4():
    # did not work - prints output to stdout - AttributeError on decode()
    import subprocess
    import sys

    proc = subprocess.Popen(['ls'], stderr=sys.stdout, shell=True)  # Not the use of sys.stdout
    out, err = proc.communicate()
    print(err.decode("utf-8"))


def examp_popen5():
    # works - prints output after popen call: err is blank unless there's an error - not exactly sure what decode() does - works ok without it
    import subprocess
    import sys

    proc = subprocess.Popen(['ls'], stderr=PIPE, stdout=PIPE, shell=True)  # Not the use of sys.stdout
    out, err = proc.communicate()
    print(err.decode("utf-8"))
    print(out.decode("utf-8"))

def examp_popen6():
    # works - but prints each letter of the file on a separate line
    import subprocess
    import sys

    proc = subprocess.Popen(['ls', "fileio.py"], stderr=PIPE, stdout=PIPE, shell=True)  # Not the use of sys.stdout
    out, err = proc.communicate()
    #print(err.decode("utf-8"))
    #print(out.decode("utf-8"))
    print 'len(out)', len(out)
    for line in out:
        #print(line.decode().rstrip())
        print(line)
        #print 'len(line)', len(line)

def examp_popen7():
        # works - but prints each letter of the file on a separate line
        import subprocess
        import sys

        proc = subprocess.Popen(['ls', 'fileio.py'], stderr=PIPE, stdout=PIPE, shell=True)  # Not the use of sys.stdout
        out, err = proc.communicate()
        # print(err.decode("utf-8"))
        # print(out.decode("utf-8"))
        for line in out:
            print(line.decode().rstrip())
            #print(line)


def examp_popen8():
    # works - prints each file on a separate line
    import subprocess
    import sys

    proc = subprocess.Popen(['ls', '*.md'], stderr=PIPE, stdout=PIPE)  # , use shell=True when using a single cmd string with all params included - ie. 'ls -lt'
    #out, err = proc.communicate()
    # print(err.decode("utf-8"))
    # print(out.decode("utf-8"))
    # print 'len(proc.stdout)', len(proc.stdout)
    for line in proc.stdout:
        print(line.decode().rstrip())
        # print(line)

def simple_playback1_4():
    # works - but adds a separate blank line after each line - also prints out stderr as <open file '<fdopen>'
    import subprocess
    return_code = 0
    vle_final_statistics = ""
    process_status = subprocess.Popen(["ls", "*.md"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
    # Parse the VLE output from stdout and obtain the summarised final statistics information
    with process_status.stdout:
        for line in iter(process_status.stdout.readline, b''):
            print line
            #if VLE_STATISTICS_FIRST_LINE in line:
            #    vle_final_statistics = ""
            #vle_final_statistics += line
    process_status.wait()
    return_code = process_status.returncode
    print 'return code:',return_code
    #print 'vle_final_statistics: size in bytes:', len(vle_final_statistics)
    #print 'last line in stats.log:',line
    print 'stderr:',process_status.stderr
    #print vle_final_statistics


my_test_popen1_3()
#examp_popen8()
#simple_playback1_4()

