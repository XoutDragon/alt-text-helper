import os
from bot import ImageBot
from dotenv import load_dotenv

load_dotenv()


def decipher(images=[]):
    url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")
    bot = ImageBot("gemini-3.8-flash", url, api_key)
    print("Worked!")
    return

decipher()