class Node:

    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = value


class SinglyLinkedList:

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        curr_node = self.__head
        string = ""

        while (curr_node):
            string += str(curr_node.data) + "\n"
            curr_node = curr_node.next_node
        return string

    def sorted_insert(self, value):
        curr = self.__head
        newN = Node(value)

        if curr is None:
            self.__head = newN
        elif curr.data > value:
            newN.next_node = self.__head 
            self.__head = newN
            print(self.__head)
            print(self.__head.data.data)
#        else:
#            while (curr.next_node and curr.next_node.data < value):
#                curr = curr.next_node
#            newN.next_node = curr.next_node
#            curr.next_node = newN
