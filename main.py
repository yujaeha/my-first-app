import streamlit as st

st.set_page_config(
    page_title="⚽ 축구선수 추천기",
    page_icon="⚽",
    layout="centered"
)

players = {
    "메시": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Lionel_Messi_20180626.jpg",
        "video": "https://www.youtube.com/watch?v=RM_5tJncHww",
        "highlight": "2015 바이에른 뮌헨전 보아텡 드리블 골",
        "personality": "천재형 플레이메이커 🧠",
        "stats": {
            "드리블": 5,
            "패스": 5,
            "슛": 5,
            "스피드": 4,
            "리더십": 5
        }
    },

    "호날두": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg",
        "video": "https://www.youtube.com/watch?v=OUKGsb8CpF8",
        "highlight": "유벤투스전 오버헤드킥",
        "personality": "노력형 승부사 🚀",
        "stats": {
            "드리블": 4,
            "패스": 4,
            "슛": 5,
            "스피드": 5,
            "리더십": 5
        }
    },

    "손흥민": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Son_Heung-min_2022.jpg",
        "video": "https://www.youtube.com/watch?v=1kLytk8PqKQ",
        "highlight": "번리전 70m 원더골",
        "personality": "겸손한 리더 🇰🇷",
        "stats": {
            "드리블": 4,
            "패스": 4,
            "슛": 5,
            "스피드": 5,
            "리더십": 5
        }
    },

    "음바페": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Kylian_Mbappe_2022.jpg",
        "video": "https://www.youtube.com/watch?v=R3jK6Vw7zM4",
        "highlight": "2022 월드컵 결승 해트트릭",
        "personality": "초고속 공격수 ⚡",
        "stats": {
            "드리블": 5,
            "패스": 4,
            "슛": 5,
            "스피드": 5,
            "리더십": 4
        }
    },

    "네이마르": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Neymar_2018.jpg",
        "video": "https://www.youtube.com/watch?v=Z3J_MCbwaJ0",
        "highlight": "산투스 시절 원더골",
        "personality": "예술가형 드리블러 🎭",
        "stats": {
            "드리블": 5,
            "패스": 4,
            "슛": 4,
            "스피드": 5,
            "리더십": 3
        }
    },

    "홀란드": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Erling_Haaland_2023.jpg",
        "video": "https://www.youtube.com/watch?v=1z4n8XGxG7Y",
        "highlight": "맨시티 데뷔 시즌 대폭발",
        "personality": "괴물 스트라이커 🦁",
        "stats": {
            "드리블": 4,
            "패스": 3,
            "슛": 5,
            "스피드": 5,
            "리더십": 4
        }
    }
}

st.title("⚽ 축구선수 하이라이트 추천기")
st.markdown("### 🌟 좋아하는 축구선수를 입력해보세요!")

player = st.text_input(
    "✍️ 선수 이름 입력",
    placeholder="메시, 호날두, 손흥민, 음바페..."
).strip()

if st.button("🎥 하이라이트 보기"):
    if player in players:

        st.balloons()

        data = players[player]

        st.success(f"🎉 {player} 분석 완료!")

        st.image(data["image"], use_container_width=True)

        st.markdown("---")

        st.subheader("🔥 대표 하이라이트")
        st.info(data["highlight"])

        st.video(data["video"])

        st.markdown("---")

        st.subheader("🧠 선수 성향")
        st.write(data["personality"])

        st.markdown("---")

        st.subheader("⭐ 능력치")

        for stat, value in data["stats"].items():
            st.write(f"{stat} : {'⭐' * value}")

        st.markdown("---")

        st.success(
            f"⚽ 당신에게 추천하는 하이라이트는 '{data['highlight']}' 입니다!"
        )

    else:
        st.error("❌ 지원하지 않는 선수입니다.")
        st.info("현재 지원 선수: 메시, 호날두, 손흥민, 음바페, 네이마르, 홀란드")

st.markdown("---")
st.caption("⚽ Football Highlight Recommender")
