import streamlit as st 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# load data with cache 
@st.cache_data
def load_data(file):
    return pd.read_csv(file)


# title of dashboard
st.title("Dashboard")

# defince variables
file = None

# sidebar
st.sidebar.title("Upload File")
with st.sidebar:
    with st.spinner("Uploading..."):
        file = st.file_uploader("File : ",type=["csv"])

if file != None : 
    df = load_data(file)

    n_rows = st.slider("Number of Rows : " , min_value=5, max_value=len(df), step=15)


    # choose columns : 
    columns = st.multiselect("Select columns : ",df.columns , default=df.columns.tolist())

    st.write(df.loc[:n_rows,columns]) # appear the rows 

    # get numerical columns for scatter : 
    numerical_col = df.select_dtypes(include=np.number).columns.to_list()

    # set all in vertical line ; 
    tab1 , tab2 ,tab3= st.tabs(["Scatter","Histogram","Heatmap])

    with tab1:

        col1 , col2 , col3 , col4 = st.columns(4)

        with col1 : 
            x_axis = st.selectbox("Column on X axis ", options=numerical_col)
        with col2 : 
            y_axis = st.selectbox("Column on Y axis ", options=numerical_col)
        with col4 : 
            size_column = st.selectbox("Size column ", options=numerical_col)
        with col3 :
            color_column = st.selectbox("Color Column ", options=df.columns)
        
        scatter = px.scatter(df , x= x_axis ,y = y_axis,color=color_column,size=size_column)

        st.plotly_chart(scatter)

    with tab2:

        hist_features = st.selectbox("Column : ", options=numerical_col)
        histogram = px.histogram(df , x= hist_features, nbins=100 , title=f"{hist_features} Distribution")
        
        st.plotly_chart(histogram)

    with tab3 : 
        # get num columns
        numeric_df = df.select_dtypes(include=np.number)
        # heatmap
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, ax=ax,)
        # rotation of words
        plt.xticks(rotation=45)
        plt.yticks(rotation=45)

        st.pyplot(fig)
