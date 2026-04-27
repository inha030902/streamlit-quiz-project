import streamlit as st
import time

st.set_page_config(
    page_title="COYS Quiz",
    page_icon="⚽",
    layout="centered"
)

# -----------------------------
# 화면 디자인 CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background:
        linear-gradient(rgba(7, 20, 47, 0.86), rgba(7, 20, 47, 0.88)),
        linear-gradient(180deg, #07142f 0%, #0b1f4d 48%, #0b5d2a 100%);
    color: white;
}

.main-title {
    background: rgba(255, 255, 255, 0.12);
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.25);
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
    margin-bottom: 24px;
}

.main-title h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 8px;
}

.main-title p {
    color: #dbe7ff;
    font-size: 18px;
}

.info-card {
    background: rgba(255,255,255,0.94);
    color: #07142f;
    padding: 18px 22px;
    border-radius: 18px;
    margin-bottom: 18px;
    border-left: 8px solid #132257;
}

.quiz-card {
    background: rgba(255,255,255,0.96);
    color: #07142f;
    padding: 18px 22px;
    border-radius: 18px;
    margin: 18px 0 8px 0;
    box-shadow: 0 6px 18px rgba(0,0,0,0.22);
    border-left: 7px solid #0b5d2a;
}

.result-card {
    background: rgba(255,255,255,0.96);
    color: #07142f;
    padding: 24px;
    border-radius: 20px;
    margin-top: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.28);
}

.stButton > button {
    border-radius: 12px;
    font-weight: bold;
}

