import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 3D 소득 분포 시각화")

# CSV 불러오기
df = pd.read_csv("data/adult.csv")

# 소득을 숫자로 변환
df["income_num"] = df["income"].apply(lambda x: 1 if ">50K" in x else 0)

# 필요한 열 선택
df_clean = df[["age", "hours-per-week", "income_num"]].dropna()

# 3D 산점도
fig = px.scatter_3d(
    df_clean,
    x="age",
    y="hours-per-week",
    z="income_num",
    color="income_num",
    title="나이 vs 근무시간 vs 소득수준 (3D 시각화)",
    labels={"income_num": "소득"},
)

st.plotly_chart(fig)
