#try to add configurations so argv is supported in vscode
import sys

def print_args(args):
    for arg in args:
        print(arg)

def check_valid(args):
    """
    checks to see, given a list of arguments, 
    if the second argument is one of -p, -i, or -h and returns True if it is; otherwise, it returns False.
    """
    if args[1] in ["-p", "-i", "-h", "-w", "-r"]:
        return True
    else:
        return False
    
def write_to(args):
    """
    writes to file the text specified.
    """
    with open(args[2], "w") as file:
        #file.write("Debug")
        if len(args) <= 3:
            error_line = "No Content Provided"
            print(error_line)
        else:
            for arg in args[3:]:
                file.write(arg.strip() + "\n")

def read_from(filename):
    """
    reads from file specified in command line input
    """
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

    #error in this code is that the whitespace isn't read at the end of the file
    


def flags(args):
    """
    takes in a list of arguments. If there is a valid flag in the proper spot, flags should do the following based on the flag:
    -p - print out all the command line arguments after the -p (on separate lines)
    -i - print "Hello World"
    -h - prints out a help command with the following information
    """
    if args[1] == "-p":
        print_args(args[2:])
    if args[1] == "-i":
        print("Hello World")
    if args[1] == "-h":
        print("Valid flags:")
        print("-p : prints out all the command line arguments after the -p")
        print("-i : prints \"Hello World\"")
        print("-h : prints out a help command")
    if args[1] == "-w":
        write_to(args)
    if args[1] == "-r":
        read_from(args[2])

def main():
    """
    If there is a valid flag, call flags
    Else, call print_args
    """
    args = sys.argv # takes in all command line info, including the filename lab06.py

    if check_valid(args):
        flags(args)
    else:
        print_args(args)


if __name__ == "__main__":
    main()
