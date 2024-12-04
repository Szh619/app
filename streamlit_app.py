import streamlit as st
import os

# 确定当前工作目录
current_dir = os.getcwd()

# Streamlit 应用部分
st.title("Average TI-acs (within 1 km) across Bay area census tracts")

# 添加下拉菜单选择年份
year = st.selectbox("Select year", options=range(2012, 2023), index=0)

# 指定图片路径

image_path = os.path.join(current_dir, "figure",  str (year) + 'L2_DCFC.jpg')

# 使用 st.image 显示
st.image(image_path, use_container_width=True)