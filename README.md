import streamlit as st

st.set_page_config(page_title='Body mass index : Web Application',page_icon='🦊')
st.title('Body mass index : Web Application')
st.balloons()
st.snow()


kg=st.number_input('น้ำหนัก (kg):')
cm=st.number_input('ส่วนสูง (cm):')
from gtts import gTTS
import io
if st.button('คำนวน'):
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

  tts = gTTS(text=word, lang='th')
  mp3_fp = io.BytesIO()
  tts.write_to_fp(mp3_fp)
  mp3_fp.seek(0)
  st.audio(mp3_fp, format="audio/mp3")

col1,col2 = st.columns(2)
with col1:
 if st.button('song'):
  st.video('https://youtu.be/YPy1XSVcPtU?si=hdMut_ZwTMrRsntD')

with col2 :
  if st.button('video'):
    st.video('https://youtu.be/E_JjsVKWzm8?si=zUo9Foz9XfWnFCcn')
