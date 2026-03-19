import streamlit as st
import math
import numpy as np

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="🧮 Nisar's Scientific Calculator",
    page_icon="🧮",
    layout="wide"
)

# ---------------------------------
# PERFECT CSS - Clear Operations Text + Fixed Info Position
# ---------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Times+New+Roman:wght@400;500;600;700&family=Roboto:wght@400;500;700&display=swap');

/* Clean Theme */
.stApp {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 50%, #dee2e6 100%);
    color: #1a1a1a;
    font-family: 'Times New Roman', serif;
}

/* Cards */
.prof-card {
    background: #ffffff;
    border-radius: 18px;
    border: 2px solid #d1d9e0;
    padding: 2rem;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    margin: 1rem 0;
}

/* Title */
.prof-title {
    font-family: 'Times New Roman', serif;
    font-size: 2.8rem;
    font-weight: 700;
    color: #1a1a1a;
    text-align: center;
    margin: 0 0 1rem 0;
}

.subtitle {
    font-family: 'Roboto', sans-serif;
    font-size: 1.2rem;
    color: #495057;
    text-align: center;
    margin-bottom: 2rem;
}

/* Section Headers */
.section-title {
    font-family: 'Times New Roman', serif;
    font-size: 1.4rem;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 1.2rem;
    padding: 0.3rem 0;
    border-bottom: 3px solid #28a745;
}

/* NUMBER INPUT - Perfect Black Text */
.stNumberInput label {
    font-weight: 600 !important;
    color: #1a1a1a !important;
    font-size: 1rem !important;
}

.stNumberInput > div > div > div > div [data-baseweb="numberinput"] {
    background: #ffffff !important;
    border: 2px solid #28a745 !important;
    border-radius: 10px !important;
}

.stNumberInput input {
    color: #000000 !important;
    font-size: 1.3rem !important;
    font-weight: 600 !important;
    background: #ffffff !important;
}

/* SELECTBOX - WHITE BG + PURE BLACK TEXT FOR OPERATIONS */
.stSelectbox label {
    font-weight: 600 !important;
    color: #1a1a1a !important;
    font-size: 1rem !important;
}

.stSelectbox > div[data-baseweb="select"] {
    background: #ffffff !important;
    border: 3px solid #28a745 !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 12px rgba(40, 167, 69, 0.15) !important;
}

.stSelectbox > div[data-baseweb="select"] > div {
    background: #ffffff !important;
    color: #000000 !important;
}

.stSelectbox > div[data-baseweb="select"] * {
    color: #000000 !important;
    font-size: 1.2rem !important;
    font-weight: 600 !important;
    font-family: 'Roboto', sans-serif !important;
}

/* DROPDOWN OPTIONS - PURE BLACK TEXT + WHITE BG */
div[data-baseweb="popover"] {
    background: #ffffff !important;
    border: 2px solid #28a745 !important;
    border-radius: 10px !important;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
}

div[data-baseweb="popover"] ul {
    background: #ffffff !important;
}

div[data-baseweb="popover"] ul li {
    background: #ffffff !important;
    color: #000000 !important;
    font-size: 1.1rem !important;
    font-weight: 500 !important;
    padding: 0.8rem 1rem !important;
}

div[data-baseweb="popover"] ul li:hover {
    background: #f8f9fa !important;
    color: #000000 !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #28a745, #20c997) !important;
    border: none !important;
    border-radius: 12px !important;
    height: 3.2rem !important;
    font-size: 1.2rem !important;
    font-weight: 600 !important;
    color: #ffffff !important;
    box-shadow: 0 6px 20px rgba(40, 167, 69, 0.3) !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #20c997, #17a2b8) !important;
}

