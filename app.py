#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Neural Net of Affection
A breathtakingly beautiful, interactive Streamlit app visualizing the neural pathways of love
with stunning visuals, wholesome animations, and heartwarming messages.
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
import random
import math

# --- Page Configuration ---
st.set_page_config(
    page_title="Neural Net of Affection 🌸🧠💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Stunning Visual Theme ---
st.markdown("""
<style>
    /* Import beautiful fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Dancing+Script:wght@400;700&display=swap');
    
    /* Main app styling with gorgeous gradients */
    .stApp {
        background: linear-gradient(135deg, 
            #0f0c29 0%, 
            #24243e 25%, 
            #302b63 50%, 
            #24243e 75%, 
            #0f0c29 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Magical floating particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, rgba(255, 182, 193, 0.3), transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(255, 105, 180, 0.3), transparent),
            radial-gradient(1px 1px at 90px 40px, rgba(255, 20, 147, 0.3), transparent),
            radial-gradient(1px 1px at 130px 80px, rgba(199, 21, 133, 0.3), transparent);
        background-repeat: repeat;
        background-size: 150px 150px;
        animation: sparkle 20s linear infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    @keyframes sparkle {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.3; }
        50% { opacity: 0.6; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0.3; }
    }
    
    /* Beautiful title with magical glow */
    .magical-title {
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(45deg, 
            #ff6b6b, #feca57, #ff9ff3, #54a0ff, #5f27cd);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientText 4s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(255, 105, 180, 0.5);
        margin: 2rem 0;
        position: relative;
        z-index: 10;
    }
    
    @keyframes gradientText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Enchanting subtitle */
    .enchanting-subtitle {
        text-align: center;
        font-size: 1.4rem;
        color: #ffb6c1;
        margin-bottom: 3rem;
        font-style: italic;
        font-weight: 300;
        text-shadow: 0 0 10px rgba(255, 182, 193, 0.3);
        animation: gentleGlow 3s ease-in-out infinite alternate;
        position: relative;
        z-index: 10;
    }
    
    @keyframes gentleGlow {
        from { text-shadow: 0 0 10px rgba(255, 182, 193, 0.3); }
        to { text-shadow: 0 0 20px rgba(255, 182, 193, 0.6), 0 0 30px rgba(255, 105, 180, 0.3); }
    }
    
    /* Gorgeous sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(26, 26, 46, 0.95) 0%, rgba(48, 43, 99, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-right: 3px solid;
        border-image: linear-gradient(45deg, #ff6b6b, #feca57, #ff9ff3) 1;
        box-shadow: 5px 0 30px rgba(255, 105, 180, 0.2);
    }
    
    /* Beautiful control panels */
    .control-panel {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 182, 193, 0.2);
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(255, 105, 180, 0.1);
        transition: all 0.3s ease;
    }
    
    .control-panel:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(255, 105, 180, 0.2);
        border-color: rgba(255, 105, 180, 0.4);
    }
    
    /* Magical buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Dreamy metric cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(255, 182, 193, 0.1) 0%, rgba(255, 105, 180, 0.1) 100%);
        backdrop-filter: blur(10px);
        padding: 2rem 1rem;
        border-radius: 20px;
        border: 2px solid rgba(255, 105, 180, 0.2);
        text-align: center;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.03), transparent);
        transform: rotate(45deg);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }
    
    .metric-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(255, 105, 180, 0.25);
        border-color: rgba(255, 105, 180, 0.5);
    }
    
    .metric-card h4 {
        color: #ffb6c1;
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-card h2 {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 0 10px rgba(255, 105, 180, 0.3);
    }
    
    /* Heartwarming message box */
    .wholesome-message {
        background: linear-gradient(135deg, rgba(255, 182, 193, 0.15) 0%, rgba(255, 105, 180, 0.15) 100%);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        border: 2px solid rgba(255, 182, 193, 0.3);
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 10px 35px rgba(255, 105, 180, 0.15);
        position: relative;
        overflow: hidden;
        animation: gentlePulse 4s ease-in-out infinite;
    }
    
    @keyframes gentlePulse {
        0%, 100% { transform: scale(1); box-shadow: 0 10px 35px rgba(255, 105, 180, 0.15); }
        50% { transform: scale(1.02); box-shadow: 0 15px 45px rgba(255, 105, 180, 0.25); }
    }
    
    .wholesome-message::before {
        content: '💖';
        position: absolute;
        top: -10px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 2rem;
        animation: floatingHeart 2s ease-in-out infinite;
    }
    
    @keyframes floatingHeart {
        0%, 100% { transform: translateX(-50%) translateY(0px); }
        50% { transform: translateX(-50%) translateY(-5px); }
    }
    
    .wholesome-message h3 {
        color: #ff69b4;
        font-size: 1.3rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .wholesome-message p {
        color: #ffb6c1;
        font-size: 1.1rem;
        line-height: 1.6;
        font-style: italic;
        margin: 0;
    }
    
    /* Beautiful info sections */
    .info-section {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 182, 193, 0.15);
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .info-section:hover {
        transform: translateY(-2px);
        border-color: rgba(255, 182, 193, 0.3);
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.1);
    }
    
    .info-section h3 {
        color: #ff69b4;
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
        font-weight: 600;
    }
    
    .info-section p {
        color: #e0e0e0;
        line-height: 1.5;
        margin: 0;
    }
    
    /* Gorgeous footer */
    .magical-footer {
        text-align: center;
        margin-top: 3rem;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(255, 105, 180, 0.1) 0%, rgba(199, 21, 133, 0.1) 100%);
        border-radius: 25px;
        border: 1px solid rgba(255, 105, 180, 0.2);
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(255, 105, 180, 0.1);
    }
    
    .magical-footer em {
        color: #ffb6c1;
        font-size: 1.3rem;
        font-weight: 400;
        text-shadow: 0 0 15px rgba(255, 182, 193, 0.4);
        display: block;
        animation: gentleGlow 3s ease-in-out infinite alternate;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #ff69b4, #ff1493);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #ff1493, #c7155b);
    }
    
    /* Remove default streamlit styling */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 182, 193, 0.3);
        border-radius: 10px;
    }
    
    .stSlider > div > div {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Enhanced Data Structure ---
class NeuralNetworkData:
    def __init__(self):
        self.input_categories = {
            "💫 Magical Moments": [
                "Her radiant morning smile ☀️😊",
                "The way her eyes sparkle with joy ✨👀",
                "Her gentle sleepy whispers 🌙💤",
                "When she laughs at my silly jokes 😂💕",
                "Her focused concentration face 🤔📚"
            ],
            "💖 Heart Connections": [
                "Her warm, comforting embraces 🤗💝",
                "Our deep midnight conversations 🌌💬",
                "Her sweet 'thinking of you' messages 📱💭",
                "The way she truly listens 👂❤️",
                "Her boundless empathy and care 💙🤲"
            ],
            "🌈 Shared Adventures": [
                "Our secret inside jokes 😄🤫",
                "Dancing together in the kitchen 💃🕺",
                "Quiet moments of pure togetherness 🕯️👫",
                "Planning dreams and adventures 🗺️✈️",
                "Cheering each other's victories 🌟🎉"
            ],
            "🎨 Creative Souls": [
                "Her artistic expressions 🎨🖌️",
                "The songs that remind me of her 🎵💕",
                "Her unique perspective on life 🔍🌍",
                "The way she sees beauty everywhere 🌸👁️",
                "Her inspiring creativity 💡✨"
            ]
        }
        
        self.hidden_emotions = [
            "Pure Bliss 🌈✨",
            "Serene Peace ☮️🕊️",
            "Dancing Butterflies 🦋💃",
            "Overflowing Gratitude 🙏💖",
            "Electric Inspiration ⚡🌟",
            "Childlike Wonder 😍🎈",
            "Warm Comfort 🛋️☕",
            "Joyful Excitement 🎉🎊",
            "Deep Contentment 😌💆",
            "Gentle Tenderness 🤱💕"
        ]
        
        self.love_expressions = [
            "My heart beats only for you 💓👑",
            "You are my universe and beyond 🌌♾️",
            "In your love, I found my home 🏠💖"
        ]
        
        self.wholesome_messages = [
            {
                "title": "The Science of Love",
                "message": "Did you know that when you look at someone you love, your pupils dilate and your heart synchronizes with theirs? Love truly is the most beautiful neural network! 🧠💕"
            },
            {
                "title": "Love's Magic",
                "message": "Every time she smiles, approximately 17 muscles work together to create that perfect expression that lights up your entire world. Magic exists, and it lives in her smile! ✨😊"
            },
            {
                "title": "Neural Harmony",
                "message": "Love doesn't just exist in the heart - it creates beautiful patterns across your entire brain, lighting up regions responsible for joy, attachment, and pure bliss! 🌟🧠"
            },
            {
                "title": "Infinite Connection",
                "message": "The neural pathways of love grow stronger with every shared moment, every laugh, every gentle touch. Your love is literally rewiring your brain for happiness! 💫💖"
            },
            {
                "title": "Beautiful Chemistry",
                "message": "When you think of her, your brain releases a cocktail of dopamine, oxytocin, and serotonin - nature's own love potion that makes everything more beautiful! 🧪✨"
            }
        ]

# --- Initialize Data ---
@st.cache_resource
def get_network_data():
    return NeuralNetworkData()

network_data = get_network_data()

# --- Magical Header ---
st.markdown('<h1 class="magical-title">Neural Net of Affection</h1>', unsafe_allow_html=True)
st.markdown('<p class="enchanting-subtitle">✨ Mapping the ethereal pathways from her soul to yours 💫</p>', unsafe_allow_html=True)

# --- Enhanced Sidebar ---
with st.sidebar:
    st.markdown("### 🎛️ Love Control Center")
    
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    
    # Category selection with beautiful emojis
    selected_category = st.selectbox(
        "🌟 Choose Your Love Story:",
        list(network_data.input_categories.keys()),
        help="Select the type of beautiful moments that make your heart flutter"
    )
    
    # Animation speed with poetic description
    animation_speed = st.slider(
        "💫 Animation Flow (like time when I'm with her):",
        min_value=300,
        max_value=2000,
        value=800,
        step=100,
        help="Slower = More time to savor each beautiful moment"
    )
    
    # Color theme selection
    color_theme = st.selectbox(
        "🎨 Emotional Palette:",
        ["Dreamy Pink", "Mystical Purple", "Serene Blue", "Joyful Rainbow", "Sunset Romance"],
        help="Choose the colors that match your heart's mood"
    )
    
    # Network intensity
    intensity = st.slider(
        "💕 Love Intensity:",
        min_value=0.3,
        max_value=2.5,
        value=1.2,
        step=0.1,
        help="How deeply does your heart feel? Turn up the magic!"
    )
    
    # Special wholesome button
    if st.button("💝 Send Love Energy"):
        st.balloons()
        st.success("💖 Love energy sent through the neural network! 💖")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Wholesome message section
    current_message = random.choice(network_data.wholesome_messages)
    st.markdown(f"""
    <div class="wholesome-message">
        <h3>{current_message['title']}</h3>
        <p>{current_message['message']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- Enhanced Color Schemes ---
def get_color_scheme(theme, intensity_factor):
    themes = {
        "Dreamy Pink": {
            "input": f"rgba(255, 182, 193, {0.9 * intensity_factor})",
            "hidden": f"rgba(255, 105, 180, {1.0 * intensity_factor})",
            "output": f"rgba(255, 20, 147, {1.2 * intensity_factor})",
            "edges": f"rgba(255, 240, 245, {0.7 * intensity_factor})",
            "glow": "rgba(255, 105, 180, 0.3)"
        },
        "Mystical Purple": {
            "input": f"rgba(221, 160, 221, {0.9 * intensity_factor})",
            "hidden": f"rgba(147, 112, 219, {1.0 * intensity_factor})",
            "output": f"rgba(138, 43, 226, {1.2 * intensity_factor})",
            "edges": f"rgba(230, 230, 250, {0.7 * intensity_factor})",
            "glow": "rgba(147, 112, 219, 0.3)"
        },
        "Serene Blue": {
            "input": f"rgba(173, 216, 230, {0.9 * intensity_factor})",
            "hidden": f"rgba(100, 149, 237, {1.0 * intensity_factor})",
            "output": f"rgba(65, 105, 225, {1.2 * intensity_factor})",
            "edges": f"rgba(240, 248, 255, {0.7 * intensity_factor})",
            "glow": "rgba(100, 149, 237, 0.3)"
        },
        "Joyful Rainbow": {
            "input": f"rgba(255, 99, 132, {0.9 * intensity_factor})",
            "hidden": f"rgba(54, 162, 235, {1.0 * intensity_factor})",
            "output": f"rgba(255, 206, 86, {1.2 * intensity_factor})",
            "edges": f"rgba(255, 255, 255, {0.7 * intensity_factor})",
            "glow": "rgba(255, 99, 132, 0.3)"
        },
        "Sunset Romance": {
            "input": f"rgba(255, 154, 158, {0.9 * intensity_factor})",
            "hidden": f"rgba(250, 208, 196, {1.0 * intensity_factor})",
            "output": f"rgba(255, 206, 84, {1.2 * intensity_factor})",
            "edges": f"rgba(255, 183, 197, {0.7 * intensity_factor})",
            "glow": "rgba(255, 154, 158, 0.3)"
        }
    }
    return themes[theme]

# --- Breathtaking Figure Creation ---
@st.cache_data
def create_magical_network(inputs, hidden, output, colors, speed, intensity_val):
    # Calculate elegant positions
    input_count = len(inputs)
    hidden_count = len(hidden)
    output_count = len(output)
    
    # Create flowing, organic positions
    x_in = [-1.2] * input_count
    y_in = np.linspace(0.05, 0.95, input_count)
    
    # Create a more organic hidden layer arrangement
    x_hid = [0.5] * hidden_count
    y_hid = np.linspace(0.02, 0.98, hidden_count)
    
    x_out = [2.2] * output_count
    y_out = np.linspace(0.35, 0.65, output_count)

    fig = go.Figure()
    
    # Add magical background elements
    for i in range(10):
        fig.add_shape(
            type="circle",
            x0=random.uniform(-2, 3), y0=random.uniform(0, 1),
            x1=random.uniform(-2, 3), y1=random.uniform(0, 1),
            fillcolor=colors["glow"],
            line=dict(color="rgba(0,0,0,0)", width=0),
            opacity=0.1
        )
    
    # Create beautiful flowing connections
    connection_strengths = []
    
    # Input to hidden connections with varying beauty
    for i, (xi, yi) in enumerate(zip(x_in, y_in)):
        for j, (xh, yh) in enumerate(zip(x_hid, y_hid)):
            # Create connection strength based on emotional resonance
            strength = np.random.uniform(0.3, 1.5) * intensity_val
            connection_strengths.append(strength)
            
            # Create flowing bezier-like curves
            mid_x = (xi + xh) / 2 + np.random.uniform(-0.1, 0.1)
            mid_y = (yi + yh) / 2 + np.random.uniform(-0.05, 0.05)
            
            # Determine line style based on strength
            line_dash = "solid" if strength > 0.8 else "dot"
            
            fig.add_shape(
                type="line",
                x0=xi + 0.15, y0=yi, x1=xh - 0.15, y1=yh,
                line=dict(
                    color=colors["edges"],
                    width=strength * 2,
                    dash=line_dash
                ),
                opacity=min(strength, 1.0)
            )
    
    # Hidden to output connections (stronger and more magical)
    for xh, yh in zip(x_hid, y_hid):
        for xo, yo in zip(x_out, y_out):
            strength = np.random.uniform(1.0, 2.0) * intensity_val
            fig.add_shape(
                type="line",
                x0=xh + 0.15, y0=yh, x1=xo - 0.15, y1=yo,
                line=dict(
                    color=colors["edges"],
                    width=strength * 1.5,
                    dash="solid"
                ),
                opacity=min(strength * 0.8, 1.0)
            )
    
    # Create stunning node visualizations
    base_input_size = 20
    base_hidden_size = 25
    base_output_size = 35
    
    # Input layer - delicate and beautiful
    fig.add_trace(go.Scatter(
        x=x_in, y=y_in,
        mode="markers+text",
        marker=dict(
            size=[base_input_size + i*2 for i in range(input_count)],
            color=colors["input"],
            line=dict(color="white", width=3),
            symbol="circle",
            opacity=0.9
        ),
        text=inputs,
        textposition="middle right",
        textfont=dict(
            color="white",
            size=11,
            family="Inter, sans-serif",
            shadow="2px 2px 4px rgba(0,0,0,0.3)"
        ),
        name="✨ Beautiful Inputs",
        hovertemplate="<b>%{text}</b><br>💕 Input Layer<br>Where magic begins<extra></extra>",
        hoverlabel=dict(bgcolor="rgba(255, 105, 180, 0.8)", font_color="white")
    ))
    
    # Hidden layer - mystical and emotional
    fig.add_trace(go.Scatter(
        x=x_hid, y=y_hid,
        mode="markers+text",
        marker=dict(
            size=[base_hidden_size + i*1.5 for i in range(hidden_count)],
            color=colors["hidden"],
            line=dict(color="white", width=3),
            symbol="diamond",
            opacity=0.9
        ),
        text=hidden,
        textposition="middle right",
        textfont=dict(
            color="white",
            size=12,
            family="Inter, sans-serif",
            shadow="2px 2px 4px rgba(0,0,0,0.3)"
        ),
        name="💫 Emotional Processing",
        hovertemplate="<b>%{text}</b><br>🌟 Hidden Layer<br>Where feelings transform<extra></extra>",
        hoverlabel=dict(bgcolor="rgba(147, 112, 219, 0.8)", font_color="white")
    ))
    
    # Output layer - radiant and powerful
    fig.add_trace(go.Scatter(
        x=x_out, y=y_out,
        mode="markers+text",
        marker=dict(
            size=[base_output_size + i*5 for i in range(output_count)],
            color=colors["output"],
            line=dict(color="gold", width=4),
            symbol="star",
            opacity=1.0
        ),
        text=output,
        textposition="middle right",
        textfont=dict(
            color="white",
            size=14,
            family="Inter, sans-serif",
            shadow="3px 3px 6px rgba(0,0,0,0.4)"
        ),
        name="💖 Pure Love",
        hovertemplate="<b>%{text}</b><br>👑 Output Layer<br>The ultimate expression<extra></extra>",
        hoverlabel=dict(bgcolor="rgba(255, 20, 147, 0.8)", font_color="white")
    ))
    
    # Create mesmerizing animation frames
    frames = []
    
    # Frame 1: Gentle input awakening
    frames.append(go.Frame(
        name="gentle_awakening",
        data=[
            go.Scatter(
                x=x_in, y=y_in, mode="markers+text",
                marker=dict(
                    size=[s*1.8 for s in [base_input_size + i*2 for i in range(input_count)]], 
                    color=colors["output"],
                    line=dict(color="gold", width=4),
                    opacity=1.0
                ),
                text=inputs, textposition="middle right",
                textfont=dict(color="white", size=12, family="Inter, sans-serif"),
                name="✨ Awakening Inputs"
            ),
            go.Scatter(
                x=x_hid, y=y_hid, mode="markers+text",
                marker=dict(
                    size=[base_hidden_size + i*1.5 for i in range(hidden_count)], 
                    color=colors["hidden"],
                    opacity=0.6
                ),
                text=hidden, textposition="middle right",
                textfont=dict(color="white", size=12, family="Inter, sans-serif"),
                name="💫 Sleeping Emotions"
            ),
            go.Scatter(
                x=x_out, y=y_out, mode="markers+text",
                marker=dict(
                    size=[base_output_size + i*5 for i in range(output_count)], 
                    color=colors["output"],
                    opacity=0.4
                ),
                text=output, textposition="middle right",
                textfont=dict(color="white", size=14, family="Inter, sans-serif"),
                name="💖 Dormant Love"
            )
        ]
    ))
    
    # Frame 2: Emotional symphony
    frames.append(go.Frame(
        name="emotional_symphony",
        data=[
            go.Scatter(
                x=x_in, y=y_in, mode="markers+text",
                marker=dict(
                    size=[base_input_size + i*2 for i in range(input_count)], 
                    color=colors["input"],
                    opacity=0.8
                ),
                text=inputs, textposition="middle right",
                textfont=dict(color="white", size=11, family="Inter, sans-serif"),
                name="✨ Gentle Inputs"
            ),
            go.Scatter(
                x=x_hid, y=y_hid, mode="markers+text",
                marker=dict(
                    size=[s*2.2 for s in [base_hidden_size + i*1.5 for i in range(hidden_count)]], 
                    color=colors["output"],
                    line=dict(color="gold", width=4),
                    opacity=1.0
                ),
                text=hidden, textposition="middle right",
                textfont=dict(color="white", size=13, family="Inter, sans-serif"),
                name="💫 Dancing Emotions"
            ),
            go.Scatter(
                x=x_out, y=y_out, mode="markers+text",
                marker=dict(
                    size=[base_output_size + i*5 for i in range(output_count)], 
                    color=colors["output"],
                    opacity=0.7
                ),
                text=output, textposition="middle right",
                textfont=dict(color="white", size=14, family="Inter, sans-serif"),
                name="💖 Growing Love"
            )
        ]
    ))
    
    # Frame 3: Love's magnificent explosion
    frames.append(go.Frame(
        name="loves_explosion",
        data=[
            go.Scatter(
                x=x_in, y=y_in, mode="markers+text",
                marker=dict(
                    size=[base_input_size + i*2 for i in range(input_count)], 
                    color=colors["input"],
                    opacity=0.7
                ),
                text=inputs, textposition="middle right",
                textfont=dict(color="white", size=11, family="Inter, sans-serif"),
                name="✨ Cherished Inputs"
            ),
            go.Scatter(
                x=x_hid, y=y_hid, mode="markers+text",
                marker=dict(
                    size=[base_hidden_size + i*1.5 for i in range(hidden_count)], 
                    color=colors["hidden"],
                    opacity=0.8
                ),
                text=hidden, textposition="middle right",
                textfont=dict(color="white", size=12, family="Inter, sans-serif"),
                name="💫 Harmonious Emotions"
            ),
            go.Scatter(
                x=x_out, y=y_out, mode="markers+text",
                marker=dict(
                    size=[s*2.8 for s in [base_output_size + i*5 for i in range(output_count)]], 
                    color="rgba(255, 215, 0, 1.0)",
                    line=dict(color="white", width=5),
                    opacity=1.0
                ),
                text=output, textposition="middle right",
                textfont=dict(color="white", size=16, family="Inter, sans-serif"),
                name="💖 Radiant Love"
            )
        ]
    ))
    
    fig.frames = frames
    
    # Magical controls with beautiful styling
    fig.update_layout(
        updatemenus=[{
            "type": "buttons",
            "showactive": False,
            "x": 0.02,
            "y": 1.08,
            "bgcolor": "rgba(255, 105, 180, 0.1)",
            "bordercolor": "rgba(255, 105, 180, 0.3)",
            "borderwidth": 2,
            "buttons": [
                {
                    "label": "🌟 Awaken the Network",
                    "method": "animate",
                    "args": [None, {
                        "frame": {"duration": speed, "redraw": True},
                        "fromcurrent": True,
                        "transition": {"duration": speed//3, "easing": "cubic-in-out"}
                    }]
                },
                {
                    "label": "⏸️ Pause Magic",
                    "method": "animate",
                    "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}]
                },
                {
                    "label": "🔄 Reset Hearts",
                    "method": "restyle",
                    "args": [{"visible": [True, True, True]}]
                }
            ]
        }],
        sliders=[{
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 14, "color": "white", "family": "Inter"},
                "prefix": "✨ Stage: ",
                "visible": True,
                "xanchor": "right"
            },
            "bgcolor": "rgba(255, 105, 180, 0.1)",
            "bordercolor": "rgba(255, 105, 180, 0.3)",
            "borderwidth": 2,
            "pad": {"b": 15, "t": 60},
            "len": 0.9,
            "x": 0.05,
            "y": 0,
            "steps": [
                {
                    "args": [[f.name], {
                        "frame": {"duration": speed, "redraw": True},
                        "mode": "immediate",
                        "transition": {"duration": speed//3, "easing": "cubic-in-out"}
                    }],
                    "label": f.name.replace("_", " ").title(),
                    "method": "animate"
                } for f in frames
            ]
        }]
    )
    
    # Breathtaking layout design
    fig.update_layout(
        title={
            "text": f"💫 {selected_category} → Neural Symphony of Love 💫",
            "x": 0.5,
            "font": {"size": 18, "color": "white", "family": "Inter"},
            "pad": {"t": 20}
        },
        showlegend=True,
        legend=dict(
            x=0.02, y=0.98,
            bgcolor="rgba(0,0,0,0.7)",
            bordercolor="rgba(255,182,193,0.5)",
            borderwidth=2,
            font=dict(color="white", family="Inter", size=12)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", family="Inter"),
        xaxis=dict(
            showgrid=False, zeroline=False, showticklabels=False,
            range=[-2, 3.5], fixedrange=True
        ),
        yaxis=dict(
            showgrid=False, zeroline=False, showticklabels=False,
            range=[-0.05, 1.05], fixedrange=True
        ),
        margin=dict(l=20, r=20, t=100, b=80),
        height=700,
        hovermode="closest"
    )
    
    return fig

# --- Main Content Area ---
col1, col2 = st.columns([4, 1])

with col1:
    # Get current data
    current_inputs = network_data.input_categories[selected_category]
    colors = get_color_scheme(color_theme, intensity)
    
    # Create and display the magical network
    fig = create_magical_network(
        current_inputs,
        network_data.hidden_emotions,
        network_data.love_expressions,
        colors,
        animation_speed,
        intensity
    )
    
    st.plotly_chart(fig, use_container_width=True, key="magical_neural_network")

with col2:
    st.markdown("### 📊 Love Analytics")
    
    # Beautiful metrics
    st.markdown(f"""
    <div class="metric-card">
        <h4>💝 Input Signals</h4>
        <h2>{len(network_data.input_categories[selected_category])}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <h4>🌟 Emotions</h4>
        <h2>{len(network_data.hidden_emotions)}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <h4>💖 Love Output</h4>
        <h2>{len(network_data.love_expressions)}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Magical love wisdom button
    if st.button("🔮 Love Wisdom"):
        wisdom = random.choice([
            "Love is the only force capable of transforming an enemy into a friend 💫",
            "In your light, I learn how to love 🌟",
            "Love is not just looking at each other, it's looking in the same direction 👫",
            "The best thing to hold onto in life is each other 🤗",
            "Love is a friendship set to music 🎵",
            "Where there is love, there is life 🌱",
            "Love is the bridge between two hearts 🌉"
        ])
        st.info(f"✨ {wisdom}")
    
    # Current emotional state
    st.markdown("### 💫 Current Flow")
    emotional_intensity = min(100, int(intensity * 50))
    st.progress(emotional_intensity / 100)
    st.caption(f"💕 Love intensity: {emotional_intensity}%")

# --- Wholesome Information Sections ---
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-section">
        <h3>🎯 How Your Heart Works</h3>
        <p>Every beautiful moment with her creates neural pathways that strengthen over time. This network visualizes how her smallest gestures cascade through your emotional processing center, ultimately expressing as pure, infinite love.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-section">
        <h3>🔬 The Science of Magic</h3>
        <p>When you see her smile, your brain releases a symphony of happy chemicals. The hidden layer represents how different emotions combine and amplify, creating something far more beautiful than the sum of its parts.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-section">
        <h3>💡 Love's Algorithm</h3>
        <p>This isn't just a network - it's a love algorithm that gets stronger with every shared laugh, every gentle touch, every moment of understanding. Your love literally rewires itself to become more beautiful each day.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Dynamic Wholesome Messages ---
st.markdown("### 💌 Heartwarming Neural Messages")

message_cols = st.columns(2)
with message_cols[0]:
    if st.button("💝 Generate Love Message", key="love_msg"):
        messages = [
            "Every neuron in this network fires with the rhythm of your heartbeat when you think of her 💓",
            "The most beautiful algorithm ever written is the one that calculates how much you love her: INFINITY 💫",
            "Your brain doesn't just process her smile - it celebrates it with a festival of joy across every neural pathway 🎉",
            "Love isn't just an emotion in this network - it's the very architecture that connects every beautiful thought of her ✨",
            "When she laughs, it doesn't just activate your happiness centers - it creates new ones, dedicated entirely to that perfect sound 🎵"
        ]
        st.success(random.choice(messages))

with message_cols[1]:
    if st.button("🌟 Neural Love Fact", key="love_fact"):
        facts = [
            "Did you know? Your pupils dilate by up to 45% when you look at someone you love - it's your brain's way of trying to take in more of their beauty! 👁️✨",
            "Love activates the same reward pathways as chocolate, but with 1000x more intensity and zero calories! 🍫💕",
            "When couples hold hands, their heartbeats synchronize within 3 minutes - true neural harmony! 👫💓",
            "Your brain creates a unique 'love map' for her that's more detailed than any GPS navigation system 🗺️💖",
            "Love literally grows your brain - the areas responsible for empathy and compassion physically expand when you're in love! 🧠💕"
        ]
        st.info(random.choice(facts))

# --- Beautiful Footer ---
st.markdown("""
<div class="magical-footer">
    <em>"In the vast neural network of existence, love is the most beautiful algorithm - 
    one that transforms simple inputs into infinite joy, and makes every synapse sing with the melody of two hearts becoming one 💕✨"</em>
</div>
""", unsafe_allow_html=True)
