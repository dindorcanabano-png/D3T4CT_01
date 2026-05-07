import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import cv2
import numpy as np

st.title("✅ D3T4CT_01 - BASE WORKING")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

class TestProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        # Simple test - draw rectangle
        cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(
    key="test",
    video_processor_factory=TestProcessor,
    rtc_configuration=RTC_CONFIGURATION
)
