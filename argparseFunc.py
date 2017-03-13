import argparse



def one():
    parser = argparse.ArgumentParser()
    parser.parse_args()

# POSITIONAL ARGUMENTS
def sample_two():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print args.echo

def sample_three():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    print args.echo

def sample_four():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number")
    args = parser.parse_args()
    print args.square ** 2
    # should return a type error since argparse assumes str values unless we say differently

def sample_five():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number",
                        type=int)
    args = parser.parse_args()
    print args.square ** 2

# OPTIONAL ARGUMENTS
def sample_6():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="increase output verbosity")
    args = parser.parse_args()
    if args.verbosity:
        print "verbosity turned on"


# make the parameter more of a flag rather than a variable - set it to true by default - it no longer accepts a value
def sample_7():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print "verbosity turned on"

# short option: -v, --verbose
def sample_8():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print "verbosity turned on"

# Combining Positional and Optional arguments
def sample_9():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbose:
        print "the square of {} equals {}".format(args.square, answer)
    else:
        print answer


# restrict the range of input values
def sample_10():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbosity == 2:
        print "the square of {} equals {}".format(args.square, answer)
    elif args.verbosity == 1:
        print "{}^2 == {}".format(args.square, answer)
    else:
        print answer


sample_9()
