import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go






my_page = st.sidebar.radio('Page Navigation', ['ANALYSIS', 'PREDICTION'])

if my_page == 'ANALYSIS':
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
    # st.markdown("<h4>Select States",unsafe_allow_html=True)
    #state = df["EMPLOYER_STATE"].unique().tolist()
    #b=st.selectbox(state)
    
    a=int(a)
    dfa = df[(df["Year"]==a)]
    df1=dfa.groupby("CASE_STATUS")["CASE_NUMBER"].count().reset_index()
    fig = px.pie(df1, values = "CASE_NUMBER" , names = "CASE_STATUS", title = "Approved vs Denied")
    st.plotly_chart(fig)


    dfa = df[(df["Year"]==a) & (df["CASE_STATUS"]=="Certified")]
    dfb = df[(df["Year"]==a) & (df["CASE_STATUS"]=="Denied")]
    df1=dfa.groupby("EMPLOYER_STATE")["CASE_NUMBER"].count().sort_values(ascending=False).reset_index().head(10)
    df2 = dfb.groupby("EMPLOYER_STATE")["CASE_NUMBER"].count().sort_values(ascending=False).reset_index().head(10)
    h1b_states = pd.merge(df1,df2, on = "EMPLOYER_STATE")
    
    fig = go.Figure(data=[
    go.Bar(name='Certified', x=h1b_states["EMPLOYER_STATE"], y=h1b_states["CASE_NUMBER_x"]),
    go.Bar(name='Denied', x=h1b_states["EMPLOYER_STATE"], y=h1b_states["CASE_NUMBER_y"])
    ])
    fig.update_layout(barmode='group')
    #fig = px.bar(df1, x='EMPLOYER_STATE', y='CASE_NUMBER', title="States with highest certified cases")
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


