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
  
  payload = {
        "text": text_input,
        "speaker": speaker_id,
        "volume": 1,
        "speed": 1,
        "type_media": "mp3",
        "save_file": "true",
        "language": "th",
        "page": "user"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "botnoi-token": API_TOKEN
    }

    try:
        res = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        res.raise_for_status()
        data = res.json()
        st.write("API Response:", data)

        # ดึง URL ไฟล์เสียง
        audio_url = (
            data.get("url")
            or data.get("audio_url")
            or (data.get("data") or {}).get("url")
        )

        if audio_url:
            audio_bytes = requests.get(audio_url, timeout=30).content
            out_path = Path("botnoi_voice.mp3")
            out_path.write_bytes(audio_bytes)
            st.success(f"✅ บันทึกเสียงเรียบร้อย → {out_path.resolve()}")
            st.audio(audio_bytes, format="audio/mp3")
        else:
            st.error("ไม่พบลิงก์ไฟล์เสียงใน response")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาด: {e}")



