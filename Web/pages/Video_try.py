import streamlit as st
from yolo_predictions import YOLO_Pred
import cv2
import numpy as np
import tempfile



st.set_page_config(page_title="Video Fish Detection",
                    layout='wide',
                    page_icon='./images/video_icon.png')
st.title("Welcome to YOLO video detection")
st.write('Please upload a video for detection')

with st.spinner('Please wait while the model is loading'):
    yolo = YOLO_Pred(onnx_model='./models/best.onnx',
                    data_yaml='./models/data.yaml')

def upload_video():
    # Upload Video
    video_file = st.file_uploader(label='Upload Video', type=['mp4', 'avi', 'mov', 'webm', 'ogg', 'mkv'])
    if video_file is not None:
        size_mb = video_file.size / (1024 ** 2)
        file_details = {"filename": video_file.name,
                        "filetype": video_file.type,
                        "filesize": "{:,.2f} MB".format(size_mb)}
        
        if file_details['filetype'].startswith('video/'):
            st.success('Valid video file type')
            return {"file": video_file,
                    "details": file_details}
        else:
            st.error('Invalid video type')
            st.error('Only upload video formats such as mp4, avi, mov, webm, ogg, mkv, etc.')
            return None

def main():
    video_object = upload_video()

    if video_object:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
            temp_file.write(video_object['file'].read())

        cap = cv2.VideoCapture(temp_filename)

        if not cap.isOpened():
            st.error("Error: Could not open the video file.")
            return

        st.info('Video Preview')
        video_placeholder = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Perform object detection on the frame
            frame_with_objects = yolo.predictions(frame)

            # Display the processed frame
            video_placeholder.image(frame_with_objects, channels="BGR")

        cap.release()

if __name__ == '__main__':
    main()



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

