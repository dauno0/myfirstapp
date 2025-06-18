# app.py
import streamlit as st
import random

st.set_page_config(page_title="구구단 퀴즈", layout="centered")

st.title("🧠 구구단 퀴즈 앱")

if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.questions = []
    st.session_state.finished = False

# 문제 생성 함수
def generate_questions(num=10):
    questions = []
    for _ in range(num):
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        correct = a * b
        wrong = random.sample([i for i in range(1, 82) if i != correct], 2)
        options = wrong + [correct]
        random.shuffle(options)
        questions.append({
            'a': a,
            'b': b,
            'correct': correct,
            'options': options
        })
    return questions

if not st.session_state.questions:
    st.session_state.questions = generate_questions(10)

if not st.session_state.finished:
    q = st.session_state.questions[st.session_state.question_index]
    st.subheader(f"문제 {st.session_state.question_index + 1}/10")
    st.write(f"{q['a']} × {q['b']} = ?")

    col1, col2, col3 = st.columns(3)
    for i, opt in enumerate(q['options']):
        with [col1, col2, col3][i]:
            if st.button(str(opt), key=f"btn{st.session_state.question_index}-{i}"):
                if opt == q['correct']:
                    st.success("정답입니다! 🎉 축하합니다!")
                    st.balloons()
                    st.session_state.score += 1
                    st.session_state.question_index += 1
                else:
                    st.warning("틀렸어요. 다시 도전해보세요! 💪")
                st.experimental_retrun()

    if st.session_state.question_index >= 10:
        st.session_state.finished = True
else:
    st.success(f"퀴즈 완료! 총 {st.session_state.score}문제 맞췄어요! 👏👏👏")
    st.info("멋져요! 계속 도전하면 더욱 잘할 수 있어요! 🌈")
