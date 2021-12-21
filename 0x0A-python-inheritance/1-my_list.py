#!/usr/bin/python3
class MyList(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        last_sorted = self.copy()
        last_sorted.sort()
        print(last_sorted)
