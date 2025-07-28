#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Neural Net of Affection
A beautiful, interactive Streamlit app visualizing the neural pathways of love
with enhanced styling, animations, and user interaction.
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
import random

# --- Page Configuration ---
st.set_page_config(
    page_title="Neural Net of Affection 🌸🧠💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Enhanced Dark Theme Styling ---
st.markdown("""
<style>
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a0a1a 50%, #0c0c0c 100%);
        color: #ffffff;
    }
    
    /* Custom title styling */
    .main-title {
        text-align: center;
        font-size: 3rem;
        background: linear-gradient(45deg, #ff69b4, #ff1493, #ff69b4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 2rem;
        text-shadow: 0 0 20px rgba(255, 105, 180, 0.3);
    }
    
    /* Subtitle styling */
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #ffb6c1;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #1a1a2e;
        border-right: 2px solid #ff69b4;
    }
    
    /* Custom buttons */
    .stButton > button {
        background: linear-gradient(45deg, #ff69b4, #ff1493);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
    }
    
    /* Metrics styling */
    .metric-card {
        background: rgba(255, 105, 180, 0.1);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 105, 180, 0.3);
        text-align: center;
        margin: 0.5rem 0;
    }
    
    /* Animation keyframes */
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }
    
    .pulsing {
        animation: pulse 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

# --- Enhanced Data Structure ---
class NeuralNetworkData:
    def __init__(self):
        self.input_categories = {
            "Visual Moments": [
                "Her radiant smile 😊",
                "The way her eyes sparkle ✨",
                "Her sleepy morning face 😴",
                "When she laughs at my jokes 😂",
                "Her focused concentration look 🤔"
            ],
            "Emotional Connections": [
                "Her comforting hugs 🤗",
                "Late night deep conversations 🌙",
                "Her random 'thinking of you' texts 📱",
                "The way she listens 👂",
                "Her empathy and understanding 💙"
            ],
            "Shared Experiences": [
                "Our inside jokes 😄",
                "Dancing together 💃",
                "Quiet moments of togetherness 🕯️",
                "Adventure planning sessions 🗺️",
                "Supporting each other's dreams 🌟"
            ]
        }
        
        self.hidden_emotions = [
            "Pure Joy 🌈",
            "Deep Peace ☮️",
            "Butterflies 🦋",
            "Gratitude 🙏",
            "Inspiration ⚡",
            "Wonder ✨",
            "Comfort 🛋️",
            "Excitement 🎉"
        ]
        
        self.love_expressions = [
            "I'm completely in love with you 💘",
            "You are my everything 🌍",
            "My heart belongs to you 💖"
        ]

# --- Initialize Data ---
@st.cache_resource
def get_network_data():
    return NeuralNetworkData()

network_data = get_network_data()

# --- Header Section ---
st.markdown('<h1 class="main-title">Neural Net of Affection 🌸🧠💖</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Mapping the beautiful pathways from her actions to my heart</p>', unsafe_allow_html=True)

# --- Sidebar Controls ---
st.sidebar.markdown("### 🎛️ Network Controls")

# Category selection
selected_category = st.sidebar.selectbox(
    "Choose Input Category:",
    list(network_data.input_categories.keys())
)

# Animation speed
animation_speed = st.sidebar.slider(
    "Animation Speed (ms):",
    min_value=500,
    max_value=2000,
    value=1000,
    step=100
)

# Color theme selection
color_theme = st.sidebar.selectbox(
    "Color Theme:",
    ["Pink Love", "Purple Dreams", "Blue Serenity", "Rainbow Joy"]
)

# Network intensity
intensity = st.sidebar.slider(
    "Emotional Intensity:",
    min_value=0.1,
    max_value=2.0,
    value=1.0,
    step=0.1
)

# --- Color Theme Configuration ---
def get_color_scheme(theme, intensity_factor):
    themes = {
        "Pink Love": {
            "input": f"rgba(255, 182, 193, {0.8 * intensity_factor})",
            "hidden": f"rgba(255, 105, 180, {0.9 * intensity_factor})",
            "output": f"rgba(255, 20, 147, {1.0 * intensity_factor})",
            "edges": f"rgba(255, 255, 255, {0.6 * intensity_factor})"
        },
        "Purple Dreams": {
            "input": f"rgba(221, 160, 221, {0.8 * intensity_factor})",
            "hidden": f"rgba(147, 112, 219, {0.9 * intensity_factor})",
            "output": f"rgba(138, 43, 226, {1.0 * intensity_factor})",
            "edges": f"rgba(230, 230, 250, {0.6 * intensity_factor})"
        },
        "Blue Serenity": {
            "input": f"rgba(173, 216, 230, {0.8 * intensity_factor})",
            "hidden": f"rgba(100, 149, 237, {0.9 * intensity_factor})",
            "output": f"rgba(65, 105, 225, {1.0 * intensity_factor})",
            "edges": f"rgba(240, 248, 255, {0.6 * intensity_factor})"
        },
        "Rainbow Joy": {
            "input": f"rgba(255, 99, 132, {0.8 * intensity_factor})",
            "hidden": f"rgba(54, 162, 235, {0.9 * intensity_factor})",
            "output": f"rgba(255, 206, 86, {1.0 * intensity_factor})",
            "edges": f"rgba(255, 255, 255, {0.6 * intensity_factor})"
        }
    }
    return themes[theme]

# --- Enhanced Figure Building ---
@st.cache_data
def build_enhanced_figure(inputs, hidden, output, colors, speed, intensity_val):
    # Calculate positions with better spacing
    input_count = len(inputs)
    hidden_count = len(hidden)
    output_count = len(output)
    
    # Dynamic positioning based on node count
    x_in = [-0.5] * input_count
    y_in = np.linspace(0.1, 0.9, input_count)
    x_hid = [1] * hidden_count
    y_hid = np.linspace(0.05, 0.95, hidden_count)
    x_out = [2.5] * output_count
    y_out = np.linspace(0.4, 0.6, output_count)

    fig = go.Figure()
    
    # Add animated background pulse effect
    fig.add_shape(
        type="circle",
        x0=-1, y0=-0.2, x1=3.5, y1=1.2,
        fillcolor="rgba(255, 105, 180, 0.02)",
        line=dict(color="rgba(255, 105, 180, 0.1)", width=1)
    )
    
    # Draw enhanced edges with varying thickness
    edge_weights = np.random.uniform(0.5, 2.0, input_count * hidden_count)
    edge_idx = 0
    
    for xi, yi in zip(x_in, y_in):
        for xh, yh in zip(x_hid, y_hid):
            weight = edge_weights[edge_idx] * intensity_val
            fig.add_shape(
                type="line", x0=xi+0.1, y0=yi, x1=xh-0.1, y1=yh,
                line=dict(color=colors["edges"], width=weight, dash="dot" if weight < 1 else "solid")
            )
            edge_idx += 1
    
    for xh, yh in zip(x_hid, y_hid):
        for xo, yo in zip(x_out, y_out):
            weight = np.random.uniform(1.0, 3.0) * intensity_val
            fig.add_shape(
                type="line", x0=xh+0.1, y0=yh, x1=xo-0.1, y1=yo,
                line=dict(color=colors["edges"], width=weight)
            )
    
    # Enhanced nodes with better sizing and effects
    base_input_size = 15
    base_hidden_size = 18
    base_output_size = 25
    
    # Input layer
    fig.add_trace(go.Scatter(
        x=x_in, y=y_in, mode="markers+text",
        marker=dict(
            size=[base_input_size + i*2 for i in range(input_count)],
            color=colors["input"],
            line=dict(color="white", width=2),
            symbol="circle"
        ),
        text=inputs,
        textposition="middle right",
        textfont=dict(color="white", size=10, family="Arial Black"),
        name="Inputs",
        hovertemplate="<b>%{text}</b><br>Input Layer<extra></extra>"
    ))
    
    # Hidden layer
    fig.add_trace(go.Scatter(
        x=x_hid, y=y_hid, mode="markers+text",
        marker=dict(
            size=[base_hidden_size + i for i in range(hidden_count)],
            color=colors["hidden"],
            line=dict(color="white", width=2),
            symbol="diamond"
        ),
        text=hidden,
        textposition="middle right",
        textfont=dict(color="white", size=11, family="Arial Black"),
        name="Emotions",
        hovertemplate="<b>%{text}</b><br>Hidden Layer<extra></extra>"
    ))
    
    # Output layer
    fig.add_trace(go.Scatter(
        x=x_out, y=y_out, mode="markers+text",
        marker=dict(
            size=[base_output_size + i*3 for i in range(output_count)],
            color=colors["output"],
            line=dict(color="white", width=3),
            symbol="star"
        ),
        text=output,
        textposition="middle right",
        textfont=dict(color="white", size=12, family="Arial Black"),
        name="Love Output",
        hovertemplate="<b>%{text}</b><br>Output Layer<extra></extra>"
    ))
    
    # Create animation frames
    frames = []
    
    # Frame 1: Input activation
    frames.append(go.Frame(
        name="input_activation",
        data=[
            go.Scatter(
                x=x_in, y=y_in, mode="markers+text",
                marker=dict(size=[s*1.5 for s in [base_input_size + i*2 for i in range(input_count)]], 
                           color=colors["output"], line=dict(color="yellow", width=3)),
                text=inputs, textposition="middle right",
                textfont=dict(color="white", size=10, family="Arial Black")
            ),
            go.Scatter(
                x=x_hid, y=y_hid, mode="markers+text",
                marker=dict(size=[base_hidden_size + i for i in range(hidden_count)], color=colors["hidden"]),
                text=hidden, textposition="middle right",
                textfont=dict(color="white", size=11, family="Arial Black")
            ),
            go.Scatter(
                x=x_out, y=y_out, mode="markers+text",
                marker=dict(size=[base_output_size + i*3 for i in range(output_count)], color=colors["output"]),
                text=output, textposition="middle right",
                textfont=dict(color="white", size=12, family="Arial Black")
            )
        ]
    ))
    
    # Frame 2: Hidden layer activation
    frames.append(go.Frame(
        name="hidden_activation",
        data=[
            go.Scatter(
                x=x_in, y=y_in, mode="markers+text",
                marker=dict(size=[base_input_size + i*2 for i in range(input_count)], color=colors["input"]),
                text=inputs, textposition="middle right",
                textfont=dict(color="white", size=10, family="Arial Black")
            ),
            go.Scatter(
                x=x_hid, y=y_hid, mode="markers+text",
                marker=dict(size=[s*1.5 for s in [base_hidden_size + i for i in range(hidden_count)]], 
                           color=colors["output"], line=dict(color="yellow", width=3)),
                text=hidden, textposition="middle right",
                textfont=dict(color="white", size=11, family="Arial Black")
            ),
            go.Scatter(
                x=x_out, y=y_out, mode="markers+text",
                marker=dict(size=[base_output_size + i*3 for i in range(output_count)], color=colors["output"]),
                text=output, textposition="middle right",
                textfont=dict(color="white", size=12, family="Arial Black")
            )
        ]
    ))
    
    # Frame 3: Output activation
    frames.append(go.Frame(
        name="output_activation",
        data=[
            go.Scatter(
                x=x_in, y=y_in, mode="markers+text",
                marker=dict(size=[base_input_size + i*2 for i in range(input_count)], color=colors["input"]),
                text=inputs, textposition="middle right",
                textfont=dict(color="white", size=10, family="Arial Black")
            ),
            go.Scatter(
                x=x_hid, y=y_hid, mode="markers+text",
                marker=dict(size=[base_hidden_size + i for i in range(hidden_count)], color=colors["hidden"]),
                text=hidden, textposition="middle right",
                textfont=dict(color="white", size=11, family="Arial Black")
            ),
            go.Scatter(
                x=x_out, y=y_out, mode="markers+text",
                marker=dict(size=[s*2 for s in [base_output_size + i*3 for i in range(output_count)]], 
                           color="red", line=dict(color="gold", width=4)),
                text=output, textposition="middle right",
                textfont=dict(color="white", size=14, family="Arial Black")
            )
        ]
    ))
    
    fig.frames = frames
    
    # Enhanced controls
    fig.update_layout(
        updatemenus=[{
            "type": "buttons",
            "showactive": False,
            "x": 0.02,
            "y": 1.02,
            "buttons": [
                {
                    "label": "▶️ Activate Network",
                    "method": "animate",
                    "args": [None, {
                        "frame": {"duration": speed, "redraw": True},
                        "fromcurrent": True,
                        "transition": {"duration": speed//2}
                    }]
                },
                {
                    "label": "⏸️ Pause",
                    "method": "animate",
                    "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}]
                }
            ]
        }],
        sliders=[{
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 12, "color": "white"},
                "prefix": "Stage: ",
                "visible": True,
                "xanchor": "right"
            },
            "pad": {"b": 10, "t": 50},
            "len": 0.9,
            "x": 0.05,
            "y": 0,
            "steps": [
                {
                    "args": [[f.name], {
                        "frame": {"duration": speed, "redraw": True},
                        "mode": "immediate",
                        "transition": {"duration": speed//2}
                    }],
                    "label": f.name.replace("_", " ").title(),
                    "method": "animate"
                } for f in frames
            ]
        }]
    )
    
    # Final layout
    fig.update_layout(
        title={
            "text": f"Neural Pathways of Love - {selected_category}",
            "x": 0.5,
            "font": {"size": 16, "color": "white"}
        },
        showlegend=True,
        legend=dict(
            x=0.02, y=0.98,
            bgcolor="rgba(0,0,0,0.5)",
            bordercolor="rgba(255,105,180,0.5)",
            borderwidth=1,
            font=dict(color="white")
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", family="Arial"),
        xaxis=dict(
            showgrid=False, zeroline=False, showticklabels=False,
            range=[-1, 3.5], fixedrange=True
        ),
        yaxis=dict(
            showgrid=False, zeroline=False, showticklabels=False,
            range=[-0.1, 1.1], fixedrange=True
        ),
        margin=dict(l=20, r=20, t=80, b=60),
        height=600
    )
    
    return fig

# --- Main Content ---
col1, col2 = st.columns([3, 1])

with col1:
    # Get current inputs based on selection
    current_inputs = network_data.input_categories[selected_category]
    colors = get_color_scheme(color_theme, intensity)
    
    # Build and display figure
    fig = build_enhanced_figure(
        current_inputs,
        network_data.hidden_emotions,
        network_data.love_expressions,
        colors,
        animation_speed,
        intensity
    )
    
    st.plotly_chart(fig, use_container_width=True, key="neural_network")

with col2:
    st.markdown("### 📊 Network Stats")
    
    # Display metrics
    st.markdown(f"""
    <div class="metric-card">
        <h4>Input Neurons</h4>
        <h2>{len(network_data.input_categories[selected_category])}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <h4>Hidden Emotions</h4>
        <h2>{len(network_data.hidden_emotions)}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="metric-card">
        <h4>Love Output</h4>
        <h2>{len(network_data.love_expressions)}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Random love fact
    if st.button("💝 Random Love Fact"):
        facts = [
            "Love activates the same brain regions as addiction! 🧠",
            "Your heart literally skips a beat when you see someone you love 💓",
            "Couples in love synchronize their heartbeats when they look into each other's eyes 👁️",
            "Love reduces stress and boosts your immune system! 🛡️",
            "The average person falls in love 7 times before marriage 💕"
        ]
        st.info(random.choice(facts))

# --- Footer Section ---
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎯 Network Summary")
    st.write(f"Currently visualizing **{selected_category}** inputs flowing through emotional processing to create the beautiful output of love.")

with col2:
    st.markdown("### 🔬 How It Works")
    st.write("Each input triggers multiple emotional responses in the hidden layer, which combine and amplify to produce the final expression of love.")

with col3:
    st.markdown("### 💡 Fun Fact")
    st.write("This neural network has infinite capacity for love - the more inputs you give it, the stronger the output becomes! 💖")

# Auto-refresh option
if st.sidebar.checkbox("🔄 Auto-refresh (every 10s)"):
    time.sleep(10)
    st.experimental_rerun()

st.markdown("""
<div style='text-align: center; margin-top: 2rem; padding: 1rem; 
            background: rgba(255, 105, 180, 0.1); border-radius: 10px;'>
    <em style='color: #ffb6c1; font-size: 1.1rem;'>
    "Love is not just a feeling, it's a beautiful neural symphony 🎵💕"
    </em>
</div>
""", unsafe_allow_html=True)
