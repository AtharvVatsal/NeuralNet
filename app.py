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
    initial_sidebar_state="expanded"
)

# --- Enhanced Visual Theme ---
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
    
    /* Enhanced sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(26, 26, 46, 0.95) 0%, rgba(48, 43, 99, 0.95) 100%);
        backdrop-filter: blur(20px);
        border-right: 3px solid;
        border-image: linear-gradient(45deg, #ff6b6b, #feca57, #ff9ff3) 1;
        box-shadow: 5px 0 30px rgba(255, 105, 180, 0.2);
    }
    
    /* Beautiful control panels */
    .control-panel {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 2px solid rgba(255, 182, 193, 0.3);
        padding: 1.8rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(255, 105, 180, 0.15);
        transition: all 0.3s ease;
    }
    
    .control-panel:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 45px rgba(255, 105, 180, 0.25);
        border-color: rgba(255, 105, 180, 0.5);
    }
    
    .control-panel h3 {
        color: #ff69b4;
        text-align: center;
        margin-bottom: 1.5rem;
        font-size: 1.2rem;
        font-weight: 600;
        text-shadow: 0 0 10px rgba(255, 105, 180, 0.3);
    }
    
    /* Enhanced theme selector */
    .theme-selector {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 182, 193, 0.2);
    }
    
    .theme-preview {
        display: flex;
        align-items: center;
        padding: 0.5rem;
        margin: 0.3rem 0;
        border-radius: 10px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .theme-preview:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateX(5px);
    }
    
    .theme-color-dot {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin-right: 10px;
        border: 2px solid white;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
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
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Enhanced metric cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(255, 182, 193, 0.15) 0%, rgba(255, 105, 180, 0.15) 100%);
        backdrop-filter: blur(15px);
        padding: 2rem 1rem;
        border-radius: 20px;
        border: 2px solid rgba(255, 105, 180, 0.3);
        text-align: center;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.15);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 40px rgba(255, 105, 180, 0.3);
        border-color: rgba(255, 105, 180, 0.6);
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
        text-shadow: 0 0 15px rgba(255, 105, 180, 0.4);
    }
    
    /* Heartwarming message box */
    .wholesome-message {
        background: linear-gradient(135deg, rgba(255, 182, 193, 0.2) 0%, rgba(255, 105, 180, 0.2) 100%);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        border: 2px solid rgba(255, 182, 193, 0.4);
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 10px 35px rgba(255, 105, 180, 0.2);
        position: relative;
        overflow: hidden;
        animation: gentlePulse 4s ease-in-out infinite;
    }
    
    @keyframes gentlePulse {
        0%, 100% { transform: scale(1); box-shadow: 0 10px 35px rgba(255, 105, 180, 0.2); }
        50% { transform: scale(1.02); box-shadow: 0 15px 45px rgba(255, 105, 180, 0.3); }
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
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 182, 193, 0.2);
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .info-section:hover {
        transform: translateY(-2px);
        border-color: rgba(255, 182, 193, 0.4);
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.15);
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
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Enhanced Data Structure ---
class NeuralNetworkData:
    def __init__(self):
        self.themes = {
            "🌸 Cherry Blossom Dreams": {
                "description": "Soft pink petals of pure affection",
                "input_color": "rgba(255, 182, 193, 0.9)",
                "hidden_color": "rgba(255, 105, 180, 1.0)",
                "output_color": "rgba(255, 20, 147, 1.2)",
                "edge_color": "rgba(255, 240, 245, 0.7)",
                "glow": "rgba(255, 105, 180, 0.3)",
                "dot_color": "#ffb6c1"
            },
            "🌙 Moonlit Romance": {
                "description": "Silvery whispers under starlight",
                "input_color": "rgba(221, 160, 221, 0.9)",
                "hidden_color": "rgba(147, 112, 219, 1.0)",
                "output_color": "rgba(138, 43, 226, 1.2)",
                "edge_color": "rgba(230, 230, 250, 0.7)",
                "glow": "rgba(147, 112, 219, 0.3)",
                "dot_color": "#dda0dd"
            },
            "🌊 Ocean Serenity": {
                "description": "Gentle waves of deep connection",
                "input_color": "rgba(173, 216, 230, 0.9)",
                "hidden_color": "rgba(100, 149, 237, 1.0)",
                "output_color": "rgba(65, 105, 225, 1.2)",
                "edge_color": "rgba(240, 248, 255, 0.7)",
                "glow": "rgba(100, 149, 237, 0.3)",
                "dot_color": "#add8e6"
            },
            "🌈 Rainbow Hearts": {
                "description": "Vibrant celebration of love",
                "input_color": "rgba(255, 99, 132, 0.9)",
                "hidden_color": "rgba(54, 162, 235, 1.0)",
                "output_color": "rgba(255, 206, 86, 1.2)",
                "edge_color": "rgba(255, 255, 255, 0.7)",
                "glow": "rgba(255, 99, 132, 0.3)",
                "dot_color": "#ff6384"
            },
            "🌅 Golden Sunrise": {
                "description": "Warm dawn of new beginnings",
                "input_color": "rgba(255, 154, 158, 0.9)",
                "hidden_color": "rgba(250, 208, 196, 1.0)",
                "output_color": "rgba(255, 206, 84, 1.2)",
                "edge_color": "rgba(255, 183, 197, 0.7)",
                "glow": "rgba(255, 154, 158, 0.3)",
                "dot_color": "#ff9a9e"
            },
            "💎 Crystal Clarity": {
                "description": "Pure, crystalline love essence",
                "input_color": "rgba(200, 200, 255, 0.9)",
                "hidden_color": "rgba(150, 150, 255, 1.0)",
                "output_color": "rgba(100, 100, 255, 1.2)",
                "edge_color": "rgba(230, 230, 255, 0.7)",
                "glow": "rgba(150, 150, 255, 0.3)",
                "dot_color": "#c8c8ff"
            }
        }
        
        self.input_categories = {
            "💫 Magical Moments": [
                "Morning sunshine smile",
                "Sparkling eyes of joy",
                "Gentle sleepy whispers",
                "Infectious laughter",
                "Focused concentration"
            ],
            "💖 Heart Connections": [
                "Warm embraces",
                "Deep conversations",
                "Thoughtful messages",
                "Active listening",
                "Endless empathy"
            ],
            "🌈 Shared Adventures": [
                "Inside jokes",
                "Kitchen dancing",
                "Quiet togetherness",
                "Dream planning",
                "Victory celebrations"
            ],
            "🎨 Creative Souls": [
                "Artistic expressions",
                "Musical memories",
                "Unique perspectives",
                "Beauty appreciation",
                "Creative inspiration"
            ],
            "🌟 Daily Wonders": [
                "Morning coffee ritual",
                "Evening cuddles",
                "Silly text messages",
                "Surprise gestures",
                "Peaceful silences"
            ]
        }
        
        self.hidden_emotions = [
            "Pure Bliss",
            "Serene Peace",
            "Dancing Joy",
            "Overwhelming Gratitude",
            "Electric Inspiration",
            "Childlike Wonder",
            "Warm Comfort",
            "Excited Anticipation",
            "Deep Contentment",
            "Gentle Tenderness"
        ]
        
        self.love_expressions = [
            "Heart beats only for you",
            "You are my universe",
            "In your love, I found home"
        ]
        
        self.wholesome_messages = [
            {
                "title": "The Science of Love",
                "message": "When you look at someone you love, your pupils dilate and your heart synchronizes with theirs. Love truly is the most beautiful neural network! 🧠💕"
            },
            {
                "title": "Love's Magic",
                "message": "Every smile uses 17 muscles working together to create that perfect expression that lights up your entire world. Magic exists in every smile! ✨😊"
            },
            {
                "title": "Neural Harmony",
                "message": "Love creates beautiful patterns across your entire brain, lighting up regions responsible for joy, attachment, and pure bliss! 🌟🧠"
            },
            {
                "title": "Infinite Connection",
                "message": "Neural pathways of love grow stronger with every shared moment, laugh, and gentle touch. Your love literally rewires your brain for happiness! 💫💖"
            },
            {
                "title": "Beautiful Chemistry",
                "message": "Thinking of someone special releases dopamine, oxytocin, and serotonin - nature's own love potion that makes everything more beautiful! 🧪✨"
            }
        ]

