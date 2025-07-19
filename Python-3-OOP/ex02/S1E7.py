from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon character class
    """
    def __init__(self, first_name, is_alive=True):
        """
        Baratheon class constructor


        Args:
            first_name: a string representing the first name of the character
            is_alive: a boolean representing if the character is alive or not
        """

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        String representation of the Baratheon character
        """
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Representation of the Baratheon character
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Baratheon class die method
        """
        self.is_alive = False


class Lannister(Character):
    """
    Lannister character class
    """
    def __init__(self, first_name, is_alive=True):
        """
        Lannister class constructor

        Args:
            first_name: a string representing the first name of the character
            is_alive: a boolean representing if the character is alive or not
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Lannister class die method
        """
        self.is_alive = False

    def __str__(self):
        """
        String representation of the Lannister character
        """
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"    

    def __repr__(self):
        """
        Representation of the Lannister character
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Create a Lannister character

        Args:
            first_name: a string representing the first name of the character
            is_alive: a boolean representing if the character is alive or not
        """
        return cls(first_name, is_alive)
