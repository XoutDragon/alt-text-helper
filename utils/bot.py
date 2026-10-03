import base64
import mimetypes
from typing import List, Optional, Union
from openai import OpenAI


class ImageBot(OpenAI):

    def __init__(self, model: str, url: Optional[str], api_key: str) -> None:
        super().__init__(api_key=api_key, base_url=url)
        self.model = model

    @staticmethod
    def _encode_image_to_base64(image_path: str) -> str:
        """Encodes a local image file to a base64 Data URL."""
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            mime_type = "image/jpeg"

        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        return f"data:{mime_type};base64,{encoded_string}"

    def get_response(
        self,
        user_prompt: str,
        system_prompt: Optional[str] = None,
        image_input: Optional[Union[str, List[str]]] = None,
    ) -> str:
        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        # Normalize single string to list for uniform handling
        if isinstance(image_input, str):
            image_inputs = [image_input]
        elif isinstance(image_input, list):
            image_inputs = image_input
        else:
            image_inputs = []

        if image_inputs:
            user_content = [{"type": "text", "text": user_prompt}]

            for item in image_inputs:
                if item.startswith(("http://", "https://", "data:image/")):
                    image_target = item
                else:
                    image_target = self._encode_image_to_base64(item)

                user_content.append(
                    {"type": "image_url", "image_url": {"url": image_target}}
                )
        else:
            user_content = user_prompt

        messages.append({"role": "user", "content": user_content})

        response = self.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content or ""