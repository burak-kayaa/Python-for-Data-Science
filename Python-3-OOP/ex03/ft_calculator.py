class calculator():
    """
    A class to perform basic operations on a list of numbers

    ...

    Attributes
    ----------
    object : list
        a list of numbers

    Methods
    -------
    __add__(object)
        Adding a number to the object
    __mul__(object)
        Multiplying a number to the object
    __sub__(object)
        Subtracting a number to the object
    __truediv__(object)
        Dividing a number to the object
    """
    def __init__(self, object):
        self.object = object

    def __add__(self, object) -> None:
        """
        Adding a number to the object
        """
        for i in range(len(self.object)):
            self.object[i] += object
        print(self.object)

    def __mul__(self, object) -> None:
        """
        Multiplying a number to the object
        """
        for i in range(len(self.object)):
            self.object[i] *= object
        print(self.object)

    def __sub__(self, object) -> None:
        """
        Subtracting a number to the object
        """
        for i in range(len(self.object)):
            self.object[i] -= object
        print(self.object)

    def __truediv__(self, object) -> None:
        """
        Dividing a number to the object
        """
        for i in range(len(self.object)):
            if object != 0:
                self.object[i] /= object
            else:
                raise ValueError("Cannot divide by zero")
        print(self.object)
