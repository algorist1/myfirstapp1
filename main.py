import streamlit as st
import pandas as pd
import altair as alt

# 📂 CSV 파일을 같은 디렉토리에서 직접 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 🎯 페이지 구성
st.set_page_config(page_title="국가별 MBTI 분석", page_icon="🌐", layout="centered")
st.title("🌍 국가별 MBTI 상위 유형 분석")
st.markdown("특정 국가에서 많이 나타나는 **MBTI 상위 3개 유형**을 시각화해볼 수 있어요!")

# 🧭 사용자 국가 선택
country_list = df['Country'].unique().tolist()
selected_countries = st.multiselect("📌 국가를 선택하세요 (최대 5개)", country_list, default=["South Korea", "United States"])

# 🔎 상위 3개 유형 추출 함수
def get_top3(df, countries):
    top3_records = []
    for country in countries:
        row = df[df['Country'] == country].iloc[0]
        mbti_scores = row.drop('Country')
        top3 = mbti_scores.sort_values(ascending=False).head(3)
        for mbti, score in top3.items():
            top3_records.append({
                'Country': country,
                'MBTI': mbti,
                'Score': score
            })
    return pd.DataFrame(top3_records)

# 📊 시각화
if selected_countries:
    top3_df = get_top3(df, selected_countries)

    chart = alt.Chart(top3_df).mark_bar().encode(
        x=alt.X('MBTI:N', title='MBTI 유형'),
        y=alt.Y('Score:Q', title='비율'),
        color='MBTI:N',
        column=alt.Column('Country:N', title='국가', spacing=15)
    ).properties(
        width=130,
        height=300,
        title='국가별 MBTI TOP 3'
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("👈 분석할 국가를 하나 이상 선택해주세요.")
