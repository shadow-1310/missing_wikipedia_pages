import streamlit as st
import pandas as pd
from find_entity import FreqFinder

st.set_page_config(layout = "wide")

st.header("Suggestion app for Wikipedia Page Creation")
path = "combined2.csv"

df = pd.read_csv(path)
st.write(f"finding frequent entity for {df.shape[0]} news articles of different sources")


with st.spinner("Please Wait...."):
    f = FreqFinder(path)
    f.find_freq()

    def show_popup(key):
        st.info(f.freq_map[key][1])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Entity**")
    with col2:
        st.write("**Frequency**")
    with col3:
        st.write("**News Details**")

    # st.markdown("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True)
    for key in f.sorted_entity:
        with col1:
            st.write(key)
        with col2:
            st.write(f.freq_map[key][0])
        with col3:
            if st.button(f"details for {key}"):
                show_popup(key)
        # st.write("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True        
        # st.markdown("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True)
