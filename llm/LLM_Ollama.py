from typing import List, Optional

import ollama


class ollamaBot:
    def __init__(self, api_type: str = None, access_token: str = None):
        self.api_type = 'aistudio'
        self.access_token = 'd825eeefff61b2fa0355228203c7835b3c183add'

    def __call__(self, prompt: str, history: Optional[List] = None, **kwargs):
        if not history:
            history = []

        response = ollama.chat(
            # _config_={
            #     "api_type": self.api_type,
            #     "access_token": self.access_token,
            # },
            model="my",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        result = response['message']['content']
        return result
