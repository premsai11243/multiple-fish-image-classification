import streamlit as st
import joblib
import numpy as np 
import tensorflow as tf
from tensorflow.keras.models import load_model

st.title("Fish Species Classifier")# title 
loaded_model = load_model("D:/Desktop/fish/data/saved_model.keras")
label=joblib.load("D:/Desktop/fish/data/swaped.keras")

uploaded_file = st.file_uploader("Upload an image of a fish", type=['jpg', 'png'])# uploading the image
if uploaded_file:
    img = tf.keras.utils.load_img(uploaded_file, target_size=(300, 300))
    img_array = tf.keras.utils.img_to_array(img) / 255
    img_array = np.expand_dims(img_array, axis=0)

    predictions = loaded_model.predict(img_array)
    predicted_class = np.argmax(predictions)
    confidence_scores = predictions[0][0]

    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write(f"predicted label:{predicted_class}")    
    st.write(f"Predicted Class: {label[predicted_class]}")
    st.write(f"Confidence Scores: {confidence_scores}")

