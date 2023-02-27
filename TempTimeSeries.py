import streamlit as st
import pandas as pd
import numpy as npd
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Global Temperature",
                   page_icon=":partly_sunny:",
                   layout="wide")

def scatter_plot(dataframe):
    x_axis=st.selectbox('Select x-axis value', options=data.columns)
    y_axis=st.selectbox('Select y-axis value', options=data.columns)
    col=st.color_picker('Select a plot colour')

    plot=px.scatter(data, x=x_axis, y=y_axis)
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)

def best_fit(dataframe):
    x_axis=st.selectbox('Select x-axis value:', options=data.columns)
    y_axis=st.selectbox('Select y-axis value:', options=data.columns)
    col=st.color_picker('Select plot colour:')

    plot=px.scatter(data, x=x_axis, y=y_axis)
    plot.update_traces(marker=dict(color=col))
    plot.update_traces(mode='markers+lines', line_shape='spline')
    st.plotly_chart(plot)

def find_peak(dataframe):
    x_axis=st.selectbox('Select x-axis value:', options=data.columns)
    y_axis=st.selectbox('Select y-axis value:', options=data.columns)
    col=st.color_picker('Select plot colour:')
    plot=px.scatter(data, x=x_axis, y=y_axis)
    plot.update_traces(marker=dict(color=col))
    plot.update_traces(mode='markers+lines', line_shape='spline')

    peaks= find_peaks(y_axis)
    valleys = find_peaks(-y_axis)

    plot.update_traces(y=y_axis[peaks], mode='markers', marker_symbol='star', marker_size=10, name='peaks')
    plot.update_traces(y=y_axis[valleys], mode='markers', marker_symbol='x', marker_size=10, name='valleys')

    st.plotly_chart(plot)

#----- HOMEPAGE -----
st.title(":partly_sunny: Global Temperature Time Series")
st.markdown("##")
st.text("Global Temperature Time Series. Data are included from the GISS Surface Temperature (GISTEMP) analysis and the global component of Climate at a Glance (GCAG). Two datasets are provided: 1) global monthly mean and 2) annual mean temperature anomalies in degrees Celsius from 1880 to the present.")

#caching dataframe to avoid rerunnig entire script to load data after filter is applied
@st.cache_data
def get_data_from_csv():
    data_annual=pd.read_csv("annual.csv")
    return data_annual
data=get_data_from_csv()

#---- SIDEBAR -----
st.sidebar.header("Filter:")
continent=st.sidebar.multiselect(
         "Select source:",
         options=data["Source"].unique(),
         default=data["Source"].unique()
)

options=st.sidebar.radio(
         "Pages",
         options=['Home',
         'Scatter plot',
         'Best fit line',
         'Peaks']
)

if options=='Home':
    st.dataframe(data)
elif options=='Scatter plot':
    scatter_plot(data)
elif options=='Best fit line':
    best_fit(data)
elif options=='Peaks':
    find_peak(data)
