#!/usr/bin/python3
""" a program called console.py that
contains the entry point of the command interpreter:
A command interpreter created with cmd uses a loop to
read all lines from its input, parse them, and
then dispatch the command to an appropriate command handler
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """defines the HBNBCommand interpreter"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """command handler returns a true value,
        the program will exit cleanly
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ensures an empty line + ENTER doesnt execute anything
        """
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
