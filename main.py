import streamlit as st

# 포켓몬 데이터: MBTI - 이름, 이미지 URL, 설명, 진로/직업
mbti_pokemon_data = {
    'INTJ': {
        'name': '뮤츠',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png',
        'desc': '전략적이고 냉철한 INTJ에겐 초능력 포켓몬 뮤츠가 어울려요.',
        'career': '🧠 연구자 또는 AI전문가 스타일!'
    },
    'INTP': {
        'name': '야도킹',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/199.png',
        'desc': '아이디어가 풍부하고 분석적인 INTP는 엉뚱하지만 지적인 야도킹과 찰떡이에요.',
        'career': '🔬 발명가, 이론물리학자 스타일!'
    },
    'ENTJ': {
        'name': '리자몽',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png',
        'desc': '카리스마와 추진력을 갖춘 ENTJ에게는 불꽃 리더, 리자몽이 딱!',
        'career': '💼 CEO, 전략 컨설턴트 스타일!'
    },
    'ENTP': {
        'name': '피카츄',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png',
        'desc': '재치 있고 에너지 넘치는 ENTP는 호기심 많은 피카츄와 찰떡궁합!',
        'career': '🎤 방송인, 마케터 스타일!'
    },
    'INFJ': {
        'name': '에브이',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png',
        'desc': '이상과 비전을 추구하는 INFJ는 변화무쌍한 가능성의 에브이와 잘 맞아요.',
        'career': '📚 작가, 상담가 스타일!'
    },
    'INFP': {
        'name': '이브이',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png',
        'desc': '상상력과 감수성 넘치는 INFP는 따뜻한 이브이와 찰떡궁합!',
        'career': '🎨 예술가, 애니메이터 스타일!'
    },
    'ENFJ': {
        'name': '루카리오',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/448.png',
        'desc': '사람을 이끄는 리더십의 ENFJ는 정의로운 루카리오와 궁합 최고!',
        'career': '🏛️ 교사, 코치 스타일!'
    },
    'ENFP': {
        'name': '피츄',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/172.png',
        'desc': '밝고 사랑스러운 ENFP는 귀엽고 엉뚱한 피츄와 딱 맞아요.',
        'career': '🎭 배우, 크리에이터 스타일!'
    },
    'ISTJ': {
        'name': '팬텀',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/093.png',
        'desc': '신중하고 책임감 강한 ISTJ는 조용한 카리스마의 팬텀과 잘 어울려요.',
        'career': '📊 회계사, 시스템 관리자 스타일!'
    },
    'ISFJ': {
        'name': '푸린',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png',
        'desc': '배려 깊고 따뜻한 ISFJ는 포근한 푸린과 찰떡궁합!',
        'career': '👩‍⚕️ 간호사, 보육 교사 스타일!'
    },
    'ESTJ': {
        'name': '갸라도스',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png',
        'desc': '강한 의지와 조직력을 지닌 ESTJ는 파워 넘치는 갸라도스가 어울려요.',
        'career': '🏗️ 공무원, 프로젝트 매니저 스타일!'
    },
    'ESFJ': {
        'name': '파이리',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png',
        'desc': '따뜻하고 친근한 ESFJ는 밝은 에너지의 파이리와 찰떡이에요.',
        'career': '👩‍🏫 선생님, 서비스직 스타일!'
    },
    'ISTP': {
        'name': '다크펫',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/359.png',
        'desc': '논리적이고 쿨한 ISTP는 미스터리한 다크펫이 어울려요.',
        'career': '🧰 엔지니어, 보안 전문가 스타일!'
    },
    'ISFP': {
        'name': '이상해씨',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png',
        'desc': '감성적이고 자연을 사랑하는 ISFP는 따뜻한 이상해씨와 잘 맞아요.',
        'career': '🌱 플로리스트, 디자이너 스타일!'
    },
    'ESTP': {
        'name': '라이츄',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/026.png',
        'desc': '모험심 강하고 즉흥적인 ESTP는 스피드감 넘치는 라이츄가 찰떡!',
        'career': '🏎️ 스포츠 선수, 세일즈 전문가 스타일!'
    },
    'ESFP': {
        'name': '꼬부기',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png',
        'desc': '즐겁고 장난기 많은 ESFP는 귀염둥이 꼬부기와 찰떡이에요.',
        'career': '🎈 이벤트 플래너, 무대연출가 스타일!'
    },
}

# 페이지 설정
st.set_page_config(page_title="MBTI x 포켓몬", page_icon="🌟", layout="centered")

# 타이틀 및 설명
st.title("🎉 MBTI로 알아보는 나의 포켓몬 친구")
st.write("당신의 성격과 어울리는 포켓몬을 찾아볼까요?\n직업 상상력도 함께 느껴보세요! 👀")

# 드롭다운
selected_mbti = st.selectbox("📌 당신의 MBTI를 선택하세요", list(mbti_pokemon_data.keys()))

# 추천 버튼
if st.button("✨ 나와 어울리는 포켓몬 보기"):
    result = mbti_pokemon_data[selected_mbti]
    st.balloons()  # 🎈 풍선 효과
    st.markdown(f"## 🧬 {selected_mbti} 타입에게 어울리는 포켓몬은?")
    st.image(result['img_url'], caption=f"🌟 {result['name']} 🌟", use_column_width=True)
    st.markdown(f"**{result['desc']}**")
    st.markdown(f"💡 진로 상상력: **{result['career']}**")
