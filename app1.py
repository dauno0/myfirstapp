# app1.py
import streamlit as st

# 임시 사전 데이터 (실제 배포 시 외부 API나 DB 연동 가능)
korean_dict = {
    "사랑": {
        "뜻": "어떤 사람이나 존재를 몹시 아끼고 소중히 여기는 마음.",
        "한자": ["愛"],
        "예문": [
            "그녀는 가족에 대한 사랑이 깊다.",
            "사랑은 서로를 이해하고 존중하는 것이다.",
            "첫사랑의 기억은 오래도록 남는다."
        ]
    },
    "우정": {
        "뜻": "친구 사이의 정이나 사랑.",
        "한자": ["友情"],
        "예문": [
            "오랜 우정은 쉽게 깨지지 않는다.",
            "우정을 지키는 것이 중요하다.",
            "진실한 우정은 서로를 배려하는 데서 시작된다."
        ]
    },
    "행복": {
        "뜻": "기쁘고 즐거움. 또는 그러한 상태.",
        "한자": ["幸福"],
        "예문": [
            "행복은 가까운 곳에 있다.",
            "가족과 함께하는 시간이 가장 큰 행복이다.",
            "행복은 마음먹기에 달려 있다."
        ]
    }
}

st.set_page_config(page_title="국어 단어 사전", layout="centered")
st.title("📘 국어 단어 사전 앱")

# 입력창
word = st.text_input("단어를 입력하세요:")

if word:
    if word in korean_dict:
        data = korean_dict[word]

        st.subheader("📖 뜻")
        st.write(data["뜻"])

        st.subheader("🈷️ 한자")
        selected_hanja = st.radio("해당 단어의 한자를 선택하세요:", data["한자"])

        st.subheader("📌 예문")
        for example in data["예문"]:
            st.write(f"- {example}")

        st.divider()
        st.text_input("다시 단어를 입력하세요:", key="retry")
    else:
        st.warning("사전에 없는 단어입니다. 다른 단어를 입력해 보세요.")
