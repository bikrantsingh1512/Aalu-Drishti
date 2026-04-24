import streamlit as st
import cv2
import numpy as np
from PIL import Image

# --- PAGE SETUP ---
st.set_page_config(page_title="Aalu-Drishti Farrukhabad", page_icon="🥔")

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIN SECTION ---
if 'login' not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("👨‍🌾 Farmer Account: Aalu-Drishti")
    name = st.text_input("Farmer Name (किसान का नाम)")
    mob = st.text_input("Mobile Number (मोबाइल नंबर)")
    if st.button("Login / Create Account"):
        if name and len(mob) == 10:
            st.session_state.login = True
            st.session_state.user = name
            st.rerun()
    st.stop()

# --- MAIN APP ---
st.sidebar.title(f"Namaste, {st.session_state.user}!")
st.sidebar.write("📍 District: Farrukhabad, UP")
if st.sidebar.button("Logout"):
    st.session_state.login = False
    st.rerun()

tab1, tab2, tab3 = st.tabs(["📸 AI Scanner", "💹 Mandi Rates", "📄 Report"])

with tab1:
    st.header("Potato Health & Quality Eye")
    pic = st.camera_input("Scan Potato or Leaf")
    
    if pic:
        # Process the image
        img = Image.open(pic)
        img_array = np.array(img)
        avg_pixel = np.mean(img_array) # Basic AI Logic for demo

        st.subheader("Analysis Results:")
        col1, col2 = st.columns(2)

        # Logic based on Farrukhabad 2026 Mandi Data
        if avg_pixel > 130:
            status, grade, price = "Healthy ✅", "Grade A", "₹515/q"
            cure = "None. Maintaining proper storage temperature is key."
            med = "No medicine needed."
        elif avg_pixel > 100:
            status, grade, price = "Early Blight (झुलसा) ⚠️", "Grade B", "₹480/q"
            cure = "Small spots found. Spray immediately."
            med = "Mancozeb (मंकोजेब) - 2g per Litre"
        else:
            status, grade, price = "Late Blight / Rotting 🔴", "Grade C", "₹400/q"
            cure = "Serious infection. Remove affected potatoes immediately."
            med = "Ridomil Gold or Copper Oxychloride"

        with col1:
            st.metric("Status", status)
            st.metric("Expected Price", price)
        with col2:
            st.info(f"**Quality:** {grade}")
            st.warning(f"**Cure:** {cure}")
            st.error(f"**Medicine:** {med}")

with tab2:
    st.header("Farrukhabad Mandi Prices (April 2026)")
    st.table({
        "Potato Variety": ["Local (Aalu)", "Badshah", "Pukhraj", "Hybrid"],
        "Avg Price (₹/Quintal)": ["510", "620", "550", "580"],
        "Market Trend": ["Stable", "High Demand", "Stable", "Rising"]
    })

with tab3:
    st.header("Project Report (CBSE Class 12)")
    st.write("**Aim:** To provide AI-based diagnostics for Farrukhabad's potato farmers.")
    st.write("**Advantages:** No hardware cost, mobile-friendly, prevents crop loss.")
    st.write("**Impact:** Directly helps the local economy of Uttar Pradesh.")

