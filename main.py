import streamlit as st
import time

st.title("streamlit 超入門")

st.write("プログレスバーの表示")
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expander1 = st.expander("問い合わせ1")
expander1.write("1の問い合わせに関する回答")
expander2 = st.expander("問い合わせ2")
expander2.write("2の問い合わせに関する回答")
expander3 = st.expander("問い合わせ3")
expander3.write("3の問い合わせに関する回答")

