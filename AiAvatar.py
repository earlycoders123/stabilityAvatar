import streamlit as st
from TTS.api import TTS

# Load the TTS model (this may take some time when first run)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

# Streamlit UI
st.set_page_config(page_title="🎙️ AI Text to Speech Tool")
st.title("🎙️ AI Text-to-Speech Generator")
st.write("Type your sentence and listen!")

# Text input
text = st.text_input("📝 Enter your text:")

# Generate speech button
if st.button("🎧 Generate Speech"):
    if text.strip():
        with st.spinner("Generating speech..."):
            # Save the output audio
            tts.tts_to_file(text=text, file_path="output.wav")
            audio_file = open("output.wav", "rb")
            st.audio(audio_file.read(), format="audio/wav")
            st.success("✅ Speech generated!")
    else:
        st.warning("Please enter some text.")
