from openai import OpenAI
def askAI(question):
    client = OpenAI(api_key="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")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content

import streamlit as st

import requests
from pathlib import Path

st.set_page_config(page_title='Body mass index : Web Application',page_icon='🦊')
st.title('Body mass index : Web Application')
st.balloons()
st.snow()


kg=st.number_input('น้ำหนัก (kg):')
cm=st.number_input('ส่วนสูง (cm):')

import io
if st.button('คำนวน') and cm > 10 and kg >10 :
  bmi = kg/((cm/100)**2)
  tt = f'ค่า BMI ของคุณคือ {bmi:.2f}'
  if bmi < 18.5:
    st.info(tt)
    st.image('b1.png')
    word = "น้ำหนักน้อยกว่าปกติ"

  elif bmi < 24.9:
    st.success(tt)
    st.image('b2.png')
    word = "น้ำหนักปกติ"

  elif bmi < 29.9:
    st.warning(tt)
    st.image('b3.png')
    word = "น้ำหนักเกิน"

  elif bmi < 39.9:
    st.warning(tt)
    st.image('b4.png')
    word = "โรคอ้วน"

  else:
    st.warning(tt)
    st.image('b5.png')
    word = "โรคอ้วนอันตราย"
  


 
  q=st.empty()
  q.write("กรุณารอสักครู่")
  question = f"โรคที่มีความเสี่ยงสูงที่สุด ถ้าค่าbmi={bmi}"
  q.write(askAI(question))
    

