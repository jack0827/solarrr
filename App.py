import streamlit as st
import pandas as pd
import os

#import profiling capability
import pandas_profiling 
from streamlit_pandas_profiling import st_profile_report

#import ml model



#imports for side navbar
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

#page-title
st.set_page_config(
    page_title= "SolAral",
    page_icon="logaur.png")

#nav-bar
with st.sidebar:
    choice = option_menu("Menu", ["Home", "Upload", "Data Analysis", "View Prediction"], 
                         icons=['house','upload', 'graph-up', 'eye'],
                         menu_icon= "app-indicator", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#fafafa"},
                             "icon": {"color": "black", "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#f3f3f3", "color": "black"},
                         })
    
#style configs
st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
        .css-1aumxhk{
        background-color: #fafafa;
        background-image: none;
        color: white;
        }
        p{
        text-align: justify;
        }
    </style>
    """, unsafe_allow_html=True
)

if os.path.exists("new_pm_data.csv"):
    df = pd.read_csv("new_pm_data.csv", index_col =None)

if choice == "Home":
    st.image("logaur.png", width=140)
    st.title("SolAral")
    st.markdown(
        """
        <p>
        A Recurrent and Graph Neural Networks-based Predictive Maintenance Model for Rooftop 
        Solar Photovoltaic Systems, SolAral aims to promote the use of solar energy by serving
        as a tool to maintain this type of RE system. For now, the model aims to predict the
        maintenance of a simulated grid-connected solar PV system for Wawa Elementary School
        in Tanay, Rizal.
        </p>
        """, unsafe_allow_html=True)

if choice == "Upload":
    st.title("Upload your data")
    file = st.file_uploader("Upload your data in .csv file")
    if file:
       df = pd.read_csv(file, index_col=None)
       df.to_csv("new_pm_data.csv", index=None)
       st.dataframe(df)

if choice == "Data Analysis":
    st.title("Data Analysis Report")
    profile_report = df.profile_report()
    st_profile_report(profile_report)
       

if choice == "View Prediction":
    #insert model and prediction results here
    st.title("Predictive Maintenance")
    pass

    


