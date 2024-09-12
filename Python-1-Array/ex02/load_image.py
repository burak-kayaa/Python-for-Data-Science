from PIL import Image
import numpy as np


def ft_load(path: str) -> Image:
    """
    Load an image from a file and return it as a numpy array.
    If the image cannot be loaded, return None.

    Parameters:
    ----------
    path : str
        The path to the image file.

    Returns:
    -------
    np.ndarray
        The image as a numpy array.

    Raises:
    ------
    FileNotFoundError
        If the image cannot be loaded.
    """
    try:
        array = Image.open(path)
        h, w = array.size
        print(f"The shape of the image is: ({w}, {h}, {len(array.mode)})")
        return np.array(array)
    except FileNotFoundError:
        print("Error: Could not load image")
        return None
