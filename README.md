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
- Determining confusion matrix, accuracy score, RSME value and other support metrics such as precision recall and F1. 
- Visualizing the results using Plotly. 
- Project has very good scope in visualization and will include sophisticated visualization techniques using Plotly.  

## Deployment
Planning to create a webpage for deployment of the model using ‘streamlit’. By the development of the model, it would be easy for end user to utilize the application. Users can predict their chances of their of being certified or denied. The project will be very useful for individuals who are planning to relocate to US. It will be highly helpful for thousands of graduates every year in knowing if the company that they received offer from sponspors H1B or not. End users can access the data using the web page developed in streamlit.  