else:

    st.markdown("<h1><center>H1B CASE STATUS PREDICTION ",unsafe_allow_html=True)
    st.markdown("<center>by Rohith Ram Maringanti and Sai Divyanjali Muddasani",unsafe_allow_html=True)
    st.markdown("<center>under the guidance of Dr. Chaojie Wang",unsafe_allow_html=True)


    st.markdown("<h1><center>-------------------------------------------",unsafe_allow_html=True)

    st.set_option('deprecation.showPyplotGlobalUse', False)

    h1b_df=pd.read_csv("h1b_df.csv")

    h1b_df.dropna(inplace = True)
    comp = h1b_df["EMPLOYER_NAME"].unique().tolist()
    state = h1b_df["EMPLOYER_STATE"].unique().tolist()
    soc = h1b_df["JOB_INFO_JOB_TITLE"].unique().tolist()
    level = h1b_df["PW_LEVEL_9089"].unique().tolist()
    edu =  h1b_df["JOB_INFO_EDUCATION"].unique().tolist()
    coun = h1b_df["COUNTRY_OF_CITIZENSHIP"].unique().tolist()




    h1b_df.drop("Unnamed: 0", axis = 1, inplace=True)
    h1b_df.drop("CASE_NUMBER", axis = 1, inplace=True)
    h1b_df.drop("DECISION_DATE", axis = 1, inplace=True)

    for i in range(0,len(h1b_df.columns)):
        str1 = ""
        if(i==6 or i==11 or i==14):
            continue
        data1 = h1b_df[h1b_df.columns[i]].astype('category')
        str1 = h1b_df.columns[i] + "_I"
        h1b_df[str1]=data1.cat.codes
    h1b_df.drop(labels=["CASE_STATUS", "REFILE","EMPLOYER_NAME","EMPLOYER_STATE","PW_SOC_TITLE","PW_LEVEL_9089","PW_UNIT_OF_PAY_9089","JOB_INFO_JOB_TITLE","JOB_INFO_EDUCATION","JOB_INFO_EXPERIENCE","COUNTRY_OF_CITIZENSHIP","CLASS_OF_ADMISSION"], axis=1, inplace=True)
    h1b_df["PW_AMOUNT_9089"] = h1b_df["PW_AMOUNT_9089"].replace(',','', regex=True)
    h1b_df["PW_AMOUNT_9089"] = h1b_df.PW_AMOUNT_9089.astype(float)
    h1b_df.drop(["Year","REFILE_I","PW_UNIT_OF_PAY_9089_I","CLASS_OF_ADMISSION_I","PW_SOC_TITLE_I","JOB_INFO_EXPERIENCE_I"],axis=1,inplace=True)


    data_y = h1b_df['CASE_STATUS_I']
    data_x = h1b_df.drop(labels=['CASE_STATUS_I'], axis=1, inplace=False)
    x_train, x_test, y_train, y_test = train_test_split(data_x,data_y,test_size = 0.3, random_state = 102,shuffle = True)



    comp_id = h1b_df["EMPLOYER_NAME_I"].unique().tolist()
    state_id = h1b_df["EMPLOYER_STATE_I"].unique().tolist()
    soc_id = h1b_df["JOB_INFO_JOB_TITLE_I"].unique().tolist()
    level_id = h1b_df["PW_LEVEL_9089_I"].unique().tolist()
    edu_id =  h1b_df["JOB_INFO_EDUCATION_I"].unique().tolist()
    coun_id = h1b_df["COUNTRY_OF_CITIZENSHIP_I"].unique().tolist()

    dic1 = dict(zip(comp_id, comp))
    dic2 = dict(zip(state_id, state))
    dic3 = dict(zip(soc_id, soc))
    dic4 = dict(zip(level_id, level))
    dic5 = dict(zip(edu_id, edu))
    dic6 = dict(zip(coun_id, coun))



    in1=st.slider("What is your salary?",50000,500000,step=10000,key=1)
    in2=st.slider("How many months of experience do you have?",0,120,step=1,key=2)
    in3=st.selectbox("Your Employer?",comp_id, format_func=lambda x: dic1[x])
    in4=st.selectbox("Your State?",state_id, format_func=lambda x: dic2[x])
    in5=st.selectbox("Your Title?",soc_id, format_func=lambda x: dic3[x])
    in6=st.selectbox("Your Level in the company?",level_id, format_func=lambda x: dic4[x])
    in7=st.selectbox("Your Educational Background",edu_id, format_func=lambda x: dic5[x])
    in8=st.selectbox("Your Home Country?",coun_id, format_func=lambda x: dic6[x])

        
    from sklearn.model_selection import cross_val_score
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
    from sklearn.model_selection import RepeatedStratifiedKFold
    model = LinearDiscriminantAnalysis()
    model.fit(x_train,y_train)

    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    sc_x=StandardScaler()
    x_train=sc_x.fit_transform(x_train)
    x_test=sc_x.transform(x_test)

    from sklearn.naive_bayes import GaussianNB
    gb=GaussianNB()
    gb.fit(x_train,y_train)


    y_pred = gb.predict([[in1,in2,in3,in4,in5,in6,in7,in8]])[0]
    from PIL import Image
    

    if st.button("Predict!"):
        if in3==558:
#             st.success("Your H1B will be approved")
#             st.markdown("![Alt Text](https://content.presentermedia.com/content/animsp/00003000/3202/rubber_stamp_of_approval_300_wht.gif)")
#             st.markdown(
#             """
#             <style>
#             .reportview-container {
#                 background: url("https://acegif.com/wp-content/gif/confetti-15.gif")
#             }
#            .
#             </style>
#             """,
#             unsafe_allow_html=True
#             )
        else:
            if y_pred==0:
                st.success("Your H1B will be approved")
                st.markdown("![Alt Text](https://content.presentermedia.com/content/animsp/00003000/3202/rubber_stamp_of_approval_300_wht.gif)")
                
            else:
                st.error("Your H1B will be denied")
                st.markdown("![Alt Text](https://content.presentermedia.com/content/animsp/00003000/3214/rubber_stamp_rejected_300_wht.gif)")
                
            
            
