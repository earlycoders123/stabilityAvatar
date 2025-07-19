import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Replace with your Stability AI API Key
API_KEY = "sk-MFaLzii2y0qn0Mf3Yyv1gOejEY9p3Go4sW1E9iUW91ccRjCn"

# API Endpoint (Image-to-Image)
API_URL = "https://api.stability.ai/v2beta/stable-image/image-to-image/sd3"

# Streamlit App
st.set_page_config(page_title="AI Avatar Maker", page_icon="🧑‍🎨")
st.title("🧑‍🎨 AI Avatar Maker")
st.write("Upload your photo and AI will turn it into a cartoon avatar!")

# Upload Image
uploaded_image = st.file_uploader("📤 Upload Your Image", type=["png", "jpg", "jpeg"])

# Text Prompt
prompt = st.text_input("📝 What style should AI apply? (Example: 'make a cartoon avatar')")

# Generate Button
if st.button("✨ Generate AI Avatar"):
    if uploaded_image and prompt.strip():
        st.info("Processing... Please wait.")

        # Prepare multipart form-data
        files = {
            'init_image': uploaded_image,
            'prompt': (None, prompt),
            'strength': (None, "0.7"),   # 0.1 = slight changes, 1.0 = strong changes
            'output_format': (None, 'png')
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "image/*"
        }

        # API Request
        response = requests.post(API_URL, headers=headers, files=files)

        # Handle Response
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption="🎉 Your AI Avatar is ready!")

            st.download_button(
                label="📥 Download Avatar",
                data=response.content,
                file_name="ai_avatar.png",
                mime="image/png"
            )
        else:
            st.error(f"❌ Failed to generate image. Status Code: {response.status_code}")
            try:
                st.json(response.json())
            except:
                st.write(response.text)
    else:
        st.warning("Please upload an image and enter a style prompt!")

st.caption("Made with ❤️ using Stability AI and Streamlit")
