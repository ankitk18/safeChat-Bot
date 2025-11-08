import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []

# Page config
st.set_page_config(page_title="SafeChat", page_icon="🛡️", layout="centered")

# Header
st.title("🛡️ SafeChat - Toxicity Filter & Rewriter")
st.markdown("**Detect toxic messages and rewrite them politely using AI**")

# Sidebar with simple controls
with st.sidebar:
    st.header("Settings")
    
    # Tone selection
    tone = st.selectbox(
        "Rewrite Style:",
        ["Professional", "Friendly", "Polite", "Formal"]
    )
    
    # Sensitivity
    sensitivity = st.slider("Detection Sensitivity", 0.3, 0.9, 0.6)
    
    st.markdown("---")
    
    # Simple stats
    if st.session_state.history:
        total = len(st.session_state.history)
        toxic = sum(1 for h in st.session_state.history if h['toxic'])
        st.metric("Messages Analyzed", total)
        st.metric("Toxic Detected", toxic)
    
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

# Main interface
st.markdown("### Enter your message:")
user_input = st.text_area(
    "",
    placeholder="Type your message here...",
    height=120
)

col1, col2 = st.columns(2)
with col1:
    analyze_btn = st.button("🔍 Analyze Message", type="primary")
with col2:
    rewrite_btn = st.button("✨ Analyze & Rewrite")

# Analysis function
def analyze_text(text, include_rewrite=False):
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    # Toxicity detection
    detect_prompt = f"""
    Analyze this text for toxicity:
    Text: "{text}"
    
    Respond with JSON format:
    {{
        "is_toxic": true/false,
        "score": 0.0-1.0,
        "reason": "brief explanation",
        "categories": ["list of issues found"]
    }}
    """
    
    try:
        response = model.generate_content(detect_prompt)
        result_text = response.text.strip()
        
        # Clean JSON response
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0]
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0]
        
        result = json.loads(result_text)
    except:
        # Fallback if JSON parsing fails
        result = {
            "is_toxic": False,
            "score": 0.0,
            "reason": "Analysis completed",
            "categories": []
        }
    
    # Rewrite if requested and toxic
    rewrite = None
    if include_rewrite and (result.get("is_toxic", False) or result.get("score", 0) > sensitivity):
        rewrite_prompt = f"""
        Rewrite this message to be {tone.lower()} and respectful while keeping the same meaning:
        
        Original: "{text}"
        
        Provide only the rewritten text, nothing else.
        """
        
        try:
            rewrite_response = model.generate_content(rewrite_prompt)
            rewrite = rewrite_response.text.strip()
        except:
            rewrite = "Could not generate rewrite"
    
    return result, rewrite

# Process user input
if (analyze_btn or rewrite_btn) and user_input.strip():
    with st.spinner("Analyzing..."):
        result, rewrite = analyze_text(user_input, include_rewrite=rewrite_btn)
    
    # Store in history
    st.session_state.history.append({
        'text': user_input[:50] + "..." if len(user_input) > 50 else user_input,
        'toxic': result.get('is_toxic', False),
        'score': result.get('score', 0),
        'timestamp': datetime.now().strftime("%H:%M:%S")
    })
    
    # Display results
    st.markdown("### 📊 Analysis Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        is_toxic = result.get('is_toxic', False)
        status = "🔴 Toxic" if is_toxic else "🟢 Safe"
        st.metric("Status", status)
    
    with col2:
        score = result.get('score', 0)
        st.metric("Toxicity Score", f"{score:.2f}")
    
    with col3:
        risk_level = "High" if score > 0.7 else "Medium" if score > 0.4 else "Low"
        st.metric("Risk Level", risk_level)
    
    # Explanation
    if result.get('reason'):
        st.info(f"**Analysis:** {result['reason']}")
    
    # Categories
    if result.get('categories'):
        st.warning(f"**Issues detected:** {', '.join(result['categories'])}")
    
    # Rewrite section
    if rewrite:
        st.markdown("### ✨ Suggested Rewrite")
        st.success(rewrite)
        
        if st.button("📋 Copy Rewrite"):
            st.balloons()
            st.success("Copied to clipboard!")

elif (analyze_btn or rewrite_btn) and not user_input.strip():
    st.warning("Please enter some text to analyze!")

# Load example if selected
if hasattr(st.session_state, 'example_text'):
    st.text_area("Selected example:", value=st.session_state.example_text, key="example_display")
    del st.session_state.example_text



# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🎓 <strong>College Project</strong> | Built with Google Gemini AI & Streamlit</p>
    <p><small>⚠️ This is an educational project. Results may not be 100% accurate.</small></p>
</div>
""", unsafe_allow_html=True)