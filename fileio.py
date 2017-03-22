#from __future__ import print_function  # Only needed for Python 2


import time
import os

CONFIG_DIR = None


def fileio_1():
    # If you choose to go with print(..., file=f) you will probably find that you'll want to suppress the newline from
    # time to time, or replace it with something else. This can be done by setting the optional end parameter, e.g.;
    with open("test", 'w') as f:
        #print('Foo1,', file=f, end='')
        #print('Foo2,', file=f, end='')
        #print('Foo3', file=f)
        print

def fileio_2():
    f = open('myfile', 'w')
    f.write('hi there\n')  # python will convert \n to os.linesep
    f.close()  # you can omit in most cases as the destructor will call it


def fileio_3():
    print("hi there")


def fileio_4():
    with open('file_to_write', 'w') as f:
       f.write('file contents')


def fileio_5():
    x = 0
    output_file = 'mytestfile.txt'
    with open(output_file, 'a') as f:
        while x < 4:
            load = 'file content:' + str(x) + '\n'
            print 'write contents to file:', load
            f.write(load)
            time.sleep(.5)
            x += 1

def file_func_6():
    # When you said Line it means some serialized characters which are ended to '\n' characters. Line should be last at
    # some point so we should consider '\n' at the end of each line. Here is solution:
    # in append mode after each write the cursor move to new line, if you want to use 'w' mode you should add '\n'
    # characters at the end of write() function:
    # the_file.write('Hello'+'\n')
    with open('YOURFILE.txt', 'a') as the_file:
        the_file.write('Hello')

def fileio_func_7():
    file = open('testfile.txt', 'w')

    file.write('HelloWorld')
    file.write('This is our new text file')
    file.write(' and this is anotherline.')
    file.write('Why? Because we can.')

    file.close()

def fileio_func_8():
    file = open("textfile.txt","w")
    print 
   



def get_base_dir_path():
    """
    Gets the absolute path to the base directory of the test framework so that the same can be used to access all
    directories like conf\, tests\, etc.

    :return the absolute path to the base directory of the test framework
    """
    this_file_path = os.path.abspath(__file__)
    helpers_dir = os.path.dirname(this_file_path)

    print 'this_file_path:',this_file_path
    print 'helpers_dir:',helpers_dir
    return os.path.split(helpers_dir)

def greptest_ospath():
    '''
    os.path.abspath(path)
    os.path.basename(path)
            .currdir
            .dirname(path)
            .getatime(filename)
            .exists(path)
            .expanduser(path)
            .expandvars(path)
            .splitdrive(path)
            .split(path)
    splitdrive(path)
    split(path)
    this_file_path = os.path.absPath(__file__)

    '''
    FILE_NAME = 'TEST.XML'
    os_path_abspath = os.path.abspath(__file__)
    os_path_basename = os.path.basename(__file__)
    os_path_dirname = os.path.dirname(__file__)
    os_path_abs_dirname = os.path.dirname(os_path_abspath)
    filename = os.path.join(os_path_dirname,FILE_NAME )
    abs_filename = os.path.join(os_path_abs_dirname,FILE_NAME)
    print 'os_path.abspath(__file__)', os_path_abspath
    print 'os_path.basename(__file__)', os_path_basename
    print 'os_path.dirname(__file__)', os_path_dirname
    print 'os.path.join(os_path_dirname,FILE_NAME )', filename
    print 'os.path.join(os_path_abs_dirname,FILE_NAME )', abs_filename


    # useful sequence of calls
    print
    print '**** useful sequence of calls ****'
    os_path_abspath2 = os.path.abspath(__file__)
    os_abs_path_dirname2 = os.path.dirname(os_path_abspath2)
    os_abs_path_dirname3 = os.path.dirname(os_abs_path_dirname2)
    abs_filename2 = os.path.join(os_abs_path_dirname2,FILE_NAME)
    abs_filename3 = os.path.join(os_abs_path_dirname3, FILE_NAME)
    print 'abs_filename2:', abs_filename2
    print 'abs_filename3:', abs_filename3




if __name__ == "__main__":
    #fileio_3()
    #print get_base_dir_path()
    #test_ospath()
    fileio_5()
    

