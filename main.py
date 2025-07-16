import streamlit as st

# 포켓몬 이미지와 설명이 포함된 MBTI 매핑 딕셔너리
mbti_pokemon_data = {
    'INTJ': {
        'name': '뮤츠',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png',
        'desc': '전략적이고 냉철한 INTJ에겐 초능력 포켓몬 뮤츠가 어울려요.'
    },
    'INTP': {
        'name': '야도킹',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/199.png',
        'desc': '독창적이고 분석적인 INTP에겐 신비로운 야도킹이 잘 맞아요.'
    },
    'ENTJ': {
        'name': '리자몽',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png',
        'desc': '강한 리더십을 가진 ENTJ에게는 열정 넘치는 리자몽이 딱이죠.'
    },
    'ENTP': {
        'name': '피카츄',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png',
        'desc': '활발하고 창의적인 ENTP에게는 귀엽고 재치 있는 피카츄가 어울려요.'
    },
    'INFJ': {
        'name': '에브이',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png',
        'desc': '이상과 비전을 중시하는 INFJ에겐 다양한 가능성의 에브이가 잘 어울려요.'
    },
    'INFP': {
        'name': '이브이',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png',
        'desc': '상상력이 풍부한 INFP는 변화무쌍한 이브이와 찰떡궁합!'
    },
    'ENFJ': {
        'name': '루카리오',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/448.png',
        'desc': '사람을 이끄는 힘을 지닌 ENFJ는 정의로운 루카리오와 잘 어울려요.'
    },
    'ENFP': {
        'name': '피츄',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/172.png',
        'desc': '밝고 다정한 ENFP는 귀엽고 사랑스러운 피츄와 완벽한 조합이에요.'
    },
    'ISTJ': {
        'name': '팬텀',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/093.png',
        'desc': '신중하고 책임감 강한 ISTJ는 조용한 카리스마의 팬텀이 어울려요.'
    },
    'ISFJ': {
        'name': '푸린',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png',
        'desc': '따뜻하고 섬세한 ISFJ는 포근한 푸린과 잘 어울려요.'
    },
    'ESTJ': {
        'name': '갸라도스',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png',
        'desc': '결단력 있는 ESTJ에겐 강렬한 포스를 가진 갸라도스가 찰떡이에요.'
    },
    'ESFJ': {
        'name': '파이리',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png',
        'desc': '사교적이고 친근한 ESFJ는 누구에게나 사랑받는 파이리가 잘 어울려요.'
    },
    'ISTP': {
        'name': '다크펫',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/359.png',
        'desc': '논리적이고 관찰력 좋은 ISTP는 쿨한 다크펫과 잘 맞아요.'
    },
    'ISFP': {
        'name': '이상해씨',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png',
        'desc': '조용하지만 감수성 풍부한 ISFP는 따뜻한 이상해씨와 잘 어울려요.'
    },
    'ESTP': {
        'name': '라이츄',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/026.png',
        'desc': '활동적이고 재치 있는 ESTP는 에너지 넘치는 라이츄와 궁합 최고!'
    },
    'ESFP': {
        'name': '꼬부기',
        'img_url': 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png',
        'desc': '재미있고 친화력 있는 ESFP는 귀엽고 명랑한 꼬부기와 잘 어울려요.'
    },
}

# 페이지 설정
st.set_page_config(page_title="MBTI x 포켓몬", page_icon="🐾", layout="centered")

# 헤더
st.title("🐾 MBTI에 어울리는 포켓몬 추천기")
st.write("당신의 성격 유형에 딱 맞는 포켓몬 친구를 찾아보세요!")

# 드롭다운으로 MBTI 선택
mbti_list = list(mbti_pokemon_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 버튼 누르면 결과 표시
if st.button("포켓몬 추천받기"):
    data = mbti_pokemon_data[selected_mbti]
    st.markdown(f"## 🎉 추천 포켓몬: {data['name']} 🎉")
    st.image(data['img_url'], caption=f"{data['name']} (for {selected_mbti})", use_column_width=True)
    st.markdown(f"📝 {data['desc']}")
