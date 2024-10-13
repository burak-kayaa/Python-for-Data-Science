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
    dotproduct(V1, V2)
        Dot product of two vectors
    add_vec(V1, V2)
        Adding two vectors
    sous_vec(V1, V2)
        Subtracting two vectors
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Dot product of two vectors
        """
        if len(V1) == len(V2):
            dot_product = 0
            for i in range(len(V1)):
                dot_product += V1[i] * V2[i]
            print("Dot product is: " + str(dot_product))
        else:
            raise ValueError("Vectors must be of the same length")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adding two vectors
        """
        if len(V1) == len(V2):
            add = []
            for i in range(len(V1)):
                add.append(V1[i] + V2[i])
            print("Add Vector is : " + str([f"{num:.1f}" for num in add]))
        else:
            raise ValueError("Vectors must be of the same length")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracting two vectors
        """
        if len(V1) == len(V2):
            sub = []
            for i in range(len(V1)):
                sub.append(V1[i] - V2[i])
            print("Sous Vector is: " + str([f"{num:.1f}" for num in sub]))
        else:
            raise ValueError("Vectors must be of the same length")
