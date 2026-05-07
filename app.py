import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration, WebRtcMode
import av
import cv2
from ultralytics import YOLO

# ... your other imports ...

# WebRTC Configuration (FIXED)
RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
})

class VideoProcessor:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')  # Use nano model for speed
    
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        # Run YOLO
        results = self.model(img, verbose=False)
        
        # Draw results
        annotated_frame = results[0].plot()
        
        return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

# Streamlit app
st.title("🔍 D3T4CT_01 - Real-time Object Detection")

webrtc_ctx = webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    video_processor_factory=VideoProcessor,
    media_stream_constraints={
        "video": {
            "width": {"ideal": 640},
            "height": {"ideal": 480},
            "frameRate": {"ideal": 30}
        }
    }
)
