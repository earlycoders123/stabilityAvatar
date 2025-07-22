import streamlit as st
from bark import SAMPLE_RATE, generate_audio
import numpy as np
import scipy.io.wavfile

st.set_page_config(page_title="🎙️ GenAI Text-to-Speech with Bark")
st.title("🎙️ Bark GenAI Text-to-Speech")
st.write("Type your sentence and listen! AI will generate human-like speech.")

# Text input
text = st.text_area("📝 Enter your text:")

# Generate speech button
if st.button("🎧 Generate Speech"):
    if text.strip():
        with st.spinner("AI is generating speech..."):
            audio_array = generate_audio(text)
            wav_file = "bark_output.wav"
            scipy.io.wavfile.write(wav_file, SAMPLE_RATE, audio_array)

            # Play audio
            st.audio(wav_file)

            # Download button
            with open(wav_file, "rb") as audio_file:
                st.download_button("📥 Download Speech", audio_file, file_name="speech.wav")

            st.success("✅ Done! Generated using Bark AI.")
    else:
        st.warning("Please enter some text!")
