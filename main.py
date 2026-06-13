import streamlit as st

st.set_page_config(
    page_title="⚽ 축구선수 하이라이트 추천기",
    page_icon="⚽",
    layout="centered"
)

players = {
    "메시": {
        "emoji": "🐐",
        "highlight": "2015 바이에른 뮌헨전 보아텡 드리블 골",
        "personality": "천재형 플레이메이커. 침착하고 창의적이며 경기의 흐름을 지배해요."
    },
    "호날두": {
        "emoji": "🚀",
        "highlight": "2018 유벤투스전 오버헤드킥",
        "personality": "노력형 승부사. 자신감이 넘치고 목표를 향해 끝없이 도전해요."
    },
    "음바페": {
        "emoji": "⚡",
        "highlight": "2022 월드컵 결승전 해트트릭",
        "personality": "초고속 공격수. 대담하고 에너지가 넘치며 결정적인 순간에 강해요."
    },
    "네이마르": {
        "emoji": "🎭",
        "highlight": "산투스 시절 플라멩구전 원더골",
        "personality": "예술가형 드리블러. 창의적이고 화려한 플레이를 즐겨요."
    },
    "손흥민": {
        "emoji": "🇰🇷",
        "highlight": "번리전 70m 원더골",
        "personality": "겸손한 리더. 성실하고 팀을 위해 헌신하는 스타일이에요."
    },
    "홀란드": {
        "emoji": "🦁",
        "highlight": "맨시티 데뷔 시즌 5골 경기",
        "personality": "파괴형 스트라이커. 강력하고 직선적이며 득점 본능이 뛰어나요."
    }
}

st.title("⚽ 축구선수 하이라이트 추천기")
st.markdown("---")

st.markdown("""
### 🏟️ 내가 좋아하는 축구선수의 대표 명장면은?
선수 이름을 입력하면 🔥 레전드 하이라이트와 성향을 알려드려요!
""")

player = st.text_input(
    "✍️ 축구선수 이름 입력",
    placeholder="예: 메시, 호날두, 손흥민"
).strip()

if st.button("🎬 하이라이트 추천받기"):
    if player in players:
        data = players[player]

        st.balloons()

        st.success("추천 결과가 나왔어요! 🎉")

        st.markdown(f"""
# {data['emoji']} {player}

## 🎥 대표 하이라이트
### 🔥 {data['highlight']}

---

## 🧠 성향 분석
{data['personality']}

---

### ⚽ 한 줄 평가
**{player}는 축구 역사에 이름을 남긴 특별한 선수입니다!**
""")

    else:
        st.error("❌ 데이터에 없는 선수입니다.")
        st.info("현재 지원: 메시, 호날두, 음바페, 네이마르, 손흥민, 홀란드")

st.markdown("---")
st.caption("⚽ Football Highlight Finder | Made with Streamlit")
