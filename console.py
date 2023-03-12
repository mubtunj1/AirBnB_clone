#!/usr/bin/python3
""" a program called console.py that
contains the entry point of the command interpreter:
A command interpreter created with cmd uses a loop to
read all lines from its input, parse them, and
then dispatch the command to an appropriate command handler
"""
import cmd
from models import *


class HBNBCommand(cmd.Cmd):
    """defines the HBNBCommand interpreter"""
    prompt = '(hbnb) '

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
        """Command handler creates a new instance of a class,
        saves it to JSON file and prints id"""
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
        """Command handler prints the string representation
        of an instance based on the class name and id"""
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
        """Command handler deletes an instance based on the class
        name and id and saves the changes in a JSON file"""
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
        """Command handler prints all str representations
        of all instances based or not on the class name"""
        list = []
        arg = line.split()
        objs = storage.all()
        if not arg:
            for key in objs.keys():
                list.append(str(objs[key]))
            print(list)

        elif arg[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            for key in objs.keys():
                kwarg = key.split(".")
                if arg[0] == kwarg[0]:
                    list.append(str(objs[key]))
            print(list)

    def do_update(self, line):
        """Command handler updates an instance based on the class
        name and id by adding or updating an attribute"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objs.keys():
                print("** no instance found **")
            else:
                setattr(objs[key], args[2], args[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
