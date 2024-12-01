from load_image import ft_load
import numpy as np
from PIL import Image

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert the given array manually.
    """
    new_array = []
    for i in range(len(array)):
        tmp_array = []
        for j in range(len(array[0])):
            tmp_array.append(255 - array[i][j])
        new_array.append(tmp_array)
    new_array = np.array(new_array, dtype=np.uint8)
    return new_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keep only the red channel of the given array.
    """
    new_array = []
    for i in range(len(array)):
        tmp_array = []
        for j in range(len(array[0])):
            tmp_array.append([array[i][j][0], 0, 0])
        new_array.append(tmp_array)
    new_array = np.array(new_array, dtype=np.uint8)
    return new_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keep only the green channel of the given array.
    """
    new_array = []
    for i in range(len(array)):
        tmp_array = []
        for j in range(len(array[0])):
            tmp_array.append([0, array[i][j][1], 0])
        new_array.append(tmp_array)
    new_array = np.array(new_array, dtype=np.uint8)
    return new_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keep only the blue channel of the given array.
    """
    new_array = []
    for i in range(len(array)):
        tmp_array = []
        for j in range(len(array[0])):
            tmp_array.append([0, 0, array[i][j][2]])
        new_array.append(tmp_array)
    new_array = np.array(new_array, dtype=np.uint8)
    return new_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert the given array to grayscale manually.
    """
    new_array = []
    for i in range(len(array)):
        tmp_array = []
        for j in range(len(array[0])):
            gray_value = (
                0.299 * array[i][j][0] +
                0.587 * array[i][j][1] +
                0.114 * array[i][j][2]
            )
            tmp_array.append(int(gray_value))
        new_array.append(tmp_array)
    new_array = np.array(new_array, dtype=np.uint8)
    return new_array


def main():
    """
    Load an image, slice it, convert it to grayscale, and display it.
    """
    path = "./landscape.jpeg"
    array = ft_load(path)
    print(array)
    invert = ft_invert(array)
    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)
    grey = ft_grey(array)
    invert_image = Image.fromarray(invert)
    red_image = Image.fromarray(red)
    green_image = Image.fromarray(green)
    blue_image = Image.fromarray(blue)
    grey_image = Image.fromarray(grey)
    invert_image.show()
    red_image.show()
    green_image.show()
    blue_image.show()
    grey_image.show()

if __name__ == '__main__':
    main()
