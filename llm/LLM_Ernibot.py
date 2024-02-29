# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from typing import List, Optional

import erniebot


class ERNIEBot:
    def __init__(self, api_type: str = None, access_token: str = None):
        self.api_type = 'aistudio'
        self.access_token = 'd825eeefff61b2fa0355228203c7835b3c183add'

    def __call__(self, prompt: str, history: Optional[List] = None, **kwargs):
        if not history:
            history = []

        response = erniebot.ChatCompletion.create(
            _config_={
                "api_type": self.api_type,
                "access_token": self.access_token,
            },
            model="ernie-3.5",
            # model="ernie-bot",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            functions=[
                {
                    "name": "get_name",
                    "description": "根据输入内容提取实体",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "操作任务": {
                                "type": "string",
                                "description": "描述一个操作任务，比如110kv流沙线#1杆流沙公用台由运行转检修",
                                "examples": [
                                    "110kv流沙线#1杆流沙公用台由运行转检修",
                                    "110kv流沙线#1杆1T1开关后段线路由运行转检修",
                                ],
                            },
                            "设备名称": {
                                "type": "string",
                                "description": "描述设备名称，比如110kv流沙站10kv流沙线AFA 流沙公用台支线 #1杆流沙公用台，110kv流沙站10kv流沙线AFA 流沙公用台支线 #1杆1T1开关",
                                "examples": [
                                    "110kv流沙站10kv流沙线AFA #2电缆分接箱支线 #1杆流沙公用台",
                                    "110kv流沙站10kv流沙线AFA 流沙公用台支线 #1杆1T1开关",
                                    "110kv流沙站10kv流沙线AFA #2电缆分接箱支线 #1杆 流沙公用台",
                                    "110kv流沙站10kv流沙线AFA 流沙公用台支线 #2电缆分接箱 603开关",
                                ],
                            },
                            "设备类型": {
                                "type": "string",
                                "description": "通过设备名称判断设备类型，例如‘110kv流沙站10kv流沙线AFA #2电缆分接箱支线 #1杆流沙公用台’应该判断为台区，‘110kv流沙站10kv流沙线AFA 流沙公用台支线 #1杆1T1开关’应判断为柱上开关，‘110kv流沙站10kv流沙线AFA 流沙公用台支线 #2电缆分接箱 603开关’应判断为电缆分接箱",
                                "enum": ["台区","柱上开关","电缆分接箱"],
                            },
                            "自动化开关": {
                                "type": "boolean",
                                "default": "false",
                                "description": "判断柱上开关是否属于自动化开关",
                            },
                            "台区低压配置": {
                                "type": "string",
                                "description": "判断台区低压配置为配电柜或是柱上刀闸",
                                "enum": ["配电柜","柱上刀闸"],
                                "default": "柱上刀闸",
                            },
                            "操作前状态": {
                                "type": "string",
                                "description": "判断设备操作前状态",
                                "enum": ["运行","热备用","冷备用","检修"],
                            },
                            "操作后状态": {
                                "type": "string",
                                "description": "判断设备操作后状态",
                                "enum": ["运行","热备用","冷备用","检修"],
                            },
                            "高压刀闸数量": {
                                "type": "number",
                                "description": "提取高压刀闸数量",
                                "default": 1,
                                "minimum": 0,
                                "maximum":2,
                            },
                            "低压刀闸数量": {
                                "type": "number",
                                "description": "提取低压刀闸数量",
                                "default": 1,
                                "minimum": 0,
                                "maximum":5,
                            },
                            "低压开关数量": {
                                "type": "number",
                                "description": "提取低压开关数量",
                                "default": 1,
                                "minimum": 0,
                                "maximum":5,
                            },
                        },
                        "required": [
                            "操作任务",
                            "设备名称",
                            "设备类型",
                            "自动化开关",
                            "台区低压配置",
                            "操作前状态",
                            "操作后状态",
                            "高压刀闸数量",
                            "低压刀闸数量",
                            "低压开关数量",
                        ]
                    },
                    "responses": {
                        "type": "object",
                        "properties": {
                            "操作任务": {
                                "type": "string",
                                "description": "描述一个操作任务，比如将110kv流沙站10kv流沙线AFA #1杆流沙公用台由运行转检修",
                                "examples": [
                                    "将110kv流沙站10kv流沙线AFA #1杆流沙公用台由运行转检修",
                                    "将110kv流沙站10kv流沙线AFA #1杆1T1开关后段线路由运行转检修",
                                ],
                            },
                            "设备名称": {
                                "type": "string",
                                "description": "描述设备名称，比如110kv流沙站10kv流沙线AFA #1杆流沙公用台，110kv流沙站10kv流沙线AFA #1杆1T1开关",
                                "examples": [
                                    "110kv流沙站10kv流沙线AFA #1杆流沙公用台",
                                    "110kv流沙站10kv流沙线AFA #1杆1T1开关",
                                ],
                            },
                            "设备类型": {
                                "type": "string",
                                "description": "通过设备名称判断设备类型，例如台区、柱上开关、电缆分接箱",
                                "enum": ["台区","柱上开关","电缆分接箱"],
                            },
                            "自动化开关": {
                                "type": "boolean",
                                "default": "false",
                                "description": "判断柱上开关是否属于自动化开关",
                            },
                            "台区低压配置": {
                                "type": "string",
                                "description": "判断台区低压配置为配电柜或是柱上刀闸",
                                "enum": ["配电柜","柱上刀闸"],
                                "default": "柱上刀闸",
                            },
                            "操作前状态": {
                                "type": "string",
                                "description": "判断设备操作前状态",
                                "enum": ["运行","热备用","冷备用","检修"],
                            },
                            "操作后状态": {
                                "type": "string",
                                "description": "判断设备操作后状态",
                                "enum": ["运行","热备用","冷备用","检修"],
                            },
                            "高压刀闸数量": {
                                "type": "number",
                                "description": "提取高压刀闸数量",
                                "default": 1,
                                "minimum": 0,
                                "maximum":2,
                            },
                            "低压刀闸数量": {
                                "type": "number",
                                "description": "提取低压刀闸数量",
                                "default": 1,
                                "minimum": 0,
                                "maximum":5,
                            },
                            "低压开关数量": {
                                "type": "number",
                                "description": "提取低压开关数量",
                                "default": 1,
                                "minimum": 0,
                                "maximum":5,
                            },
                        },
                    }
                }
            ]
        )
        result = response.function_call['arguments']
        return result
