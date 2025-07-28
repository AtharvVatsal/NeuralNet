#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neural Net of Affection
A Streamlit app that visualizes a neural network of love with animated forward pass.
"""

import streamlit as st
# Ensure Plotly is available
try:
    import plotly.graph_objects as go
except ImportError:
    st.error("Plotly is not installed. Please install it by running `pip install plotly`.")
    st.stop()
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="Neural Net of Affection 🌸🧠💖",
    layout="wide"
)

# --- Basic App Header ---
st.write("✅ Streamlit loaded successfully! If you see this, the app is running.")
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

# --- 2. Build & Animate Figure ---
@st.cache_data(show_spinner=True)
def build_animated_figure(input_nodes, hidden_nodes, output_nodes):
    # Coordinates
    x_input = [0] * len(input_nodes)
    y_input = np.linspace(0, 1, len(input_nodes))
    x_hidden = [1] * len(hidden_nodes)
    y_hidden = np.linspace(0, 1, len(hidden_nodes))
    x_output = [2] * len(output_nodes)
    y_output = [0.5] * len(output_nodes)

    # Initial figure with neutral colors
    fig = go.Figure()
    # Edges
    for xi, yi in zip(x_input, y_input):
        for xh, yh in zip(x_hidden, y_hidden):
            fig.add_shape(type="line", x0=xi, y0=yi, x1=xh, y1=yh,
                          line=dict(color="lightpink", width=1))
    for xh, yh in zip(x_hidden, y_hidden):
        for xo, yo in zip(x_output, y_output):
            fig.add_shape(type="line", x0=xh, y0=yh, x1=xo, y1=yo,
                          line=dict(color="lightpink", width=1))
    # Static node traces
    fig.add_trace(go.Scatter(x=x_input, y=y_input, mode="markers+text",
                             marker=dict(size=16, color="#FFC0CB"), text=input_nodes,
                             textposition="middle left", hoverinfo="text"))
    fig.add_trace(go.Scatter(x=x_hidden, y=y_hidden, mode="markers+text",
                             marker=dict(size=18, color="#FFB6C1"), text=hidden_nodes,
                             textposition="middle left", hoverinfo="text"))
    fig.add_trace(go.Scatter(x=x_output, y=y_output, mode="markers+text",
                             marker=dict(size=24, color="#FF69B4"), text=output_nodes,
                             textposition="middle left", hoverinfo="text"))

    # Create animation frames
    frames = []
    # Frame 1: activate inputs
    frames.append(go.Frame(
        name="activate_inputs",
        data=[
            go.Scatter(x=x_input, y=y_input, mode="markers+text",
                       marker=dict(size=20, color="#FF1493"), text=input_nodes, textposition="middle left"),
            go.Scatter(x=x_hidden, y=y_hidden, mode="markers+text",
                       marker=dict(size=18, color="#FFB6C1"), text=hidden_nodes, textposition="middle left"),
            go.Scatter(x=x_output, y=y_output, mode="markers+text",
                       marker=dict(size=24, color="#FF69B4"), text=output_nodes, textposition="middle left"),
        ]))
    # Frame 2: activate hidden
    frames.append(go.Frame(
        name="activate_hidden",
        data=[
            go.Scatter(x=x_input, y=y_input, mode="markers+text",
                       marker=dict(size=16, color="#FFC0CB"), text=input_nodes, textposition="middle left"),
            go.Scatter(x=x_hidden, y=y_hidden, mode="markers+text",
                       marker=dict(size=22, color="#FF1493"), text=hidden_nodes, textposition="middle left"),
            go.Scatter(x=x_output, y=y_output, mode="markers+text",
                       marker=dict(size=24, color="#FF69B4"), text=output_nodes, textposition="middle left"),
        ]))
    # Frame 3: activate output
    frames.append(go.Frame(
        name="activate_output",
        data=[
            go.Scatter(x=x_input, y=y_input, mode="markers+text",
                       marker=dict(size=16, color="#FFC0CB"), text=input_nodes, textposition="middle left"),
            go.Scatter(x=x_hidden, y=y_hidden, mode="markers+text",
                       marker=dict(size=18, color="#FFB6C1"), text=hidden_nodes, textposition="middle left"),
            go.Scatter(x=x_output, y=y_output, mode="markers+text",
                       marker=dict(size=28, color="#FF1493"), text=output_nodes, textposition="middle left"),
        ]))

    fig.frames = frames
    # Animation controls
    fig.update_layout(
        updatemenus=[dict(
            type="buttons", showactive=False,
            y=1.1, x=1.05, xanchor="right", yanchor="top",
            buttons=[dict(label="▶ Play", method="animate",
                          args=[None, {"frame": {"duration": 1000, "redraw": True},
                                       "fromcurrent": True, "transition": {"duration": 500}}])]
        )],
        sliders=[dict(
            steps=[dict(method="animate", args=[[f.name], {"frame": {"duration": 1000, "redraw": True}, "mode": "immediate"}], label=f.name) for f in frames],
            transition={"duration": 0}, x=0.1, y=0, currentvalue={"prefix": "Stage: "}, len=0.9
        )]
    )
    # Base layout
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.5, 2.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.1, 1.1]),
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

# --- 3. Display Animated Figure ---
fig = build_animated_figure(input_nodes, hidden_nodes, output_nodes)
st.plotly_chart(fig, use_container_width=True)
st.markdown(
    """
    *Animated forward pass: inputs light up, then feelings, then love blooms.*
    """
)
