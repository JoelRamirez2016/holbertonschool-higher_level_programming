class Square:
    """This class define a Square

    Attributes:
        size (int): area of the square, must be an integer and >=0

    """
    def __init__(self, size = 0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size # private Attribute
