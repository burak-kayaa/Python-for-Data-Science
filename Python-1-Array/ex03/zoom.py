from load_image import ft_load
import numpy as np
from PIL import Image


def main():
    """
    Load an image, slice it, convert it to grayscale, and display it.
    """
    path = "./animal.jpeg"
    image = Image.open(path)
    values = ft_load(path)
    print(values)
    zoomed_image = image.crop((400, 100, 800, 500))
    gray_image = zoomed_image.convert("L")
    gray_array = np.array(gray_image)
    gray_array_reshaped = gray_array[:, :, np.newaxis]
    print(f"New shape after slicing: {gray_array_reshaped.shape}")
    print(gray_array_reshaped)
    gray_image.show()


if __name__ == '__main__':
    main()
