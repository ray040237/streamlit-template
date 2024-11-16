
DEFAULT_PROMPT='''
  #角色
  -你是一个智能助手，根据规则抽取信息，无需输出思考过程和注释文字，仅输出答案json格式。
  #提取规则
  1、操作任务，操作任务的规则：将xxx由xx转xx；
  2、设备名称，如：110kV流沙站10kv流沙线FA2 流沙支线#1杆流沙公用台，110kV流沙站10kv流沙线FA2 流沙支线#1杆斗文公用台，110kV流沙站10kv流沙线FA2 流沙支线#1杆1T1开关，110kV流沙站10kv流沙线FA2 流沙支线#1杆32T2开关，110kV流沙站10kv流沙线FA2 流沙支线#1电缆分接箱601开关，110kV流沙站10kv流沙线FA2 流沙支线#1电缆分接箱602开关；
  3、设备类型，判断选项：台区，柱上开关，电缆分接箱开关；例如：【110kV流沙站10kv流沙线FA2#1杆流沙公用台，110kV流沙站10kv流沙线FA2#1杆斗文公用台】应判断为“台区”，【110kV流沙站10kv流沙线FA2#1杆1T1开关，110kV流沙站10kv流沙线FA2#1杆32T2开关】应判断为“柱上开关”，【110kV流沙站10kv流沙线FA2 流沙支线#1电缆分接箱601开关，110kV流沙站10kv流沙线FA2 流沙支线#1电缆分接箱602开关】应判断为“电缆分接箱开关”；
  4、操作前状态，判断选项：运行，热备用，冷备用，检修；
  5、操作后状态，判断选项：运行，热备用，冷备用，检修；
  6、高压刀闸数量，使用阿拉伯数字；
  7、低压刀闸数量，使用阿拉伯数字；
  8、低压开关数量，使用阿拉伯数字；
  9、是否为自动化开关。
  #问题
  -将110kV流沙站10kv流沙线FA2#1杆1T1开关后段线路由运行转检修，有2个低压刀闸，3个低压开关
  #思考分析
  1、操作任务要符合规则：”将110kV流沙站10kv流沙线FA2#1杆1T1开关后段线路由运行转检修“。
  2、设备名称：”110kV流沙站10kv流沙线FA2#1杆1T1开关“；
  3、设备类型：根据设备名称判断设备类型，设备名称“110kV流沙站10kv流沙线FA2#1杆1T1开关”，判断为“柱上开关”。
  4、根据”运行转检修“可得出操作前状态："运行"
  5、根据”运行转检修“可得出操作后状态："检修"
  6、高压刀闸未提及输出0；
  7、低压刀闸数量是2个；
  8、低压开关数量是3个；
  9、是否为自动化开关未提及，输出false；
  # 答案
  {
  "操作任务": "将110kV流沙站10kv流沙线FA2#1杆1T1开关后段线路由运行转检修",
  "设备名称": "110kV流沙站10kv流沙线FA2#1杆1T1开关",
  "设备类型": "柱上开关",
  "操作前状态": "运行",
  "操作后状态": "检修",
  "高压刀闸数量": 0,
  "低压刀闸数量": 2,
  "低压开关数量": 3,
  "是否为自动化开关": false
  }
'''
import requests
import json
url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "01-ai/Yi-1.5-6B-Chat",
    # Qwen/Qwen2-1.5B-Instruct  Qwen/Qwen2.5-7B-Instruct  THUDM/chatglm3-6b  internlm/internlm2_5-7b-chat  01-ai/Yi-1.5-6B-Chat
    "messages": [
        {
            "role": "system",
            "content": DEFAULT_PROMPT
        },
        {
            "role": "user",
            "content": "将110kV南郊站10kV园林线FG6 #8杆绿地公用台由热备用转检修，有2个高压刀闸，有1个低压刀闸，2个低压开关。"
        }
    ],
    "stream": False
}
headers = {
    "Authorization": "Bearer sk-pritvkbdvlghpcbawpvalalvckgqtrjqmmrfbtxjqnqpkivu",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(json.loads(response.text)['choices'][0]['message']['content'])
