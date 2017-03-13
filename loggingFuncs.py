"""
    logging notes

        --log=debug

     Advanced Logging
        logger
        handler
        filter
        formatter


"""


import logging

def simple_example():
    # simple logging - default log level is Warning and all levels below it
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything  - default level is Warning and below
    logging.warning('%s before you %s', 'Look', 'leap!')  # format the output

def intermediate_example():
    # define the format of the log mesage
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')

def intermediate2():
    logging.basicConfig(format='%(asctime)s %(message)s')
    logging.warning('is when this event was logged.')

def intermediate3():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('is when this event was logged.')


def log_to_a_file():
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    #    mylib.do_something()
    logging.info('Finished')


def test_func(num):
    print num
    return num+1

def test_func2(rec):
    rec2=rec
    rec2[]

def test_func3():
    myrec = {}
    myrec = test_func(myrec)


if __name__ == '__main__':
    #    simple_example()
    #    log_to_a_file()
    #    intermediate_example()
    # intermediate3()
    rec={}
    val = test_func(rec)
    print rec, val
