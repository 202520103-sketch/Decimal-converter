# streamlit_base_converter.py
import streamlit as st

st.set_page_config(page_title="진수 변환기", layout="centered")

# 제목
st.title("🔄 진수 변환기")

# 설명
st.markdown("""
이 웹사이트는 다양한 진수를 서로 변환할 수 있는 도구입니다.  
사용 방법:
1. 변환하고 싶은 숫자를 입력하세요.
2. 입력한 숫자의 진수를 선택하세요.
3. 변환할 진수를 선택하세요.
4. 변환 버튼을 누르면 결과가 표시됩니다.
""")

# 사용자 입력
number_input = st.text_input("변환할 숫자를 입력하세요", "")
from_base = st.selectbox("입력 진수", options=[2, 8, 10, 16], index=2)
to_base = st.selectbox("출력 진수", options=[2, 8, 10, 16], index=0)

# 변환
if st.button("변환"):
    try:
        # 입력 숫자를 10진수로 변환
        decimal_number = int(number_input, from_base)
        
        # 원하는 진수로 변환
        if to_base == 2:
            result = bin(decimal_number)[2:]
        elif to_base == 8:
            result = oct(decimal_number)[2:]
        elif to_base == 10:
            result = str(decimal_number)
        elif to_base == 16:
            result = hex(decimal_number)[2:].upper()
        
        st.success(f"결과: {result}")
    except ValueError:
        st.error("입력 값이 올바른 숫자가 아닙니다.")
