import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "INTJ": ("뮤츠", "🧠", "전략적이고 독립적인 천재형. 깊게 생각하고 목표를 향해 묵묵히 나아가요."),
    "INTP": ("후딘", "🔮", "호기심이 많고 분석을 좋아하는 아이디어 뱅크예요."),
    "ENTJ": ("리자몽", "🔥", "강한 리더십과 추진력을 가진 카리스마형이에요."),
    "ENTP": ("팬텀", "👻", "재치 있고 창의적이며 새로운 도전을 즐겨요."),
    "INFJ": ("루기아", "🌊", "조용하지만 깊은 통찰력을 가진 이상주의자예요."),
    "INFP": ("이브이", "🌈", "상상력이 풍부하고 따뜻한 감성을 지녔어요."),
    "ENFJ": ("피카츄", "⚡", "사람들을 밝게 만드는 인기만점 리더예요."),
    "ENFP": ("뮤", "✨", "자유롭고 호기심 넘치는 모험가예요."),
    "ISTJ": ("거북왕", "🐢", "책임감이 강하고 믿음직한 성격이에요."),
    "ISFJ": ("해피너스", "💖", "배려심이 많고 주변 사람들을 잘 챙겨요."),
    "ESTJ": ("보스로라", "🛡️", "체계적이고 든든한 관리자 스타일이에요."),
    "ESFJ": ("파르토", "🎉", "친화력이 좋고 사람들과 함께하는 걸 좋아해요."),
    "ISTP": ("루카리오", "🥋", "냉철하고 실용적인 문제 해결사예요."),
    "ISFP": ("나인테일", "🦊", "감성이 풍부하고 자신만의 개성이 뚜렷해요."),
    "ESTP": ("인파이트몽", "💥", "에너지 넘치고 행동력이 뛰어난 타입이에요."),
    "ESFP": ("푸린", "🎤", "분위기 메이커! 즐거움을 나누는 걸 좋아해요.")
}

st.title("⚡ MBTI 포켓몬 추천기")
st.markdown("---")

st.markdown(
    """
    ### 🎮 나와 가장 잘 어울리는 포켓몬은?
    MBTI를 입력하면 어울리는 포켓몬과 성향을 알려드려요!
    """
)

mbti = st.text_input(
    "📝 MBTI를 입력하세요 (예: INFP)",
    max_chars=4
).upper()

if st.button("🔍 포켓몬 추천받기"):
    if mbti in pokemon_data:
        pokemon, emoji, desc = pokemon_data[mbti]

        st.balloons()

        st.success("추천 결과가 나왔어요! 🎉")

        st.markdown(
            f"""
            ## {emoji} 당신과 가장 잘 어울리는 포켓몬!

            # 🎯 **{pokemon}**

            ### 💡 성향
            {desc}

            ---
            ### 🌟 한 줄 요약
            **{mbti} + {pokemon} = 최고의 조합!**
            """
        )

    else:
        st.error("❌ 올바른 MBTI를 입력해주세요! (예: ENFP, ISTJ)")
        st.info("가능한 MBTI는 16가지 유형만 입력할 수 있어요.")

st.markdown("---")
st.caption("⚡ Made with Streamlit | MBTI Pokémon Finder")
