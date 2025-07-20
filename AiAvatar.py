import streamlit as st
import requests
import os

# Set your Replicate API Key
REPLICATE_API_TOKEN = "r8_6Db0E6KufdDLrKOvzlysrnPrmmDeDGS478dlQ"
REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Streamlit App Setup
st.set_page_config(page_title="AI Image Transformer", page_icon="🎨")
st.title("🎨 AI Image-to-Image Transformer (Replicate API)")
st.write("Upload a photo and pick a style to transform your image!")

# Upload Image
uploaded_image = st.file_uploader("📤 Upload your image", type=["jpg", "png"])

# Style Selection
style_prompt = st.selectbox("🎭 Pick a style:", [
    "Pencil sketch",
    "Cartoon style",
    "Watercolor painting",
    "Black and white photo",
    "Oil painting",
    "Cyberpunk style"
])

# Transform Button
if st.button("✨ Transform Image") and uploaded_image:
    st.info("Processing your image... Please wait.")

    # Read image bytes
    image_bytes = uploaded_image.read()

    # Replicate API Request
    api_url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Example using SDXL model with image-to-image prompt
    # Replace 'stability-ai/sdxl' with any other model endpoint if desired
    data = {
        "version": "db21e45b19b363682f014aadf1d95cf06db2a769de110b6c94a98e72eb37b3c1",  # SDXL Image-to-Image Version
        "input": {
            "image": f"data:image/png;base64,{image_bytes.decode('latin1')}",
            "prompt": f"Transform this image into a {style_prompt.lower()}."
        }
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 201:
        output_url = response.json()["urls"]["get"]
        st.success("✅ Image generated! Fetching your result...")

        # Polling or directly display if available:
        st.image(output_url, caption=f"🎉 Transformed Image: {style_prompt}")

        st.write(f"[🔗 View Full Image]({output_url})")

    else:
        st.error(f"❌ Failed to transform image. Status Code: {response.status_code}")
        st.json(response.json())

else:
    st.warning("Please upload an image and pick a style.")

st.caption("Made with ❤️ using Replicate + Streamlit")
