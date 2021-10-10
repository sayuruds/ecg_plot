
from matplotlib.pyplot import figure
import mpld3
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import streamlit as st

# Title
st.write("""
# Electrocardiogram Elot
Prevention is Better Than Cure
""")

image = Image.open('C:/Users/Sayuru Dissanayake/Desktop/ECG/heart.jpg')
#st.image(image, caption='ML', use_column_width=True)
st.image(image, width=250)


unqid = st.text_input("Enter Patient ID", "ab001")


if unqid == "xxx":
    x = np.loadtxt('C:/Users/Sayuru Dissanayake/Desktop/ECG/SampleECG.txt')[:,-1]
    plt.plot(x[-9000:-4000]/1024./1.1*3.3-1.5, 'k')
    mpld3.show()
    

st.write("""
Created by NTP-2021-26
""")