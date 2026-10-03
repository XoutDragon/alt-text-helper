from typing import Optional

from openai import OpenAI
#import AI to receive image and be able to check the image when needed
class ImageBot(OpenAI):
    def __init__(self, model, url, api_key) -> None:
        super().__init__()
        self.base_url = url
        self.api_key = api_key
        self.model = model

    def get_response(self, system_prompt: Optional[str], user_prompt: str) -> str:
        response = self.chat.completions.create(
            models=self.model,
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        )
        return response.choices[0].message.content