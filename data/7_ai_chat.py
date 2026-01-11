# 인터프리터선택(ctrl+shift+p) -> 실행은 ctrl+j에서 가상환경에서 streamlit run 7_chat.py
# https://docs.streamlit.io/
import streamlit as st
from ai_llm import ask_with_reference_rerank

st.set_page_config(page_title="소득세 쳇봇", page_icon="💰")
# print("===============\n시작")
st.title("💰소득세 쳇봇")
st.caption("소득세에 관련된 질문을 답해 드려요")
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 대화 이력 표시
for msg in st.session_state.messages:
  #st.chat_message(msg["role"]).write(msg["content"])
  with st.chat_message(msg["role"]):
    st.write(msg["content"])

if user_question := st.chat_input(placeholder="소득세에 관련된 질문을 물어보세요"):
  #st.chat_message("user").write(user_question)
  with st.chat_message("user"):
    st.write(user_question)
  st.session_state.messages.append({"role":"user", "content":user_question})

  # AI 응답을 받아 session 추가하고 출력
  with st.spinner("질문에 답변을 생성하는 중입니다..."):
    # chat_history를 함께 전달
    answer = ask_with_reference_rerank(user_question)
    with st.chat_message("ai"):
      st.write(answer)
    st.session_state.messages.append({"role":"ai", "content":answer})