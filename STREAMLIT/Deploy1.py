import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go

st.markdown("<h1><center>H1B CASE STATUS ANALYSIS",unsafe_allow_html=True)
st.markdown("<center>by Rohith Ram Maringanti and Sai Divyanjali Muddasani",unsafe_allow_html=True)
st.markdown("<center>under the guidance of Dr. Chaojie Wang",unsafe_allow_html=True)


st.markdown("<h1><center>-------------------------------------------",unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

df=pd.read_csv("h1b_df.csv")
st.markdown("<h4>Select an year",unsafe_allow_html=True)
a=st.selectbox("",('2017','2018','2019','2020','2021'))
a=int(a)
dfa = df[df["Year"]==a]
df1=dfa.groupby("CASE_STATUS")["CASE_NUMBER"].count().reset_index()
fig = px.pie(df1, values = "CASE_NUMBER" , names = "CASE_STATUS", title = "Approved vs Denied")
st.plotly_chart(fig)


dfa = df[(df["Year"]==a) & (df["CASE_STATUS"]=="Certified")]
df1=dfa.groupby("EMPLOYER_STATE")["CASE_NUMBER"].count().sort_values(ascending=False).reset_index().head(10)
fig = px.bar(df1, x='EMPLOYER_STATE', y='CASE_NUMBER', title="States with highest certified cases")
st.plotly_chart(fig)

dfa = df[(df["Year"]==a)]
h1b_df_e = dfa.groupby("EMPLOYER_NAME")["CASE_NUMBER"].count().sort_values(ascending=False).reset_index().head(10)
labels = list(h1b_df_e["EMPLOYER_NAME"])
fig = px.pie(h1b_df_e, names='EMPLOYER_NAME', labels=labels , values='CASE_NUMBER', title="Top 10 companies sponsoring H1B")
st.plotly_chart(fig)

st.write("Educational Background")
h1b_job=dfa.groupby("JOB_INFO_EDUCATION")["CASE_NUMBER"].count().sort_values(ascending=False).reset_index()
fig = go.Figure(data=[go.Pie(labels=list(h1b_job["JOB_INFO_EDUCATION"]), values=list(h1b_job["CASE_NUMBER"]), pull=[0, 0, 0.2, 0.2,0.2,0.2,0.2])])
st.plotly_chart(fig)


h1b_title=dfa.groupby("PW_SOC_TITLE")["CASE_NUMBER"].count().sort_values(ascending=False).reset_index().head(10)
fig = px.pie(h1b_title, values='CASE_NUMBER', names='PW_SOC_TITLE', title='Job Titles Statistics', hole=.3)
st.plotly_chart(fig)

st.write("Immigrant's home country")
h1b_coun = dfa.groupby("COUNTRY_OF_CITIZENSHIP")["CASE_NUMBER"].count().sort_values(ascending=False).reset_index()
import numpy as np
import pycountry
def do_fuzzy_search(country):
    try:
        result = pycountry.countries.search_fuzzy(country)
    except Exception:
        return np.nan
    else:
        return result[0].alpha_3
h1b_coun["iso_code"] = h1b_coun["COUNTRY_OF_CITIZENSHIP"].apply(lambda country: do_fuzzy_search(country))
cases = list(h1b_coun["CASE_NUMBER"])
b=list(range(len(h1b_coun),0,-1))
b[0],b[1],b[2] = 400,250,200
h1b_coun["CASE_NUMBER"] = b
fig = go.Figure(data=go.Choropleth(
    locations = h1b_coun['iso_code'],
        z = h1b_coun['CASE_NUMBER'],
    text = cases,
    colorscale = [[0, 'rgb(255,255,0)'], [1, 'rgb(255,0,0)']],
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=1,
    showscale  = False,

))
st.plotly_chart(fig)
