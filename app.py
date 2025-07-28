# -*- coding: utf-8 -*-
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- Page Configuration and Basic Test ---
st.set_page_config(page_title="Neural Net of Affection", layout="wide")
st.write("✅ Streamlit loaded successfully! If you see this message, the app is running.")

# --- Title ---
st.title("Neural Net of Affection 🌸🧠💖")

# --- 1. Define Layers ---
input_nodes = [
    "Her smile", "Her voice", "Her support", "Her laugh", "Her texts",
    "Her sleepy goodnights", "Her excitement over little things", "Her caring reminders",
    "Her random 'I thought of you' moments", "Her way of listening like no one else does",
    "Her warmth when I feel low", "Her passion when she talks about what she loves",
    "Her happy rants", "Her teasing that makes me grin like a fool", "Her hugs (real or imagined)",
    "Her kindness, even on tough days", "Her eyes when they light up with joy",
    "Her courage to be vulnerable", "Her faith in me when I don’t have it myself",
    "Her voice when she says my name"
]

hidden_nodes = [
    "Butterflies", "Calm", "Longing", "Euphoria", "Gratitude", "Hope",
    "Daydreams", "Safe haven", "Heart skips", "Serotonin spike",
    "Gentle chaos", "Melting", "Inspiration", "Blushes",
    "Peace I didn’t know I needed", "Mental hugs", "Joy without cause",
    "A sense of home", "The urge to protect", "Soft distraction",
    "Heartbeat orchestra", "Waking up smiling", "Internal fireworks",
    "The ache of missing her even when she’s around", "Eyes that forget to blink when she’s talking"
]

output_nodes = ["I’m in love with you 💘"]

# --- 2. Compute Node Coordinates ---
x_input = [0] * len(input_nodes)
y_input = np.linspace(0, 1, len(input_nodes))

x_hidden = [1] * len(hidden_nodes)
y_hidden = np.linspace(0, 1, len(hidden_nodes))

x_output = [2] * len(output_nodes)
y_output = [0.5]

# --- 3. Build Plotly Figure ---
fig = go.Figure()

# Edges: input → hidden
for xi, yi in zip(x_input, y_input):
    for xh, yh in zip(x_hidden, y_hidden):
        fig.add_shape(type="line", x0=xi, y0=yi, x1=xh, y1=yh,
                      line=dict(color="lightpink", width=1))
# Edges: hidden → output
for xh, yh in zip(x_hidden, y_hidden):
    for xo, yo in zip(x_output, y_output):
        fig.add_shape(type="line", x0=xh, y0=yh, x1=xo, y1=yo,
                      line=dict(color="lightpink", width=1))

# Nodes: input layer
fig.add_trace(go.Scatter(
    x=x_input, y=y_input,
    mode="markers+text",
    marker=dict(size=16, color="#FFC0CB"),
    text=input_nodes,
    textposition="middle left",
    hoverinfo="text"
))

# Nodes: hidden layer
fig.add_trace(go.Scatter(
    x=x_hidden, y=y_hidden,
    mode="markers+text",
    marker=dict(size=18, color="#FFB6C1"),
    text=hidden_nodes,
    textposition="middle left",
    hoverinfo="text"
))

# Node: output layer
fig.add_trace(go.Scatter(
    x=x_output, y=y_output,
    mode="markers+text",
    marker=dict(size=24, color="#FF69B4"),
    text=output_nodes,
    textposition="middle left",
    hoverinfo="text"
))

# Layout styling
fig.update_layout(
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.5, 2.5]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.1, 1.1]),
    plot_bgcolor="white",
    margin=dict(l=20, r=20, t=40, b=20)
)

# Display
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
*Static visualization of the 'Neural Net of Affection' — inputs on left, feelings in middle, love on right.*
""")
