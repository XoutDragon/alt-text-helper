import os
from utils import images
from utils import decipher
from utils import comparer

if __name__ == "__main__":
    API_KEY = os.getenv("API_KEY")
    BASE_URL = os.getenv("BASE_URL")


    images = images.get_images_from_file("resources/cat_distribution_system_demo.html")

    for image in images:
        text = decipher.decipher(image)
  
