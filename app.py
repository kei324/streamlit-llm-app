from dotenv import load_dotenv
load_dotenv() 

from openai import OpenAI

import streamlit as st
st.title("課題提出:LLMアプリ")

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


input_message = st.text_input(label="質問を入力してください。")
selected_item = st.radio(
    "専門家を選択してください。",
    ["経営の専門家", "健康の専門家"],
)
st.divider()

if selected_item == "経営の専門家":
    messages = [
    SystemMessage(content="あなたは経営の専門家です。"),
    HumanMessage(content=input_message),
]
    result = llm(messages)
else:
    messages = [
    SystemMessage(content="あなたは健康の専門家です。"),
    HumanMessage(content=input_message),
]
    result = llm(messages)

if st.button("実行"):
    st.divider()
    st.write(result.content)
    st.divider()