/* Result */
.result-section {
    background: linear-gradient(135deg, #d4edda, #c3e6cb);
    border: 3px solid #28a745;
    border-radius: 15px;
    padding: 1.8rem;
    text-align: center;
    box-shadow: 0 12px 35px rgba(40, 167, 69, 0.25);
}

.result-title {
    font-family: 'Times New Roman', serif;
    font-size: 1.4rem;
    font-weight: 600;
    color: #155724;
}

.result-value {
    font-family: 'Times New Roman', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #155724;
}

.result-equation {
    font-size: 1rem;
    color: #495057;
    font-style: italic;
}

/* History */
.history-item {
    background: #f8f9fa;
    border-left: 4px solid #28a745;
    padding: 0.8rem;
    margin: 0.4rem 0;
    border-radius: 6px;
    font-family: 'Roboto', sans-serif;
    font-size: 1rem;
    color: #1a1a1a;
}

/* Info message styling */
.stInfo figure {
    background: #fff3cd !important;
    border: 1px solid #ffeaa7 !important;
    border-radius: 8px !important;
    color: #856404 !important;
}

/* Nisar Card */
.nisar-card {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    border: 2px solid #dee2e6;
    border-radius: 15px;
    padding: 1.8rem;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
}

.nisar-name {
    font-family: 'Times New Roman', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #1a1a1a;
}

/* Hide empty spaces */
div[data-testid="stVerticalBlock"] > div:empty,
div[data-testid="stHorizontalBlock"] > div:empty,
.st-emotion-cache-1r4iq0w, .st-emotion-cache-1lbw5bz {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Session State
# ---------------------------------
if "history" not in st.session_state:
    st.session_state.history = []
if "result" not in st.session_state:
    st.session_state.result = None
if "expression" not in st.session_state:
    st.session_state.expression = ""

# ---------------------------------
# Header
# ---------------------------------
st.markdown('<h1 class="prof-title">🧮 Scientific Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-family: \'Roboto\', sans-serif; font-size: 1.2rem; color: #495057; text-align: center; margin-bottom: 2rem;">Professional calculations with history tracking</p>', unsafe_allow_html=True)

# ---------------------------------
# Main Layout
# ---------------------------------
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown('<div class="prof-card">', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">📊 Input Values</div>', unsafe_allow_html=True)
    
    col_num1, col_num2 = st.columns(2)
    with col_num1:
        num1 = st.number_input("**First Number**", value=0.0, step=0.1, format="%.6f")
    with col_num2:
        num2 = st.number_input("**Second Number**", value=0.0, step=0.1, format="%.6f")
    
    st.markdown('<div class="section-title">⚙️ Select Operation</div>', unsafe_allow_html=True)
    
    operation = st.selectbox(
        "Choose operation:",
        [
            "➕ Addition (+)",
            "➖ Subtraction (-)",
            "✖️ Multiplication (×)",
            "➗ Division (÷)",
            "📊 Modulus (%)",
            "🔲 Square (x²)",
            "🟢 Square Root (√x)",
            "🔄 Inverse (1/x)",
            "📐 Sine (sin)",
            "📐 Cosine (cos)",
            "📐 Tangent (tan)",
            "📐 Logarithm (log)",
            "📐 Exponent (e^x)",
            "📐 Power (x^y)"
        ]
    )
    
    # SINGLE BUTTON + INFO BELOW IT
    if st.button("**CALCULATE**", use_container_width=True):
        try:
            n1_rad = math.radians(num1)
            
            if "Addition" in operation:
                result = num1 + num2
                expression = f"{num1} + {num2}"
            elif "Subtraction" in operation:
                result = num1 - num2
                expression = f"{num1} - {num2}"
            elif "Multiplication" in operation:
                result = num1 * num2
                expression = f"{num1} × {num2}"
            elif "Division" in operation:
                if num2 == 0:
                    st.error("❌ Division by zero!")
                    result = None
                else:
                    result = num1 / num2
                    expression = f"{num1} ÷ {num2}"
            elif "Modulus" in operation:
                result = num1 % num2
                expression = f"{num1} % {num2}"
            elif "Square" in operation:
                result = num1 ** 2
                expression = f"{num1}²"
            elif "Square Root" in operation:
                if num1 < 0:
                    st.error("❌ Square root of negative!")
                    result = None
                else:
                    result = math.sqrt(num1)
                    expression = f"√{num1}"
            elif "Inverse" in operation:
                if num1 == 0:
                    st.error("❌ Division by zero!")
                    result = None
                else:
                    result = 1 / num1
                    expression = f"1/{num1}"
            elif "Sine" in operation:
                result = math.sin(n1_rad)
                expression = f"sin({num1}°)"
            elif "Cosine" in operation:
                result = math.cos(n1_rad)
                expression = f"cos({num1}°)"
            elif "Tangent" in operation:
                result = math.tan(n1_rad)
                expression = f"tan({num1}°)"
            elif "Logarithm" in operation:
                if num1 <= 0:
                    st.error("❌ Log of non-positive!")
                    result = None
                else:
                    result = math.log10(num1)
                    expression = f"log({num1})"
            elif "Exponent" in operation:
                result = math.exp(num1)
                expression = f"e^{num1}"
            elif "Power" in operation:
                result = num1 ** num2
                expression = f"{num1}^{num2}"
            
            if result is not None:
                st.session_state.history.append(f"{expression} = {result:.6f}")
                st.session_state.result = result
                st.session_state.expression = expression
                st.success("✅ Calculation completed!")
            else:
                st.session_state.result = None
                st.session_state.expression = ""
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    
    # INFO MESSAGE DIRECTLY BELOW CALCULATE BUTTON
    st.info("👆 Click **CALCULATE** to see result on the right")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Results Column
with col2:
    st.markdown('<div class="prof-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Result</div>', unsafe_allow_html=True)
    
    if st.session_state.result is not None:
        st.markdown(f"""
        <div class="result-section">
            <div class="result-title">Calculation Complete</div>
            <div class="result-value">{st.session_state.result:.8f}</div>
            <div class="result-equation">{st.session_state.expression}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# History
if st.session_state.history:
    st.markdown('<div class="prof-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🕒 History (Last 10)</div>', unsafe_allow_html=True)
    
    for item in st.session_state.history[-10:]:
        st.markdown(f'<div class="history-item">{item}</div>', unsafe_allow_html=True)
    
    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.history = []
        st.session_state.result = None
        st.session_state.expression = ""
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Nisar Section
st.markdown("""
<div class="prof-card nisar-card">
    <h3 class="nisar-name">Nisar Ahmad</h3>
    <p style="font-family: 'Roboto', sans-serif; font-size: 1rem; color: #495057; font-weight: 500; margin-bottom: 0.8rem;">
        AI/ML Developer | BS Computer Science Student
    </p>
    <p style="font-size: 0.95rem; color: #495057; margin: 0.8rem 0; line-height: 1.5;">
        <strong>COMSATS University Islamabad</strong><br>
        Sahiwal Campus
    </p>
    <p style="font-size: 0.9rem; color: #6c757d; margin-top: 1rem;">
        🚀 Building production-ready applications for Fiverr & Upwork clients
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 1.5rem; color: #6c757d; 
            font-size: 0.95rem; font-family: 'Roboto', sans-serif; 
            border-top: 1px solid #dee2e6; margin-top: 2rem;">
    Developed with ❤️ using Streamlit | Deployed on Hugging Face Spaces
</div>
""", unsafe_allow_html=True)
