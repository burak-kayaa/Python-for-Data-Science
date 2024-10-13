from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class
    """

    def die(self):
        """
        King class die method
        """
        self.is_alive = False

    def set_eyes(self, eyes):
        """
        Set the eyes attribute

        Args:
            eyes: a string representing the eyes color
        """
        self.eyes = eyes

    def get_eyes(self):
        """
        Get the eyes attribute
        """
        return self.eyes

    def set_hairs(self, hairs):
        """
        Set the hairs attribute

        Args:
            hairs: a string representing the hairs color
        """
        self.hairs = hairs

    def get_hairs(self):
        """
        Get the hairs attribute
        """
        return self.hairs
