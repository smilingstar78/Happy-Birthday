import streamlit as st
import time

# Set up the page
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# Custom CSS for a festive look
st.markdown("""
    <style>
    .big-title {
        font-size: 50px !important;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
    }
    .cake-style {
        font-size: 80px;
        text-align: center;
        line-height: 1.2;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="big-title">🎉 HAPPY BIRTHDAY! 🎉</p>', unsafe_allow_html=True)

# Input for your friend's name to make it personal
friend_name = st.text_input("Enter the birthday star's name:")

st.write("---")

# Session state to track if the candles are blown out
if 'candles_blown' not in st.session_state:
    st.session_state.candles_blown = False

# Display the cake based on the state
st.markdown("### Make a wish and blow out the candles! 🕯️")

if not st.session_state.candles_blown:
    # Lit candles
    st.markdown('<p class="cake-style">🔥 🔥 🔥<br>🎂🎂🎂</p>', unsafe_allow_html=True)
    
    # Interactive Button to "Blow out"
    if st.button("💨 BLOW OUT THE CANDLES!"):
        st.session_state.candles_blown = True
        st.rerun()
else:
    # Smoke/Blown out candles
    st.markdown('<p class="cake-style">💨 💨 💨<br>🎂🎂🎂</p>', unsafe_allow_html=True)
    
    # Birthday celebration effects!
    st.balloons()
    st.snow() # Looks like floating confetti/magic in this context
    
    st.success(f"✨ May all your wishes come true, {friend_name}! ✨")
    
    # Reset button so they can play with it again
    if st.button("Reset Cake 🎂"):
        st.session_state.candles_blown = False
        st.rerun()

# A little placeholder for your personal message
st.write("---")
st.markdown(f"""
### 💌 A Special Note for You:
> "Wishing you a fantastic day filled with love, laughter, and plenty of cake. 
> Cheers to another amazing year around the sun, **{friend_name}**!"
""")