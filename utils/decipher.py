import os
from bot import ImageBot


def decipher(images):
    bot = ImageBot("gemini-3.8-flash",os.getenv("BASE_URL"), os.getenv("API_KEY"))
    return