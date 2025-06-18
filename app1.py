# app.py
import streamlit as st
import random

# 단원별 예시 단어 데이터 (실제 크롤링 또는 파일 불러오기 대체 가능)
unit_words = {
    "Unit 1": [
        {"word": "school", "meaning": "학교", "options": ["school", "park", "library", "hospital"]},
        {"word": "teacher", "meaning": "선생님", "options": ["student", "teacher", "doctor", "driver"]},
    ],
    "Unit 2": [
        {"word": "apple", "meaning": "사과", "options": ["banana", "grape", "apple", "peach"]},
        {"word": "book", "meaning": "책", "options": ["pen", "notebook", "book", "eraser"]},
    ]
}

st.set_page_config(page_title="5학년 영어 단어 퀴즈", layout="centered")
st.title("📖 5학년 영어 단어 퀴즈")

# 초기 상태 설정
if 'page' not in st.session_state:
    st.session_state.page = 'select_unit'
    st.session_state.unit = None
    st.session_state.quiz = []
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.wrong_try = 0

# 유닛 선택 화면
if st.session_state.page == 'select_unit':
    st.subheader("단원을 선택하세요:")
    unit = st.selectbox("단원", list(unit_words.keys()))
    if st.button("시작하기"):
        st.session_state.unit = unit
        st.session_state.quiz = random.sample(unit_words[unit], min(10, len(unit_words[unit])))
        st.session_state.page = 'quiz'
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.wrong_try = 0
        st.experimental_rerun()

# 퀴즈 풀이 화면
elif st.session_state.page == 'quiz':
    q = st.session_state.quiz[st.session_state.current]
    st.subheader(f"문제 {st.session_state.current + 1}/10")
    st.write(f"'**{q['meaning']}**'의 영어 단어는 무엇일까요?")

    for opt in q['options']:
        if st.button(opt):
            if opt == q['word']:
                st.success("정답입니다!")
                st.session_state.score += 1
                st.session_state.current += 1
                st.session_state.wrong_try = 0
            else:
                st.session_state.wrong_try += 1
                if st.session_state.wrong_try >= 2:
                    st.error(f"정답은 '{q['word']}'입니다.")
                    st.info("이 단어들의 뜻도 함께 알아보아요:")
                    for o in q['options']:
                        st.write(f"- {o}: ... (의미를 여기에 입력하세요)")
                    st.session_state.current += 1
                    st.session_state.wrong_try = 0
                else:
                    st.warning("다시 한 번 생각해보세요!")
            st.experimental_rerun()

    if st.session_state.current >= len(st.session_state.quiz):
        st.session_state.page = 'result'
        st.experimental_rerun()

# 결과 화면
elif st.session_state.page == 'result':
    st.success(f"퀴즈 완료! 총 {st.session_state.score}문제 맞췄어요! 👏")
    st.balloons()
    if st.button("처음으로 돌아가기"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

