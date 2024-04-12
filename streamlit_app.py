# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import importlib
import time
from typing import Dict
import streamlit as st
import json
from utils import logger, make_prompt, read_yaml
from ticket.steps import output

config = read_yaml("config.yaml")

st.set_page_config(
    page_title=config.get("title"),
    page_icon=":robot:",
)

def predict_only_model(text, model):
    # params_dict = st.session_state["params"]
    response = model(text, history=None,)
    print(json.loads(response))
    return json.loads(response)


def bot_print(content, avatar: str = "🤖"):
    with st.chat_message("assistant", avatar=avatar):
        message_placeholder = st.empty()
        full_response = ""
        for chunk in content.split('。'):
            full_response += chunk + "  \n"
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "  \n")
        message_placeholder.markdown(full_response)




def tips(txt: str, wait_time: int = 2, icon: str = "🎉"):
    st.toast(txt, icon=icon)
    time.sleep(wait_time)


if __name__ == "__main__":
    title = config.get("title")
    version = config.get("version", "0.0.1")
    st.markdown(
        f"<h3 style='text-align: center;'>{title} v{version}</h3><br/>",
        unsafe_allow_html=True,
    )

    llm_module = importlib.import_module("llm")
    llm_params: Dict[str, Dict] = config.get("LLM_API")
    select_model = 'ERNIEBot'
    # menu_col1, menu_col2, menu_col3 = st.columns([1, 1, 1])
    # select_model = menu_col1.selectbox("🎨LLM:", llm_params.keys())
    # if "ERNIEBot" in select_model:
    #     with st.expander("LLM ErnieBot", expanded=True):
    #         opt_col1, opt_col2 = st.columns([1, 1])
    #         api_type = opt_col1.selectbox(
    #             "API Type(必选)",
    #             options=["aistudio", "qianfan", "yinian"],
    #             help="提供对话能力的后端平台",
    #         )
    #         access_token = opt_col2.text_input(
    #             "Access Token(必填) &nbsp;[如何获得？](https://github.com/PaddlePaddle/ERNIE-Bot-SDK/blob/2520b8d482a36e39fcb2287614197a981ecb6b79/erniebot/docs/authentication.md)",
    #             "",
    #             help="用于访问后端平台的access token（参考使用说明获取），如果设置了AK、SK则无需设置此参数",
    #         )
    #         llm_params[select_model]["api_type"] = api_type
    #
    #         if access_token:
    #             llm_params[select_model]["access_token"] = access_token

    MODEL_OPTIONS = {
        name: getattr(llm_module, name)(**params) for name, params in llm_params.items()
    }



    # with st.expander("💡Prompt", expanded=False):
    #     text_area = st.empty()
    #     input_prompt = text_area.text_area(
    #         label="Input",
    #         max_chars=500,
    #         height=200,
    #         label_visibility="hidden",
    #         value=config.get("DEFAULT_PROMPT"),
    #         key="input_prompt",
    #     )
    bot_print("我是操作票生成助手，你可以输入操作任务和设备的相关信息，我帮你生成操作票。（暂时仅支持台区、柱上开关（含自动化）运行转检修或检修转运行）\n\
              例如：将110kV西南站10kv斗文线FA2 #1杆流沙公用台由运行转检修，有1个低压刀闸，3个低压开关")
    input_txt = st.chat_input("问点啥吧！")
    if input_txt:
        with st.chat_message("user", avatar="😀"):
            st.markdown(input_txt)

        llm = MODEL_OPTIONS[select_model]
        input_prompt = config.get("DEFAULT_PROMPT")
        # if not input_prompt:
        #     input_prompt = config.get("DEFAULT_PROMPT")

        # bot_print("从知识库中抽取结果为空，直接采用LLM的本身能力回答。", avatar="📄")
        json_results = predict_only_model(input_txt, llm)
        response = output(
            name=json_results.get('设备名称', ''),
            model=json_results.get('设备类型', ''),
            before=json_results.get('操作前状态', ''),
            after=json_results.get('操作后状态', ''),
            blade=json_results.get('高压刀闸数量', 1),
            auto=json_results.get('自动化开关', 'false'),
            l_model=json_results.get('台区低压配置', ''),
            l_blade=json_results.get('低压刀闸数量', 1),
            l_switch=json_results.get('低压开关数量', 1),
        )
        str_result = '\n'.join(response)
        # print(str_result)
        bot_print(str_result)
