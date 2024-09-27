from load_image import ft_load
import numpy as np
from PIL import Image

def main():
    path = "./animal.jpeg"
    image = Image.open(path)
    # image.show()
    values = ft_load(path)
    print(values)
    zoomed_image = image.crop((400, 100, 800, 500))
    print(f"New shape after cropping: {zoomed_image.size}")
    # zoomed_image.show()
    gray_image = zoomed_image.convert("L")
    print(np.array(gray_image))
    gray_image.show()

if __name__ == '__main__':
    main()