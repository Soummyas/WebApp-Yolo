import streamlit as st
from yolo_predictions import YOLO_Pred
from streamlit_webrtc import webrtc_streamer
import av

#Loading Model
yolo = YOLO_Pred('./models/best.onnx',
                './models/data.yaml')

st.set_page_config(page_title="Live Fish Detection",
                   layout='wide',
                   page_icon='./images/live.png')
st.title('Live recognition by Cam')
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    pred_image = yolo.predictions(img)

    #flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(pred_image, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)



st.header("Physical Characteristics:")
st.write('**Size:** Typically range from a few inches to about a foot in length, depending on the species and care.')
st.write('**Coloration:** Various colors and color combinations exist due to selective breeding, including red, orange, yellow, black, white, and calico patterns')
st.write('**Body:** Their bodies vary in shape, from elongated to more rounded, and they can have single or double tails.')

st.header("Habitat:")
st.write("**Origin:** Goldfish are descendants of wild carp and were first domesticated in China.")
st.write("**Aquarium Requirements:** They thrive in freshwater tanks with ample space, good filtration, and appropriate water temperature (around 65-72°F or 18-22°C).")

st.header("Behavior and Care:")
st.write("**Social Creatures:** They are social and can thrive in groups but can also live happily on their own.")
st.write("**Feeding:** Omnivorous by nature, their diet includes fish flakes, pellets, and live or frozen foods like brine shrimp or bloodworms. ")
st.write("**Lifespan:** With proper care, they can live for many years, sometimes even surpassing a decade or more. ")

st.header("Breeding:")
st.write("**Reproduction:** They are prolific breeders, and breeding often occurs in aquarium settings. ")
st.write("**Egg Layers:** Goldfish lay adhesive eggs that attach to plants or other surfaces in the tank.")
   
st.header("Interesting Facts:")
st.write("**Memory:** Contrary to popular belief, goldfish have decent memories and can be trained to recognize feeding times and even perform simple tricks. ")
st.write("**growth:** Their size can be stunted or enhanced based on their environment and diet ")

