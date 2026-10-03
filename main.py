import os
from dotenv import load_dotenv
from utils import images
from utils.bot import ImageBot
from utils.decipher import decipher
from utils.comparer import comparer
from utils.content import get_content
from utils.tts import tts

if __name__ == "__main__":
    load_dotenv()
    MODEL = "qwen3.5"
    API_KEY = os.getenv("API_KEY")
    BASE_URL = os.getenv("BASE_URL")

    bot = ImageBot(MODEL, BASE_URL, API_KEY)

    images = images.get_images_from_html("resources/cat_distribution_system_demo.html")


    alt_texts = [decipher(image, bot) for image in images]
    
    content = get_content("resources/cat_distribution_system_demo.html", "/resources")

    relevant_alt_texts = comparer(alt_texts, content, bot)

    for alt_text in relevant_alt_texts:
        tts(alt_text)