# --- Initialize Data ---
@st.cache_resource
def get_network_data():
    return NeuralNetworkData()

network_data = get_network_data()

# --- Session State ---
if 'current_theme' not in st.session_state:
    st.session_state.current_theme = "🌸 Cherry Blossom Dreams"
if 'animation_playing' not in st.session_state:
    st.session_state.animation_playing = False
if 'network_complexity' not in st.session_state:
    st.session_state.network_complexity = 1.0

# --- Magical Header ---
st.markdown('<h1 class="magical-title">Neural Net of Affection</h1>', unsafe_allow_html=True)
st.markdown('<p class="enchanting-subtitle">✨ Mapping the ethereal pathways from heart to soul 💫</p>', unsafe_allow_html=True)

# --- Enhanced Sidebar ---
with st.sidebar:
    st.markdown("# 🎛️ Love Control Center")
    
    # Theme Selection Panel
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.markdown("### 🎨 Choose Your Love Theme")
    
    # Custom theme selector with previews
    for theme_name, theme_data in network_data.themes.items():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f'<div class="theme-color-dot" style="background: {theme_data["dot_color"]}"></div>', unsafe_allow_html=True)
        with col2:
            if st.button(theme_name, key=f"theme_{theme_name}"):
                st.session_state.current_theme = theme_name
        
        if st.session_state.current_theme == theme_name:
            st.markdown(f"*{theme_data['description']}*")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Network Configuration Panel
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.markdown("### 🌟 Network Settings")
    
    # Category selection
    selected_category = st.selectbox(
        "💝 Choose Your Love Story:",
        list(network_data.input_categories.keys()),
        help="Select the type of beautiful moments that make your heart flutter"
    )
    
    # Animation controls
    st.markdown("#### 🎬 Animation Controls")
    animation_speed = st.slider(
        "⏱️ Animation Speed:",
        min_value=300,
        max_value=2000,
        value=800,
        step=100,
        help="Control the flow of love through the network"
    )
    
    # Network complexity
    network_complexity = st.slider(
        "🧠 Network Complexity:",
        min_value=0.5,
        max_value=2.0,
        value=st.session_state.network_complexity,
        step=0.1,
        help="Adjust the intricacy of emotional connections"
    )
    st.session_state.network_complexity = network_complexity
    
    # Love intensity
    intensity = st.slider(
        "💕 Love Intensity:",
        min_value=0.3,
        max_value=2.5,
        value=1.2,
        step=0.1,
        help="How deeply does your heart feel?"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive Controls Panel
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.markdown("### 🎮 Interactive Controls")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌟 Animate", key="animate_btn"):
            st.session_state.animation_playing = True
            st.balloons()
    
    with col2:
        if st.button("⏸️ Pause", key="pause_btn"):
            st.session_state.animation_playing = False
    
    if st.button("💝 Send Love Energy", key="love_energy"):
        st.balloons()
        st.success("💖 Love energy sent through the neural network! 💖")
    
    if st.button("🔄 Reset Network", key="reset_btn"):
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Wholesome message section
    current_message = random.choice(network_data.wholesome_messages)
    st.markdown(f"""
    <div class="wholesome-message">
        <h3>{current_message['title']}</h3>
        <p>{current_message['message']}</p>
    </div>
    """, unsafe_allow_html=True)

# --- Enhanced Figure Creation ---
@st.cache_data
def create_enhanced_network(inputs, hidden, output, theme, speed, intensity_val, complexity):
    # Get theme colors
    theme_data = network_data.themes[theme]
    
    # Calculate positions with improved readability
    input_count = len(inputs)
    hidden_count = len(hidden)
    output_count = len(output)
    
    # More readable positioning
    x_in = [-2.0] * input_count
    y_in = np.linspace(0.1, 0.9, input_count)
    
    x_hid = [0.0] * hidden_count
    y_hid = np.linspace(0.05, 0.95, hidden_count)
    
    x_out = [2.0] * output_count
    y_out = np.linspace(0.3, 0.7, output_count)

    fig = go.Figure()
    
    # Add subtle background effects
    for i in range(int(5 * complexity)):
        fig.add_shape(
            type="circle",
            x0=random.uniform(-2.5, 2.5), y0=random.uniform(0, 1),
            x1=random.uniform(-2.5, 2.5), y1=random.uniform(0, 1),
            fillcolor=theme_data["glow"],
            line=dict(color="rgba(0,0,0,0)", width=0),
            opacity=0.05
        )
    
    # Create enhanced connections with better visibility
    for i, (xi, yi) in enumerate(zip(x_in, y_in)):
        for j, (xh, yh) in enumerate(zip(x_hid, y_hid)):
            strength = np.random.uniform(0.4, 1.2) * intensity_val * complexity
            
            # Improved connection visualization
            fig.add_shape(
                type="line",
                x0=xi + 0.2, y0=yi, x1=xh - 0.15, y1=yh,
                line=dict(
                    color=theme_data["edge_color"],
                    width=max(1, strength * 2.5),
                    dash="solid" if strength > 0.8 else "dot"
                ),
                opacity=min(strength * 0.8, 0.9)
            )
    
    # Hidden to output connections
    for xh, yh in zip(x_hid, y_hid):
        for xo, yo in zip(x_out, y_out):
            strength = np.random.uniform(0.8, 1.8) * intensity_val * complexity
            fig.add_shape(
                type="line",
                x0=xh + 0.15, y0=yh, x1=xo - 0.2, y1=yo,
                line=dict(
                    color=theme_data["edge_color"],
                    width=max(2, strength * 2),
                    dash="solid"
                ),
                opacity=min(strength * 0.7, 0.9)
            )
    
    # Enhanced node visualizations with better text readability
    base_input_size = 25
    base_hidden_size = 30
    base_output_size = 40
    
    # Input layer - more readable
    fig.add_trace(go.Scatter(
        x=x_in, y=y_in,
        mode="markers+text",
        marker=dict(
            size=[base_input_size + i*3 for i in range(input_count)],
            color=theme_data["input_color"],
            line=dict(color="white", width=3),
            symbol="circle",
            opacity=0.95
        ),
        text=inputs,
        textposition="middle right",
        textfont=dict(
            color="white",
            size=13,
            family="Inter, sans-serif"
        ),
        name="✨ Beautiful Inputs",
        hovertemplate="<b>%{text}</b><br>💕 Input Layer<br>Where magic begins<extra></extra>",
        hoverlabel=dict(bgcolor=theme_data["input_color"], font_color="white")
    ))
    
    # Hidden layer - enhanced visibility
    fig.add_trace(go.Scatter(
        x=x_hid, y=y_hid,
        mode="markers+text",
        marker=dict(
            size=[base_hidden_size + i*2 for i in range(hidden_count)],
            color=theme_data["hidden_color"],
            line=dict(color="white", width=3),
            symbol="diamond",
            opacity=0.95
        ),
        text=hidden,
        textposition="top center",
        textfont=dict(
            color="white",
            size=12,
            family="Inter, sans-serif"
        ),
        name="💫 Emotional Processing",
        hovertemplate="<b>%{text}</b><br>🌟 Hidden Layer<br>Where feelings transform<extra></extra>",
        hoverlabel=dict(bgcolor=theme_data["hidden_color"], font_color="white")
    ))
    
    # Output layer - most prominent
    fig.add_trace(go.Scatter(
        x=x_out, y=y_out,
        mode="markers+text",
        marker=dict(
            size=[base_output_size + i*8 for i in range(output_count)],
            color=theme_data["output_color"],
            line=dict(color="gold", width=4),
            symbol="star",
            opacity=1.0
        ),
        text=output,
        textposition="middle left",
        textfont=dict(
            color="white",
            size=15,
            family="Inter, sans-serif",
            shadow="2px 2px 4px rgba(0,0,0,0.5)"
        ),
        name="💖 Pure Love",
        hovertemplate="<b>%{text}</b><br>👑 Output Layer<br>The ultimate expression<extra></extra>",
        hoverlabel=dict(bgcolor=theme_data["output_color"], font_color="white")
    ))
    
    # Enhanced layout with better readability
    fig.update_layout(
        title={
            "text": f"💫 {selected_category} → {theme} Neural Symphony 💫",
            "x": 0.5,
            "font": {"size": 20, "color": "white", "family": "Inter"},
            "pad": {"t": 20}
        },
        showlegend=True,
        legend=dict(
            x=0.02, y=0.98,
            bgcolor="rgba(0,0,0,0.8)",
            bordercolor=theme_data["edge_color"],
            borderwidth=2,
            font=dict(color="white", family="Inter", size=12)
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", family="Inter"),
        xaxis=dict(
            showgrid=False, zeroline=False, showticklabels=False,
            range=[-3, 3], fixedrange=True
        ),
        yaxis=dict(
            showgrid=False, zeroline=False, showticklabels=False,
            range=[-0.1, 1.1], fixedrange=True
        ),
        margin=dict(l=40, r=40, t=80, b=40),
        height=650,
        hovermode="closest"
    )
    
    return fig

# --- Main Content Area ---
col1, col2 = st.columns([3, 1])

with col1:
    # Get current data
    current_inputs = network_data.input_categories[selected_category]
    
    # Create and display the enhanced network
    fig = create_enhanced_network(
        current_inputs,
        network_data.hidden_emotions,
        network_data.love_expressions,
        st.session_state.current_theme,
        animation_speed,
        intensity,
        network_complexity
    )
    
    st.plotly_chart(fig, use_container_width=True, key="enhanced_neural_network")

with col2:
    st.markdown("### 📊 Love Analytics")
    
    # Beautiful metrics with theme colors
    theme_data = network_data.themes[st.session_state.current_theme]
    
    st.markdown(f"""
    <div class="metric-card" style="border-color: {theme_data['dot_color']};">
        <h4>💝 Input Signals</h4>
        <h2>{len(network_data.input_categories[selected_category])}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card" style="border-color: {theme_data['dot_color']};">
        <h4>🌟 Emotions</h4>
        <h2>{len(network_data.hidden_emotions)}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card" style="border-color: {theme_data['dot_color']};">
        <h4>💖 Love Output</h4>
        <h2>{len(network_data.love_expressions)}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Network status
    st.markdown("### 💫 Network Status")
    
    # Love intensity progress
    emotional_intensity = min(100, int(intensity * 40))
    st.progress(emotional_intensity / 100, text=f"💕 Love Intensity: {emotional_intensity}%")
    
    # Complexity indicator
    complexity_percent = min(100, int(network_complexity * 50))
    st.progress(complexity_percent / 100, text=f"🧠 Neural Complexity: {complexity_percent}%")
    
    # Theme indicator
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px; margin: 1rem 0;">
        <div style="width: 30px; height: 30px; background: {theme_data['dot_color']}; border-radius: 50%; margin: 0 auto 10px; border: 2px solid white;"></div>
        <strong>Current Theme</strong><br>
        <em>{st.session_state.current_theme}</em>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive love wisdom
    if st.button("🔮 Generate Love Wisdom", key="wisdom_btn"):
        wisdom_messages = [
            "Love is the only force capable of transforming an enemy into a friend 💫",
            "In your light, I learn how to love 🌟",
            "Love is not just looking at each other, it's looking in the same direction 👫",
            "The best thing to hold onto in life is each other 🤗",
            "Love is a friendship set to music 🎵",
            "Where there is love, there is life 🌱",
            "Love is the bridge between two hearts 🌉",
            "True love stories never have endings 📖💕",
            "Love recognizes no barriers 🚫❤️",
            "In all the world, there is no heart for me like yours 💝"
        ]
        st.info(f"✨ {random.choice(wisdom_messages)}")

# --- Enhanced Information Sections ---
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 How This Network Works")
    st.markdown("""
    <div class="info-section">
        <h3>💡 Input Layer (Left)</h3>
        <p>Beautiful moments and experiences flow into the network. Each input represents a special memory, gesture, or feeling that sparks joy in your heart.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-section">
        <h3>🧠 Hidden Layer (Center)</h3>
        <p>Your emotional processing center where different feelings combine, amplify, and transform. This is where the magic of love happens - where simple moments become profound emotions.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🔬 The Science of Love")
    st.markdown("""
    <div class="info-section">
        <h3>💖 Output Layer (Right)</h3>
        <p>The ultimate expression of your love - pure, concentrated, and infinitely beautiful. This is where all the neural pathways converge to create something greater than the sum of its parts.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-section">
        <h3>🌈 Connection Strength</h3>
        <p>The thickness and opacity of connections represent the strength of emotional bonds. Stronger connections (thicker lines) indicate more powerful pathways of affection.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Interactive Message Center ---
st.markdown("### 💌 Interactive Love Messages")

message_col1, message_col2, message_col3 = st.columns(3)

with message_col1:
    if st.button("💝 Neural Love Fact", key="neural_fact"):
        facts = [
            "Your pupils dilate by up to 45% when you look at someone you love - your brain wants to take in more of their beauty! 👁️✨",
            "Love activates the same reward pathways as chocolate, but with 1000x more intensity! 🍫💕",
            "When couples hold hands, their heartbeats synchronize within 3 minutes - true neural harmony! 👫💓",
            "Your brain creates a unique 'love map' more detailed than any GPS! 🗺️💖",
            "Love literally grows your brain - empathy areas physically expand when you're in love! 🧠💕"
        ]
        st.success(random.choice(facts))

with message_col2:
    if st.button("🌟 Wholesome Quote", key="wholesome_quote"):
        quotes = [
            "Love is composed of a single soul inhabiting two bodies 💫",
            "The best love is the kind that awakens the soul 🌅",
            "Love is not finding someone to live with, it's finding someone you can't live without 💝",
            "In your smile, I see something more beautiful than the stars ⭐",
            "Love is the master key that opens the gates of happiness 🗝️"
        ]
        st.info(random.choice(quotes))

with message_col3:
    if st.button("🎨 Theme Inspiration", key="theme_inspiration"):
        current_theme_data = network_data.themes[st.session_state.current_theme]
        inspirations = {
            "🌸 Cherry Blossom Dreams": "Like delicate petals dancing in spring breeze, your love brings gentle beauty to every moment 🌸",
            "🌙 Moonlit Romance": "Under silver moonbeams, your love illuminates the darkest nights with ethereal grace 🌙",
            "🌊 Ocean Serenity": "Deep as ocean tides, your love flows with endless serenity and peaceful strength 🌊",
            "🌈 Rainbow Hearts": "Vibrant as a rainbow after rain, your love paints the world in brilliant colors 🌈",
            "🌅 Golden Sunrise": "Warm as morning light, your love brings the promise of beautiful new beginnings 🌅",
            "💎 Crystal Clarity": "Pure as crystal light, your love shines with perfect clarity and timeless beauty 💎"
        }
        st.success(inspirations.get(st.session_state.current_theme, "Your love theme radiates pure magic! ✨"))

# --- Beautiful Footer ---
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(255, 105, 180, 0.1) 0%, rgba(199, 21, 133, 0.1) 100%); border-radius: 25px; border: 1px solid rgba(255, 105, 180, 0.2); backdrop-filter: blur(10px); box-shadow: 0 10px 30px rgba(255, 105, 180, 0.1);">
    <em style="color: #ffb6c1; font-size: 1.3rem; font-weight: 400; text-shadow: 0 0 15px rgba(255, 182, 193, 0.4); display: block; animation: gentleGlow 3s ease-in-out infinite alternate;">
        "In the vast neural network of existence, love is the most beautiful algorithm - 
        one that transforms simple inputs into infinite joy, and makes every synapse sing with the melody of two hearts becoming one 💕✨"
    </em>
    <br><br>
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 1rem;">
        <div style="width: 20px; height: 20px; background: {network_data.themes[st.session_state.current_theme]['dot_color']}; border-radius: 50%; border: 2px solid white; animation: gentlePulse 2s ease-in-out infinite;"></div>
        <span style="color: #ff69b4;">Current Theme: {st.session_state.current_theme}</span>
    </div>
</div>
""", unsafe_allow_html=True)
