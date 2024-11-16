from typing import List, Optional
from openai import OpenAI


class AtomBot:
    def __init__(self, api_type: str = None, access_token: str = None):
        self.api_type = 'aistudio'
        self.access_token = 'd825eeefff61b2fa0355228203c7835b3c183add'

    def __call__(self, prompt: str, history: Optional[List] = None, **kwargs):
        if not history:
            history = []
        client = OpenAI(
            api_key='sk-08dcd3d04ded49d77c11522b6a845c94',
            base_url="https://api.atomecho.cn/v1",
        )
        completion = client.chat.completions.create(
            model="Atom-7B-Chat",
            messages=[
                # {"role": "system", "content": prompt},
                {"role": "user", "content":prompt}
            ],
            temperature=0.5,
        )
        result=completion.choices[0].message.content
        return result
