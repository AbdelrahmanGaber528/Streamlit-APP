import streamlit as st
import numpy as np

st.header("Shape Calculations")

# sidebar 
st.sidebar.title("Shape")
with st.sidebar:
    shape = st.selectbox("Choose Shape : ",["Circle","Rectangle","Square"])

# parameter for shapes 
area , parimeter = '' , ''

# calc based on shape
if shape == "Circle":

    raduis = st.number_input("Raduis : ",min_value=0.0 , max_value=200.0,step=0.01)
    # all numbers should be double/float not integer
    area = raduis * raduis * np.pi
    parimeter = 2 * np.pi * raduis

elif shape == "Rectangle": 

    width = st.number_input("Width : ",min_value=0.0 , step = 1.0)
    length = st.number_input("Length : ",min_value=2*width , step = 1.0)
    area = width * length
    parimeter = ( width + length )* 2

else : 

    rib =  st.number_input("Width : ",min_value=0.0 , step = 1.0)
    area = rib * rib
    parimeter = rib * 4 


# calc button
compute_btn = st.button("Compute")

if compute_btn : 
    with st.spinner("Computing..."): # snipper if the computing late
        st.write("Area:", area)
        st.write("Parimeter:", parimeter)
