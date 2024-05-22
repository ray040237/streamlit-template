from typing import List, Optional

from openai import OpenAI
from utils import extract_json



class DeepseekChat:
    def __init__(self, api_type: str = None, access_token: str = None):
        self.api_type = 'aistudio'
        self.access_token = 'd825eeefff61b2fa0355228203c7835b3c183add'

    def __call__(self, prompt: str, history: Optional[List] = None, **kwargs):
        if not history:
            history = []

        client = OpenAI(api_key="sk-4e8bf0f855b64b98a81a5828e284f395", base_url="https://api.deepseek.com/")
        sys_prompt = "根据用户输入内容提取以下实体：\
        1、操作任务；\
        2、设备名称；\
        3、设备类型，判断选项：台区，柱上开关，电缆分接箱开关；如：流沙公用台，斗文公用台为台区，1T1开关，32T2开关为柱上开关，601开关，602开关为电缆分接箱开关；\
        4、操作前状态，判断选项：运行，热备用，冷备用，检修；\
        5、操作后状态；\
        6、高压刀闸数量，使用阿拉伯数字，如果未提及的则默认为0；\
        7、低压刀闸数量；\
        8、低压开关数量；\
        9、是否为自动化开关，未提及则默认为否。\
        只用json格式输出，无需输出```json```字样。"
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        result = response.choices[0].message.content
        print(result)
        json_result=extract_json(result)
        print(json_result)
        return json_result
        # return result
