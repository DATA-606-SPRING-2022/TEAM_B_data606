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
<br>

<b> Increasing H-1B approvals every year </b><br><br>
Number of H-1B certified applications are increasing every year. In 2017, least number of H-1B applications were certified since Trump government implemented stringent immigration rules. The number of certified applications were almost same in the years 2019 and 2020. In the recent past, number of H-1B applications nearly doubled to that of 2017. With the given trend, we can come to the conclusion that number of certified cases will definitely increase leaps and bounds in the year 2022. Refer to the image below <br><br>
![image](https://user-images.githubusercontent.com/93356110/155852667-3f44a3ce-e5d7-40d1-8f13-11650653abc5.png)
<br><br>

<b> Approval vs Denial every year</b><br><br>
Plotted approvals vs denied from 2017 - 2021. Plotted subplots with multiple pie charts for every year. In the year 2018, highest number of H1B cases were denied. 1 out of every 4 application was denied. While 2018 was the year with highest denial rate, 2020 and 2021 have highest approval rate. It might be due to various reasons such as Presidential elections, change in government etc.  Refer to the image below 
<br><br>
![image](https://user-images.githubusercontent.com/93351186/154819766-bb03554a-1cc4-49f6-8d6b-0071dbdb009a.png)
<br><br>

<b> States with highest certified H-1B cases</b><br><br>
California has always been hub for the software industry providing job opportunities for majority of the immigrants. It has many companies which hire huge number of employees every year. Therefore, California is the state which has highest number of certified H-1B cases leading by a large margin. The state next to California is Texas with less than half approvals of California. Texas has always been a hub to foreigners, especially Indians. Majority of Indians living in US settle in either Texas or California. Other states among top 10 include New York, New Jersey, Washington, Virginia etc. Refer to the image below.
<br><br>
![image](https://user-images.githubusercontent.com/93356110/155847275-e503e8d0-2367-48de-99cb-64408366f606.png)
<br><br>

<b> Top Companies sponsoring H-1B </b><br><br>
Tech Giants such as Microsoft, Google, Facebook, Amazon tops the list of H-1B sponsors. Along with such Product based companies, other Service based consulting companies which sponsor H-1Bs include Tata Consultancy Services, Infosys, Cognizant etc. All these established software companies have high H-1B sponsorship. If an individual gets a job in one of these companies, the probability of their H1B being sponsored would be very high. Refer to the image below.
<br><br>
![image](https://user-images.githubusercontent.com/93356110/155847466-8a78fbe4-4ace-4d65-9b41-63e0cf39d66f.png)
<br><br>

<b> Does salary influence H1B approvals? </b><br><br>
As seen in the earlier plot, highest H1B sponsorship corresponds to renowned established companies like Amazon, Microsoft, Google Apple etc. Undoubtedly, these companies offer best salaries in the industry. Almost every employee working in these companies receive salaries greater than 100k. Hence, H1B sponsorship for salaries greater than 100k is much higher compared to salaries less than 100k. To distinguish amongst various salary levels, dataset has been filtered multiple times corresponding to the salary range. Please refer to the image below. 
<br><br>
![image](https://user-images.githubusercontent.com/93351186/155847758-76f6b9dc-d626-4ed3-a546-9bc6f0047b0e.png)
<br><br>
  
<b> Educational Background of employees </b><br><br>
More than 90% of H1B applicants have either earned a Masters or a Bachelors degree. Most of the immigrants dream to study higher education in USA because of top notch facilities and faculty. Hence, the ratio is higher. Other educational backgrounds include Doctorate, High School grads etc. However, their proportion is very minimal compared to that of Masters and Bachelors. Masters quota is leading with 50.4% while the Bachelors quota has nearly 42% applications. Refer to the image below. 
<br><br>
![image](https://user-images.githubusercontent.com/93351186/155849465-537981a4-8edc-4019-b4eb-51d1cf9b7ddc.png)
<br><br>

<b> Job Title Statistics </b><br><br>
To verify if the tendencies of H1B sponsors being software giants is true, let us plot a graph corresponsing to job titles. If most of the jobs titles relate to software industry, our insights holds true. As per our estimate, job titles corresponding to Software Industry lead the race of H1B approvals. Majority of applicants are Software Developers. Other job titles include System Engineers, Data Analysts, Statisticians etc. Few other industries include Electronics, Mechanical and Accounting sectors. Refer to the image below.
<br><br>
![image](https://user-images.githubusercontent.com/93351186/155848214-c06e46f5-49d2-4f46-9757-60ec6cddbc58.png)
<br><br>

<b> Where do the immigrants belong? </b><br><br>
The data also includes countries of citizenship. Therefore, based upon this data, we can draw insights about the data of where these immigrants are coming from. As per the data, India is the leading country with utmost majority followed by China. As per the statistics, the population of India and China are very high. We can hence assume that the population dreaming about studying abroad is higher. Other top countries include Canada, South Korea etc. A choropleth map has been plotted to understand the results. Refer to the image below.
<br><br>
![image](https://user-images.githubusercontent.com/93351186/155848379-9e68dcd3-a500-4d6f-a78b-cd6280656804.png)
<br><br>

<u>Link to presentation:<br><br>
https://github.com/rohithram23/TEAM_B_data606/blob/main/Presentations/Initial_Presentation.pptx

<br><br>
<u> Link to Video Presentation - Youtube: <br><br>
https://www.youtube.com/watch?v=VwyoawyExTY


