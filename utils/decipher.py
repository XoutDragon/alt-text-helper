from utils.bot import ImageBot


def decipher(image_path: str, bot: ImageBot) -> str:

    print(f"Found image: {image_path}")

    alt_text = bot.get_response(
        user_prompt="Generate a detailed alt text description for this image.",
        image_input=image_path,
    )
    print(f"\n[Image: {image_path}]\nAlt Text: {alt_text}")
    return alt_text
