import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Replace with your Stability AI API key
API_KEY = "sk-hoj2Vs052934motGmBmOGY3IfBQzbz43p7vehZgLng6D1a5M"

# Stability AI Image-to-Image Endpoint
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Set Streamlit Page
st.set_page_config(page_title="Image-to-Image Generator", page_icon="🎨")
st.title("🎨 AI Image-to-Image Generator using Stability AI")
st.write("Upload an image and let AI transform it!")

# File uploader
uploaded_image = st.file_uploader("📤 Upload your image (JPG/PNG):", type=["jpg", "jpeg", "png"])

# Prompt box
prompt = st.text_input("📝 Describe how AI should modify your image:")

# Generate Button
if st.button("✨ Generate Image"):
    if uploaded_image and prompt.strip():
        st.info("Please wait... AI is transforming your image!")

        # Read image bytes
        image_bytes = uploaded_image.read()

        # Headers (Important: Accept must be image/*)
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "image/*",                    # ✅ FIXED Accept Header
        }

        # Payload as multipart/form-data
        files = {
            'image': ('image.png', image_bytes, 'image/png'),
            'prompt': (None, prompt),
            'output_format': (None, 'png')
        }

        # Make API request
        response = requests.post(API_URL, headers=headers, files=files)

        # Handle API Response
        if response.status_code == 200:
            result_image = Image.open(BytesIO(response.content))
            st.image(result_image, caption="🎉 AI-generated image!", use_column_width=True)
            st.download_button("📥 Download Image", response.content, file_name="ai_image.png", mime="image/png")
        else:
            st.error(f"❌ Failed to generate image. Status Code: {response.status_code}")
            try:
                st.json(response.json())
            except:
                st.text(response.text)
    else:
        st.warning("Please upload an image and enter a description!")

# Footer
st.caption("Made with ❤️ using Stability AI and Streamlit")
