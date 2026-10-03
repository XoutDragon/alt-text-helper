import json
import re
from typing import List
from utils.bot import ImageBot

def comparer(alt_texts: List[str], page_content: str, bot: ImageBot) -> List[str]:
    print(f"Comparing text: {alt_texts}")

    prompt = (
        f"Use the list of alternative texts, {alt_texts}, generated from the images within the HTML page "
        f"and compare the relevancy of each text to the contents of the page, {page_content}. "
        f"Return ONLY a valid JSON array of strings representing all the relevant alternative texts. "
        f"Remove non-relevant ones like logos, banners, and ads. Do not include extra commentary or markdown code blocks."
    )

    comparison_result = bot.get_response(user_prompt=prompt)
    print(f"\n[Text Comparison]\nResult: {comparison_result}")

    # Clean potential markdown formatting like ```json ... ```
    cleaned_result = re.sub(r"^```(?:json)?\s*|\s*```$", "", comparison_result.strip())

    try:
        parsed_list = json.loads(cleaned_result)
        if isinstance(parsed_list, list):
            return parsed_list
    except json.JSONDecodeError:
        pass

    # Fallback if string could not be parsed directly as JSON
    return [comparison_result]