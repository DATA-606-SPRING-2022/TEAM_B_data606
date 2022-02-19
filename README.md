# H1B Case Status Analysis - Team B
by Sai Divyanjali Muddasani and Rohith Ram Maringanti
## Idea
  &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; H1B visa is a permit to work for non-immigrant temporary workers in United States. An employer files a petition on behalf of an employee. Every year, there are thousands of applicants for H1B out of which only few gets approved. Most of the international students who complete their masters land in their dream job. Many individuals who work for companies in their home countries get a chance to work in USA through H1B. Hence, many applicants eagerly wait to know if there application would be approved. Our project aims to determine the chances of a case being approved or denied based upon the data from 2015-2020. 

## Data
The data retrieved from the official government website - Department of Labor. The data is disclosed every year after the individuals file their applications. We are considering the data of 5 years (2015-2020). The latest data will give us most updated case scenarios which will help in making better predictions. The data contains case files corresponding to 190,000 applicants over 5 years. The data contains 30+ columns which constitutes few important attributes as follows.    
<br><br>
EMPLOYER_NAME : (String Type) The company which sponsors H1B for the applicants. <br>
EMPLOYER_PROVINCE : (String Type) The state in which employee works <br>
SOC_TITLE : (String Type) The field of work type. Ex: Software, Accountants, Mechanical etc.<br>
SOC_CODE : (String Type) The code related to each job field<br>
SOC_TITLE : (String Type) Job Designation of individuals<br>
WAGE : (Integer Type) Annual income of employers <br>
MINIMUM_EDUCATION : (String Type) High School, Bachelors or Masters <br>
MAJOR_FIELD_OF_STUDY : (String Type) Applicant's academic major<br>
COUNTRY_OF_CITIZENSHIP : (String Type) Applicant's Home Country <br>
FULL_TIME_POSITION : (String Type) Job type - Full time or Contract type
<br><br>
The data acquired is in raw format with many missing values and irrelevant columns. Thorough Preprocessing of data is required to implement machine learning algorithms. 
<br><br>
Dataset: https://www.dol.gov/agencies/eta/foreign-labor/performance <br><br>
Size of the data - nearly 237MB - contains 5 files each of consisting of data related to an year.<br><br>

## What questions do you have in mind and would like to answer?
The primary role of the project is to determine if a case status would be approved or denied. We would like to explore the data with respect to attributes such as type of job field, annual income of the employee, province of work location etc. Our project would also answer additional questions for H1B aspirants such as<br>
- Which state has high percentage of H1B applications certified? 
- What is the average wage of H1B certified employees. 
- Which job fields have higher preference?
- Does Full time position affect the decision?
- Which job titles have high risk of application being denied?

## Techniques
- Determining correlation amongst variables for feature selection. 
- Planning to implement classification algorithms such as Support Vector Machine, KNN classifier, Random Forest.
- Support vector machine works well with data with high dimensionality. It gives us faster prediction with better accuracy. Since H1B process application process is random. There would be possibility of outliers and hence, SVM would handle any outliers better than other models. <br>
- KNN Classifier works well in making real time predictions. It is very important to scale all features to the same level. Hence, will use standard scalar technique while building a model with KNN. 
- Implementing grid search for optimal parameter selection.
- Building an ensemble model such as Random Forest which reduces variance in the data. Random Forest will work well with the data if there is any possibility of overfitting. The data contains many categorical values and hence, working with Random Forest would be a better choice.
- Will use lazy predict to find if any additional algorithms would work well with the given data. 
- Determining confusion matrix, accuracy score, RSME value and other support metrics such as precision recall and F1. 
- Visualizing the results using Plotly. 
- Project has very good scope in visualization and will include sophisticated visualization techniques using Plotly.  


## Deployment - Streamlit
Planning to create a webpage for deployment of the model using ‘streamlit’. By the development of the model, it would be easy for end user to utilize the application. Users can predict their chances of their of being certified or denied. The project will be very useful for individuals who are planning to relocate to US. It will be highly helpful for thousands of graduates every year in knowing if the company that they received offer from sponspors H1B or not. End users can access the data using the web page developed in streamlit.  

## Work Distribution
#### Divya
- Data preprocessing steps - Cleaning the data, handling missing values, eliminating unwanted rows and columns.
- Indexing categorical values. 
- Determining the insights of the data with respect to wage, home country of applicants and employers. 
- Visualizing the plots with respect to employers and wages. 
- Building Support Vector Machine and KNN Classifier
- Deploy Webpage 1 - the visualizations of data in Streamlit. 
#### Rohith
- Initial analysis of data. Exploring the types of each columns. 
- Finding insights in the data with respect to Province and Job Type. 
- Visualization of plots with respect to Job titles, provinces using plotly
- Using Standard Scalar
- Building Random Forest and implementing another best algorithm suggested by lazy predict.
- Deploy Web Page 2 - Machine learning model with outcome prediction in streamlit. 
<br>
**********************************************************************************************
<br>

## EDA - Phase 1
- Imported necessary packages and covnerted the datasets into dataframes by using read_excel()
- Note: Since the data is very large, it takes time to load dataframes. 
- Extracting the required information from the data frame and concatinating dataframes of all years.
- For every case filed, there are personal information such as employee_name, employee_address etc which are sensitive. Also, this data isn't necessary to analyze the data and implement a machine learning model. Hence, following data ethics, the columns containing sensitive information is not being considered. Required data is being extracted from the raw dataframe.
- Appended the data of different years to have a holistic dataframe for 5 years
- Filtered the cases which are 'withdrawn' and 'expired'
- Eliminating small number of cases from the year 2016 (Since data from 2017-2021 is being considered for modelling)
- Following uniform notations for state names. Data has different cell values for state referring to same state. Ex: California, CA
- Hence, mapped such redundencies to uniform notations. 
## Insights from the data
- Number of H-1B certified applications are increasing every year. 
- In 2017, least number of H-1B applications were certified since Trump government implemented stringent immigration rules. 
- In the recent past, number of H-1B applications nearly doubled to that of 2017. 
- Refer to the image below <br>
![image](https://user-images.githubusercontent.com/93351186/154819652-5ed94486-fd21-428c-b2ba-10ef9e8a7932.png)
<br>
- Plotted approvals vs denied from 2017 - 2021. Plotted subplots with multiple pie charts <br>
- Refer to the image below 
<br>

![image](https://user-images.githubusercontent.com/93351186/154819766-bb03554a-1cc4-49f6-8d6b-0071dbdb009a.png)

<br>

## Next weeks
- Find which states has highest number of approvals year-wise
- Find which companies sponsers highest number of H-1Bs 
- Find if annual income has any influence on approvals
- Which educational background has higher number of approvals
- Job titles which have higher chances of approvals. 

