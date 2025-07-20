import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Replace this with your real Stability AI API key
API_KEY = "sk-hoj2Vs052934motGmBmOGY3IfBQzbz43p7vehZgLng6D1a5M"

# API Endpoint for Image-to-Image generation (Stable Diffusion)
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Streamlit App
st.set_page_config(page_title="AI Emotion Avatar Generator", page_icon="😊")
st.title("😊 AI Avatar Emotion Changer")
st.write("Upload your photo, pick an emotion, and AI will generate your new photo!")

# Upload Image
uploaded_image = st.file_uploader("📤 Upload your photo (face image)", type=["png", "jpg", "jpeg"])

# Select Emotion
emotions = ["Happy", "Sad", "Angry", "Surprised", "Neutral"]
selected_emotion = st.selectbox("😃 Pick an Emotion", emotions)

# Generate Button
if st.button("✨ Generate My New Avatar"):
    if uploaded_image and selected_emotion:
        st.info("AI is working... please wait ⏳")

        # Prepare API request
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "image/png"
        }

        # Prompt based on selected emotion
        prompt = f"A photorealistic portrait, person looking {selected_emotion.lower()}, keep the face same, clear expression"

        # Prepare multipart/form-data
        files = {
            "prompt": (None, prompt),
            "init_image": (uploaded_image.name, uploaded_image, uploaded_image.type),
            "output_format": (None, "png"),
        }

        # Make API request
        response = requests.post(API_URL, headers=headers, files=files)

        # Handle API response
        if response.status_code == 200:
            result_image = Image.open(BytesIO(response.content))
            st.image(result_image, caption=f"🎉 Your {selected_emotion} Avatar!")

            st.download_button(
                label="📥 Download Image",
                data=response.content,
                file_name="ai_avatar.png",
                mime="image/png"
            )
        else:
            st.error(f"❌ Failed to generate image. Status Code: {response.status_code}")
            st.json(response.json())
    else:
        st.warning("Please upload an image and select an emotion.")

st.caption("Made with ❤️ using Stability AI & Streamlit")
