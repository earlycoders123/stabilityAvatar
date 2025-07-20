import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Your Stability AI API Key (store securely)
API_KEY = "sk-hoj2Vs052934motGmBmOGY3IfBQzbz43p7vehZgLng6D1a5M"

# Stability AI Endpoint
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "image/*"
}

# Streamlit App
st.set_page_config(page_title="AI Image-to-Image Generator", page_icon="🎨")
st.title("🎨 AI Image-to-Image Generator Tool")
st.write("Upload your image and choose a style or transformation!")

# Upload Image
uploaded_image = st.file_uploader("📷 Upload an image:", type=["png", "jpg", "jpeg"])

# Choose Style / Transformation
style = st.selectbox("🎭 Choose transformation style:", [
    "Cartoon Style", "Sketch Drawing", "Oil Painting", "Happy Face", "Sad Face", "Fantasy Art"
])

# Generate Button
if st.button("✨ Generate Image"):
    if uploaded_image:
        prompt = f"Convert this image into {style.lower()}."

        files = {
            'mode': (None, 'image-to-image'),
            'prompt': (None, prompt),
            'strength': (None, '0.5'),
            'output_format': (None, 'png'),
            'image': ('input.png', uploaded_image, 'image/png')
        }

        with st.spinner("Generating your transformed image..."):
            response = requests.post(API_URL, headers=headers, files=files)

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption=f"Here’s your {style} image!")

                st.download_button(
                    "📥 Download Image",
                    data=response.content,
                    file_name="generated_image.png",
                    mime="image/png"
                )
            else:
                st.error(f"❌ Failed to generate image. Status Code: {response.status_code}")
                try:
                    st.json(response.json())
                except:
                    st.write(response.text)
    else:
        st.warning("Please upload an image first!")

st.caption("Made with ❤️ using Stability AI and Streamlit")
