import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import cv2
from ultralytics import YOLO
import numpy as np

st.title("🦾 D3T4CT_01")

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}] })

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        results = model(img)
        annotated = results[0].plot()
        return av.VideoFrame.from_ndarray(annotated, format="bgr24")

webrtc_streamer(key="example", 
                video_processor_factory=VideoProcessor,
                rtc_configuration=RTC_CONFIGURATION)
