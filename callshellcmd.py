import subprocess
from subprocess import call

def useCallFunc():
    print 'make call to call - lets see what kind of output we get'
    call (["ls","-lt"])
    print 'after the call to call'


def usePopenFunc():
    print subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()
    # Be aware that for all methods where you pass the final command to be executed by the shell as a string and you are responsible for escaping it.

def useSubprocessFunc():
    return_code = subprocess.call("echo Hello World", shell=True)
    print return_code

def useSubprocessFunc2():
    p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()

def useSubprocessFunc5():
    p = subprocess.Popen(['ls','-lt'], shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line,
    #retval = p.wait()


def useSubprocessFunc3():
    return_code = subprocess.call("ls", shell=True)
    print return_code

def useSubprocessFunc4():
    return_code = subprocess.call(["ls","-lt"], shell=True)
    print return_code

#usePopenFunc()
#useCallFunc()
#useSubprocessFunc()
useSubprocessFunc4()