[data-testid="stRadio"] {
    background: rgba(255,255,255,0.88);
    padding: 10px;
    border-radius: 12px;
    color: #07142f;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 첫 화면
# -----------------------------
st.markdown("""
<div class="main-title">
    <h1>⚽ COYS Quiz</h1>
    <p>Tottenham Hotspur Fan Knowledge Test</p>
    <p>토트넘 홈구장 피치 위에서 퀴즈를 푸는 팬 테스트</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <h3>📌 프로젝트 정보</h3>
    <p><b>과목:</b> 오픈소스소프트웨어실습 중간고사 대체 과제</p>
    <p><b>학번:</b> 2022204068</p>
    <p><b>이름:</b> 최인하</p>
    <p><b>주제:</b> 토트넘 홋스퍼 팬 지식 퀴즈 웹 애플리케이션</p>
</div>
""", unsafe_allow_html=True)

st.divider()


# -----------------------------
# 캐싱 기능
# -----------------------------
@st.cache_data
def load_quiz_data():
    """
    퀴즈 데이터는 앱이 실행될 때마다 반복해서 새로 만들 필요가 없으므로
    Streamlit 캐싱 기능을 사용하여 한 번 불러온 데이터를 재사용한다.
    """
    time.sleep(1)

    questions = [
        {
            "question": "토트넘 홋스퍼의 별명으로 가장 적절한 것은?",
            "options": ["The Reds", "The Blues", "Spurs", "The Gunners"],
            "answer": "Spurs"
        },
        {
            "question": "토트넘의 홈구장 이름은?",
            "options": ["Emirates Stadium", "Tottenham Hotspur Stadium", "Old Trafford", "Anfield"],
            "answer": "Tottenham Hotspur Stadium"
        },
        {
            "question": "토트넘의 대표 응원 구호는?",
            "options": ["You'll Never Walk Alone", "COYS", "Glory Glory Man United", "Blue Moon"],
            "answer": "COYS"
        },
        {
            "question": "COYS의 뜻으로 알맞은 것은?",
            "options": [
                "Come On You Spurs",
                "City Of Young Stars",
                "Club Of Yellow Soccer",
                "Come On Your Side"
            ],
            "answer": "Come On You Spurs"
        },
        {
            "question": "토트넘 홋스퍼가 마지막으로 잉글랜드 1부 리그 우승을 차지한 시기는?",
            "options": ["1950-51 시즌", "1960-61 시즌", "1970-71 시즌", "1980-81 시즌"],
            "answer": "1960-61 시즌"
        },
        {
            "question": "토트넘의 상징 동물로 가장 적절한 것은?",
            "options": ["사자", "닭", "독수리", "여우"],
            "answer": "닭"
        },
        {
            "question": "토트넘이 속한 리그는?",
            "options": ["La Liga", "Bundesliga", "Premier League", "Serie A"],
            "answer": "Premier League"
        },
        {
            "question": "토트넘과 북런던 라이벌 관계에 있는 팀은?",
            "options": ["아스널", "에버턴", "브라이튼", "웨스트햄"],
            "answer": "아스널"
        },
        {
            "question": "토트넘의 전통적인 유니폼 색 조합으로 가장 적절한 것은?",
            "options": ["빨강 상의와 흰 바지", "파랑 상의와 검정 바지", "흰 상의와 남색 바지", "초록 상의와 흰 바지"],
            "answer": "흰 상의와 남색 바지"
        },
        {
            "question": "토트넘 홋스퍼 스타디움이 개장한 연도는?",
            "options": ["2015년", "2017년", "2019년", "2021년"],
            "answer": "2019년"
        }
    ]

    return questions


# -----------------------------
# 로그인 상태 초기화
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""


# -----------------------------
# 로그인 기능
# -----------------------------
st.subheader("🔐 Spurs Fan Login")

if not st.session_state.logged_in:
    user_id = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")

    st.caption("테스트 계정: ID = spurs / PW = 1882")

    if st.button("로그인"):
        if user_id == "spurs" and password == "1882":
            st.session_state.logged_in = True
            st.session_state.username = user_id
            st.success("로그인 성공! COYS Quiz를 시작할 수 있습니다.")
            st.rerun()
        else:
            st.error("로그인 실패: 아이디 또는 비밀번호가 올바르지 않습니다.")

else:
    st.success(f"{st.session_state.username}님, 로그인되었습니다.")

    if st.button("로그아웃"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.divider()

    # -----------------------------
    # 퀴즈 기능
    # -----------------------------
    st.subheader("🏟️ Tottenham Hotspur Quiz")

    with st.spinner("퀴즈 데이터를 불러오는 중입니다..."):
        quiz_data = load_quiz_data()

    st.info("퀴즈 데이터는 @st.cache_data를 사용하여 캐싱됩니다.")

    score = 0
    user_answers = []

    with st.form("quiz_form"):
        for i, q in enumerate(quiz_data):
            st.markdown(
                f"""
                <div class="quiz-card">
                    <h3>Q{i + 1}. {q['question']}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            selected = st.radio(
                label="정답을 선택하세요.",
                options=q["options"],
                key=f"question_{i}"
            )
            user_answers.append(selected)

        submitted = st.form_submit_button("결과 확인하기")

    if submitted:
        st.divider()
        st.subheader("🏆 퀴즈 결과")

        for i, q in enumerate(quiz_data):
            if user_answers[i] == q["answer"]:
                score += 1

        st.markdown(
            f"""
            <div class="result-card">
                <h2>🏟️ Match Result</h2>
                <p>총 {len(quiz_data)}문제 중 <b>{score}문제</b>를 맞혔습니다.</p>
                <p>당신의 토트넘 팬 지식을 기준으로 등급이 결정됩니다.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("📊 등급 체계")

        grade_table = {
            "점수 범위": ["0~3점", "4~7점", "8~10점"],
            "등급": ["입문 팬", "꽤 아는 스퍼스 팬", "진짜 COYS 팬"],
            "설명": [
                "토트넘을 알아가기 시작한 단계",
                "기본적인 토트넘 지식이 있는 팬",
                "토트넘에 대한 지식이 뛰어난 팬"
            ]
        }

        st.table(grade_table)

        if score <= 3:
            st.warning("당신의 등급은 **입문 팬**입니다. 이제부터 토트넘을 더 알아가면 됩니다!")
        elif score <= 7:
            st.info("당신의 등급은 **꽤 아는 스퍼스 팬**입니다. 기본 지식이 좋습니다!")
        else:
            st.success("당신의 등급은 **진짜 COYS 팬**입니다! 토트넘에 대한 지식이 훌륭합니다.")

        st.divider()

        st.subheader("✅ 정답 확인")

        for i, q in enumerate(quiz_data):
            if user_answers[i] == q["answer"]:
                st.write(f"Q{i + 1}. ✅ 정답: {q['answer']}")
            else:
                st.write(
                    f"Q{i + 1}. ❌ 내 답: {user_answers[i]} / 정답: {q['answer']}"
                )
