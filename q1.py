import streamlit as st
import requests
from pathlib import Path

st.title("Botnoi Voice API Demo")
API_URL = "https://api-voice.botnoi.ai/openapi/v1/generate_audio"
API_TOKEN = "RtR9GUvxybl8g6iJo3G9BN49Q92fcIbb"


text_input = st.text_input("ข้อความที่ต้องการแปลงเป็นเสียง", "สวัสดีชาวโลก")
speaker_id = st.text_input("Speaker ID", "1")
generate_btn = st.button("Generate Voice")

if generate_btn:
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
