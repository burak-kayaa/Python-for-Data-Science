from abc import ABC, abstractmethod


class Character(ABC):
    """
    Character class

    Attributes:
        first_name: a string representing the first name of the character
        is_alive: a boolean representing if the character is
        alive or not

    Methods:
        is_alive: a method that sets the is_alive attribute to False
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Character class constructor

        Args:
            first_name: a string representing the first name of the character
            is_alive: a boolean representing if the character is alive or not
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Character class die method
        """
        self.is_alive = False


class Stark(Character):
    """
    Stark character class
    """
    def __init__(self, first_name, is_alive=True):
        """
        Stark class constructor

        Args:
            first_name: a string representing the first name of the character
            is_alive: a boolean representing if the character is alive or not
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Stark class die method
        """
        self.is_alive = False
