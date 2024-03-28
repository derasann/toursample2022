import pandas as pd
import streamlit as st

st.write("2022年の販売ツアー数：8月〜12月のデータ")

# データをDataFrameに読み込む
df = pd.read_csv("tour_data.csv")

# 市町を選択するドロップダウンメニューを作成
city = st.selectbox("市町を選択", df['市町'].unique())

# 選択された市町に基づきデータを絞り込む
filtered_df = df[df['市町'] == city]

# 絞り込んだデータを表示
st.write(filtered_df)

# 絞り込んだデータのツアー数を合計
total_tours = filtered_df['販売ツアー数'].sum()

# 合計ツアー数を表示
st.write(f"選択された市町 ({city}) の合計ツアー数: {total_tours}")
