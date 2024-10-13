from load_image import ft_load
import numpy as np
from PIL import Image


def transpoze_array(array: np.ndarray) -> np.ndarray:
    """
    Transpose the given array manually
    (ignoring the third dimension if present) and print it.

    Parameters:
    ----------
    array : np.ndarray
        The array to transpose.
    """
    if array.ndim == 3:
        array = array[:, :, 0]
    new_array = []
    for j in range(len(array[0])):
        tmp_array = []
        for i in range(len(array)):
            tmp_array.append(array[i][j])
        new_array.append(tmp_array)
    new_array = np.array(new_array)
    print(f"New shape after Transpose: {new_array.shape}")
    print(new_array)
    return new_array


def main():
    path = "./animal.jpeg"
    image = Image.open(path)
    ft_load(path)
    zoomed_image = image.crop((400, 100, 800, 500))
    gray_image = zoomed_image.convert("L")
    gray_array = np.array(gray_image)
    print(f"The shape of image is: {gray_array.shape}")
    print(gray_array)
    transpozed_array = transpoze_array(gray_array)
    transpozed_image = Image.fromarray(transpozed_array)
    transpozed_image.show()


if __name__ == '__main__':
    main()
