import streamlit as st
import av
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
from ultralytics import YOLO

st.title("🔥 D3T4CT_01 - WORKING!")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

class DetectionProcessor:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
    
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        results = self.model(img)
        return av.VideoFrame.from_ndarray(results[0].plot(), format="bgr24")

webrtc_streamer(
    key="detection",
    video_processor_factory=DetectionProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={
        "video": {"width": 640, "height": 480, "frameRate": 30}
    }
)
