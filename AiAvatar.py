# Homework Helper Squad using Gemini + Streamlit
import streamlit as st
import google.generativeai as genai

# Set Gemini API Key (store in st.secrets in production)
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")

# Load Gemini Model
model = genai.GenerativeModel('gemini-2.5-pro')

# Streamlit App UI
st.set_page_config(page_title="Homework Helper Squad", page_icon="📚")
st.title("📚 Homework Helper Squad - AI Friends to Help You!")

# Sidebar for choosing agents
agent = st.sidebar.radio("Pick Your Helper Agent:", 
                         ("🧮 Math Agent", "📝 Grammar Agent", "💡 Explainer Agent"))

# Agent Workflows
if agent == "🧮 Math Agent":
    st.subheader("Math Agent 🤖")
    question = st.text_input("Enter your math question:")
    if st.button("Ask Math Agent"):
        if question.strip():
            prompt = f"Explain and solve this math problem for a child: {question}"
            response = model.generate_content(prompt)
            st.success(response.text)
        else:
            st.warning("Please type a math problem.")

elif agent == "📝 Grammar Agent":
    st.subheader("Grammar Agent ✍️")
    text = st.text_area("Paste your sentence or paragraph here:")
    if st.button("Check Grammar"):
        if text.strip():
            prompt = f"Check grammar and spelling in this text, and explain corrections simply: {text}"
            response = model.generate_content(prompt)
            st.success(response.text)
        else:
            st.warning("Please paste something for checking.")

elif agent == "💡 Explainer Agent":
    st.subheader("Explainer Agent 💡")
    topic = st.text_input("What should I explain?")
    if st.button("Explain It Simply"):
        if topic.strip():
            prompt = f"Explain this topic in simple words for a 10-year-old kid: {topic}"
            response = model.generate_content(prompt)
            st.success(response.text)
        else:
            st.warning("Please enter a topic to explain.")

# Footer
st.caption("Made with ❤️ using Gemini AI")
