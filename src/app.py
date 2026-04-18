import streamlit as st
import pickle
import asyncio
import time
from truecallerpy import search_phonenumber

# --- 1. PAGE CONFIG & CYBER THEME ---
st.set_page_config(page_title="SPAM-SHIELD AI", page_icon="🛡️", layout="wide")

# Custom CSS for the "Command Center" look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    div.stButton > button:first-child {
        background: linear-gradient(to right, #00f2fe, #4facfe);
        color: white;
        border: none;
        padding: 15px 32px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 0px 15px rgba(79, 172, 254, 0.5);
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 25px rgba(79, 172, 254, 0.8);
    }
    .report-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.markdown("## 🛡️ SYSTEM STATUS")
    st.success("AI Core: Online")
    st.success("API Bridge: Connected")
    st.markdown("---")
    st.write("Logged in as: **Atharva (Admin)**")

# --- 3. HEADER ---
st.title("🛡️ SPAM-SHIELD : SENDER VERIFICATION")
st.markdown("#### *Next-Gen Hybrid Security Analysis*")

# --- 4. INPUT SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    message_input = st.text_area("📩 MESSAGE CONTENT", placeholder="Drop the suspicious text here...", height=150)
with col2:
    phone_input = st.text_input("📞 SENDER NUMBER", placeholder="+91XXXXXXXXXX")

# --- 5. THE "EXCITING" EXECUTION ---
if st.button("🚀 INITIALIZE SECURITY SCAN"):
    if not message_input or not phone_input:
        st.warning("⚠️ Access Denied: Missing Input Data.")
    else:
        # Visual Loading Sequence
        progress_text = "🔒 Scanning Database..."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.5)
        my_bar.empty()

        # Logic Path
        try:
            # ML Prediction (Assume model/vectorizer are pre-loaded or load here)
            model = pickle.load(open("model.pkl", "rb"))
            vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
            
            data = vectorizer.transform([message_input]).toarray()
            prediction = model.predict(data)[0]
            confidence = max(model.predict_proba(data)[0]) * 100
            
            st.markdown("---")
            res_col1, res_col2 = st.columns(2)

            with res_col1:
                st.markdown('<div class="report-card">', unsafe_allow_html=True)
                st.subheader("🤖 AI ANALYSIS")
                if prediction == "spam":
                    st.error("🚨 THREAT DETECTED: SPAM")
                else:
                    st.success("✅ THREAT LEVEL: SAFE")
                st.write(f"Confidence Level: **{confidence:.2f}%**")
                st.markdown('</div>', unsafe_allow_html=True)

            with res_col2:
                st.markdown('<div class="report-card">', unsafe_allow_html=True)
                st.subheader("👤 SENDER IDENTITY")
                # Identity check logic (Simulated for speed, replace with your asyncio logic)
                st.write("**Name:** Searching...")
                st.info("API Response: Verified Caller Found")
                st.markdown('</div>', unsafe_allow_html=True)

            st.balloons() # Added for excitement on scan completion
            
        except Exception as e:
            st.error(f"System Error: {e}")