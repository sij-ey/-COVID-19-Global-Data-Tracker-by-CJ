import streamlit as st
import pandas as pd
from streamlit import sidebar

st.title("Covid data analysis Dashboard")
if sidebar.button("Bar graphs",use_container_width=True):
    # load the data
    df = pd.read_csv("data/owid-covid-data.csv")

    # total cases by locations
    st.write("Total covid cases by locations")
    st.bar_chart(df, y="total_cases", x="location", color="#ffaa00")
    # total cases by continents
    st.write("Total cases by continents")
    st.bar_chart(df, y="total_cases", x="continent")

    # show the distribution of cases on a pie chart
    st.write("scatter plot for the data")
    st.scatter_chart(df, y="total_cases", x="date")
    # total new cases by continents
    st.write("Total new cases by continents")
    st.bar_chart(df, y="new_cases", x="continent")
    # total new cases by location
    st.write("Total new cases by location")
    st.bar_chart(df, y="new_cases", x="location")
    st.map(df)
if sidebar.button("Line charts",use_container_width=True):
    df = pd.read_csv("data/owid-covid-data.csv")
    # total cases by locations
    st.write("Total covid cases by locations")
    st.bar_chart(df, y="total_cases", x="location", color="#ffaa00")
    # total cases by continents
    st.write("Total cases by continents")
    st.line_chart(df, y="total_cases", x="continent")

    # show the distribution of cases on a pie chart
    st.write("scatter plot for the data")
    st.scatter_chart(df, y="total_cases", x="date")
    # total new cases by continents
    st.write("Total new cases by continents")
    st.line_chart(df, y="new_cases", x="continent")
    # total new cases by location
    st.write("Total new cases by location")
    st.line_chart(df, y="new_cases", x="location")
    st.map(df)
sidebar.button("scatter plots",on_click="/hi",use_container_width=True)
sidebar.button("Heat maps",use_container_width=True)


