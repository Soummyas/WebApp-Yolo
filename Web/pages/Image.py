import streamlit as st
from yolo_predictions import YOLO_Pred
from PIL import Image
import numpy as np



st.set_page_config(page_title="Image Fish Detection",
                    layout='wide',
                    page_icon='./images/picture.png')
st.title("Welcome to YOLO image detection")
st.write('Please upload image for detection')

with st.spinner('Please wait while model is loading'):
    yolo = YOLO_Pred(onnx_model='./models/best.onnx',
                    data_yaml='./models/data.yaml')
      
def upload_image():
    # Upload Image
    image_file = st.file_uploader(label='Upload Image', type=['png', 'jpg', 'jpeg'])
    if image_file is not None:
        size_mb = image_file.size/(1024**2) #divide byte file size by 1024 sq to get file size in mb
        file_details = {"filename" : image_file.name,
                        "filetype" : image_file.type,
                        "filesize" : "{:,.2f} MB".format(size_mb) }
        #st.json(file_details)

        # validate file
        if file_details['filetype'] in ('image/png', 'image/jpg','image/jpeg'):
            st.success('Valid image file type')
            return {"file" : image_file, 
                    "details" : file_details}
        else:
            st.error('Invalid image type')
            st.error('Only upload png, jpg, or jpeg file format')
            return None
        
def main():
    object = upload_image()
    
    if object:
        prediction = False
        image_obj = Image.open(object['file'])
        #st.image(image_obj)

#cols to display img and img deatils
        col1, col2 = st.columns(2)

        with col1:
            st.info('Image Preview')
            st.image(image_obj)

        with col2:
            st.subheader('Check below for file details')
            st.json(object['details'])
            b = st.button('Get Predictions')
            if b:
                with st.spinner("""
                    Please wait...
                                """):
                    st.write('button pressed')
                    #below will convert object into array
                    image_array = np.array(image_obj)
                    pred_image = yolo.predictions(image_array)
                    pred_image_obj = Image.fromarray(pred_image)
                    prediction = True

        if prediction:
            st.subheader("Predicted image")
            st.caption("Object detection from YOLOv5")
            st.image(pred_image_obj)

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

