#!/usr/bin/python3
"""100-singly_linked_list
Define the class Node and SinglyLinkedList
"""


class Node:
    """Node: This class define a node to create linked list

    Attributes:
        data (int): integer to store in the node
        next_node (Node): next node
    """
    def __init__(self, data, next_node=None):
        """init_method to create a node
        Args:
            data (int): integer to store in the node
            next_node (Node): next node
        """
        if type(data) != int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get/set for the Node.data attr"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set for the Node.next_node attr"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList: This class define the methods for a linked list
    using Node implementation

    Attributes:
        head (Node): head Node of the list
    """
    def __init__(self):
        """Initalize a new SinglyLinkedList
        """
        self.__head = None

    def __str__(self):
        """String representation of the list
        Returns:
           formatted string
        """
        curr_node = self.__head
        string = ""

        while (curr_node):
            string += str(curr_node.data)
            curr_node = curr_node.next_node
            if curr_node:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """Insert a new node created with data = value in ascendent order

        Args:
            value (int): The value of the Node to create.
        """
        curr = self.__head
        newN = Node(value)

        if curr is None:
            self.__head = newN
        elif curr.data > value:
            newN.next_node = self.__head
            self.__head = newN
        else:
            while (curr.next_node and curr.next_node.data < value):
                curr = curr.next_node
            newN.next_node = curr.next_node
            curr.next_node = newN
