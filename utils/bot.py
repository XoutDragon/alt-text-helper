from typing import Optional
from openai import OpenAI


class ImageBot(OpenAI):

    def __init__(self, model: str, url: Optional[str], api_key: str) -> None:
        super().__init__(
            api_key=api_key,
            base_url=url,
        )
        self.model = model

    def get_response(
        self, system_prompt: Optional[str], user_prompt: str
    ) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_prompt})

        response = self.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content or ""