#!/usr/bin/python3
""" a program called console.py that
contains the entry point of the command interpreter:
A command interpreter created with cmd uses a loop to
read all lines from its input, parse them, and
then dispatch the command to an appropriate command handler
"""
import cmd
from models import *
from models import storage

class HBNBCommand(cmd.Cmd):
    """defines the HBNBCommand interpreter"""
    prompt = '(hbnb)'
    classes =["BaseModel"]

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
    
    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        else:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj = storage.classes()[line]()
                obj.save()
                print(obj.id)
                
    def do_show(self, line):
        arg = line.split()
        if line == "":
            print("** class name missing **")
        elif arg[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **") 
        else:
            obj = storage.all()
            key = f"{arg[0]}.{arg[1]}"
            if key not in obj.keys():
                print("** no instance found **")
            else:
                print(obj[key])
        
    def do_destroy(self, line):
        arg = line.split()
        if line == "":
            print("** class name missing **")
        elif arg[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **") 
        else:
            obj = storage.all()
            key = f"{arg[0]}.{arg[1]}"
            if key not in obj.keys():
                print("** no instance found **")
            else:
                del(obj[key])
                storage.save()
                
    def do_all(self, line):
        arg = line.split()
        objs= storage.all()
        
        
                
            
if __name__ == '__main__':
        HBNBCommand().cmdloop()
