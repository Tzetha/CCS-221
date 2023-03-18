import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

two_d_arr = np.array([[1,0,1], [0,1,0],[1,0,1]])

def change(x, y, color):
    
    two_d_arr[x][y] = color
    
    img = plt.imshow(two_d_arr, interpolation='none', cmap='Pastel2')
    img.set_clim([0,50])
    plt.colorbar()
    return img

def main():
    x_coordinates = st.number_input("X coordinates:", min_value=0, max_value=2, step=1)
    y_coordinates = st.number_input("Y coordinates:", min_value=0, max_value=2, step=1)
    colorvalue = st.slider("Select a Color Value",0, 50, step = 10, key='my_slider')
    img = change(x_coordinates, y_coordinates, colorvalue)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

main()
