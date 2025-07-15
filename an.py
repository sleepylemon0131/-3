import pandas as pd
import plotly.express as px

# 데이터 로드
df = pd.read_csv("/mnt/data/unzipped/adult.csv")

# 범주형 income을 수치형으로 변환
df["income_num"] = df["income"].apply(lambda x: 1 if ">50K" in x else 0)

# 필요한 열만 선택
df_clean = df[["age", "hours-per-week", "income_num"]].dropna()

# 3D 산점도 시각화
fig = px.scatter_3d(
    df_clean,
    x="age",
    y="hours-per-week",
    z="income_num",
    color="income_num",
    labels={"income_num": "소득구간"},
    title="3D 소득 분포: 나이 vs 근무시간 vs 소득수준"
)

fig.show()
