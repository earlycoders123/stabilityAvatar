import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Replace with your actual Stability AI API Key
API_KEY = "sk-hoj2Vs052934motGmBmOGY3IfBQzbz43p7vehZgLng6D1a5M"

# Stability AI Image-to-Image endpoint
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Streamlit App
st.title("🖼️ AI Image to Pencil Sketch Generator")
st.write("Upload a photo and AI will convert it into a pencil sketch!")

# Upload image
uploaded_image = st.file_uploader("📤 Upload your image here", type=["jpg", "jpeg", "png"])

# Generate Button
if uploaded_image and st.button("🎨 Convert to Pencil Sketch"):
    st.info("Generating your AI pencil sketch... Please wait!")

    # Headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "image/*"
    }

    # Prompt for transformation
    prompt = "Transform this image into a realistic pencil sketch."

    # Files for multipart/form-data
    files = {
        'mode': (None, 'image-to-image'),
        'prompt': (None, prompt),
        'strength': (None, '0.6'),  # Adjust strength as needed
        'output_format': (None, 'png'),
        'image': ('uploaded_image.png', uploaded_image, 'image/png')
    }

    # API Request
    response = requests.post(API_URL, headers=headers, files=files)

    # Handle API Response
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="🎉 Here’s your AI Pencil Sketch!")

        st.download_button(
            "📥 Download Sketch",
            response.content,
            "pencil_sketch.png",
            "image/png"
        )
    else:
        st.error("❌ Failed to generate image.")
        try:
            st.json(response.json())
        except:
            st.write(response.content)

st.caption("Made with ❤️ using Stability AI and Streamlit")
