#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neural Net of Affection
Streamlit app with a simplified neural network of love for clarity.
"""

import streamlit as st
try:
    import plotly.graph_objects as go
except ImportError:
    st.error("Plotly is not installed. Please install it using `pip install plotly`.")
    st.stop()
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Neural Net of Affection 🌸🧠💖",
    layout="wide"
)

st.write("✅ App is running")
st.title("Neural Net of Affection 🌸🧠💖")

# 1. Define a reduced set of neurons for visibility
input_nodes = [
    "Her smile",
    "Her laugh",
    "Her sleepy goodnights",
    "Her random ‘I thought of you’ moments",
    "Her eyes when they light up with joy"
]
hidden_nodes = [
    "Butterflies",
    "Calm",
    "Euphoria",
    "Gratitude",
    "Inspiration",
    "Daydreams"
]
output_nodes = ["I’m in love with you 💘"]

# 2. Build & Animate Figure
@st.cache_data(show_spinner=True)
def build_figure(inputs, hidden, output):
    # Coordinates
    x_in = [0] * len(inputs)
    y_in = np.linspace(0, 1, len(inputs))
    x_hid = [1] * len(hidden)
    y_hid = np.linspace(0, 1, len(hidden))
    x_out = [2] * len(output)
    y_out = [0.5] * len(output)

    fig = go.Figure()
    # Draw edges
    for xi, yi in zip(x_in, y_in):
        for xh, yh in zip(x_hid, y_hid):
            fig.add_shape(
                type="line", x0=xi, y0=yi, x1=xh, y1=yh,
                line=dict(color="lightpink", width=1)
            )
    for xh, yh in zip(x_hid, y_hid):
        for xo, yo in zip(x_out, y_out):
            fig.add_shape(
                type="line", x0=xh, y0=yh, x1=xo, y1=yo,
                line=dict(color="lightpink", width=1)
            )
    # Nodes
    fig.add_trace(go.Scatter(
        x=x_in, y=y_in, mode="markers+text",
        marker=dict(size=18, color="#FFB6C1"), text=inputs,
        textposition="middle left"
    ))
    fig.add_trace(go.Scatter(
        x=x_hid, y=y_hid, mode="markers+text",
        marker=dict(size=22, color="#FF69B4"), text=hidden,
        textposition="middle left"
    ))
    fig.add_trace(go.Scatter(
        x=x_out, y=y_out, mode="markers+text",
        marker=dict(size=28, color="#FF1493"), text=output,
        textposition="middle left"
    ))

    # Animation frames
    frames = [
        go.Frame(
            name="inputs", data=[
                go.Scatter(marker=dict(size=24, color="#FF1493"), x=x_in, y=y_in, text=inputs, textposition="middle left"),
                go.Scatter(marker=dict(size=22, color="#FF69B4"), x=x_hid, y=y_hid, text=hidden, textposition="middle left"),
                go.Scatter(marker=dict(size=28, color="#FF1493"), x=x_out, y=y_out, text=output, textposition="middle left")
            ]
        ),
        go.Frame(
            name="hidden", data=[
                go.Scatter(marker=dict(size=18, color="#FFB6C1"), x=x_in, y=y_in, text=inputs, textposition="middle left"),
                go.Scatter(marker=dict(size=28, color="#FF1493"), x=x_hid, y=y_hid, text=hidden, textposition="middle left"),
                go.Scatter(marker=dict(size=28, color="#FF1493"), x=x_out, y=y_out, text=output, textposition="middle left")
            ]
        ),
        go.Frame(
            name="output", data=[
                go.Scatter(marker=dict(size=18, color="#FFB6C1"), x=x_in, y=y_in, text=inputs, textposition="middle left"),
                go.Scatter(marker=dict(size=22, color="#FF69B4"), x=x_hid, y=y_hid, text=hidden, textposition="middle left"),
                go.Scatter(marker=dict(size=32, color="#FF0000"), x=x_out, y=y_out, text=output, textposition="middle left")
            ]
        )
    ]
    fig.frames = frames
    # Controls
    fig.update_layout(
        updatemenus=[{
            "type": "buttons", "showactive": False,
            "buttons": [{"label": "▶ Play", "method": "animate", "args": [None, {"frame": {"duration": 800, "redraw": True}, "fromcurrent": True}]}]
        }],
        sliders=[{
            "steps": [{"method": "animate", "args": [[f.name], {"frame": {"duration": 800, "redraw": True}, "mode": "immediate"}], "label": f.name} for f in frames],
            "currentvalue": {"prefix": "Stage: "}
        }]
    )
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.5, 2.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.1, 1.1]),
        plot_bgcolor="white", margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig

# Display
fig = build_figure(input_nodes, hidden_nodes, output_nodes)
st.plotly_chart(fig, use_container_width=True)
