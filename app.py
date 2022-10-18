import streamlit as st
import pandas as pd
from PIL import Image

with st.sidebar :
    gubun = st.radio("열람하고 싶은 결과를 선택하세요.", ("강력범죄간 상관관계", "토지 및 인구 관련 요인", "주민 유형", "치안 관련 요인", "건물 유형"))

if gubun == "강력범죄간 상관관계" :
    st.title("강력범죄간 상관관계")

elif gubun == "토지 및 인구 관련 요인" :
    st.title("토지 및 인구 관련 요인")
    t1, t2, t3 = st.tabs(["공시지가", "인구", "행정구역 면적"])

elif gubun == "주민 유형" :
    st.title("주민 유형")
    st.write("둠치기박치기3")

elif gubun == "치안 관련 요인" :
    st.title("치안 관련 요인")
    st.write("둠치기박치기4")

else :
    st.title("건물 유형")
    st.write("둠치기박치기5")