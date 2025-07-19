import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Replace with your actual Stability AI API Key
API_KEY = "sk-MFaLzii2y0qn0Mf3Yyv1gOejEY9p3Go4sW1E9iUW91ccRjCn"

# Stability AI endpoint for image-to-image (SD3 variations)
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

st.set_page_config(page_title="AI Avatar Creator", page_icon="🎨")
st.title("🎨 AI Avatar Creator")
st.write("Upload a picture and AI will create a cartoon avatar!")

# Upload Image
uploaded_image = st.file_uploader("📤 Upload your photo (jpg/png):", type=["jpg", "jpeg", "png"])

# Prompt for stylization
style_prompt = st.text_input("🎨 Style (e.g., 'cartoon style', 'anime avatar')", value="cartoon style")

if st.button("✨ Generate Avatar"):
    if uploaded_image:
        st.info("Generating your AI Avatar... Please wait...")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "image/png"
        }

        files = {
            "init_image": uploaded_image,
            "prompt": (None, style_prompt),
            "output_format": (None, "png")
        }

        response = requests.post(API_URL, headers=headers, files=files)

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption="🎉 Your AI Avatar!")

            st.download_button(
                label="📥 Download Avatar",
                data=response.content,
                file_name="ai_avatar.png",
                mime="image/png"
            )
        else:
            st.error("❌ Avatar generation failed.")
            st.json(response.json())
    else:
        st.warning("Please upload a photo!")

st.caption("Made with ❤️ using Stability AI & Streamlit")
