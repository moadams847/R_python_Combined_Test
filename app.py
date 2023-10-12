import streamlit as st
import subprocess
from PIL import Image

st.header('🎈 R x Python Streamlit App')
# Specify the path to the Rscript executable

# process1 = subprocess.Popen(["Rscript", "helloworld.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
# result1 = process1.communicate()
# # print(result1)
# st.write(result1)

st.subheader('Creating a plot using `ggplot2`')

process2 = subprocess.Popen(["Rscript", "plot.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process2.communicate()
image = Image.open('plot.png')
st.image(image)
st.caption('**Figure 1.** A simple scatter plot of *wt* as a function of *mpg* from the mtcars dataset.')

#-------------------
process3 = subprocess.Popen(["Rscript", "cal.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result3 = process2.communicate()
