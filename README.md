# Lung Cancer Prediction - Team B
by Sai Divyanjali Muddasani and Rohith Ram Maringanti
## Idea
  &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; Machine learning has influenced the health care sector today because of its strong computational potential for early disease prediction with reliable data analysis. Although there is immense awareness on lung diseases, lung cancer is still a major reason for deaths among many individuals. Lung cancer is caused by the uncontrolled development of cells in the lungs. It affects men, women, smokers, and non-smokers. This is the primary reason why we are interested in developing a predictive model which tells us the level of intensity we are prone to with respect to lung cancer based on the symptoms. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Knowing the level of severity beforehand, one can use necessary steps to either avoid activities that lead to the disease or take preventive measures in dealing with the severity. The model would take the data from patients who were suffering from lung cancer to predict the outcomes of other patients. Each patient's risk of lung cancer will be classed as 'high,' 'low,' or 'medium.' The information also reveals the link between other characteristics of lung cancer, such as smoking habits, obesity, etc. 
## What questions do you have in mind and would like to answer?
- How prone a particular individual is to lung cancer?
- Does gender affect severity in lung cancer?
- Does smoking cause lung diseases?
- Does age influence symptoms of Lung Cancer?
## Data
The data retrieved is a survey of patients who suffer from lung diseases. The data is collected from ‘data.world’ which is a legitimate and trustable source. The size of the data is nearly 2MB with data related to 1000 patients. Hence, there are 1000 rows in the data with 25 columns each including a symptom of lung cancer. Each patient disclosed the intensity of a symptom on a scale of 1-10. Few attributes of the data are as follows.
<br><br>
patient_id<br>
age<br>
gender<br>
air_pollution<br>
alcohol_use<br>
dust_allergy<br>
balanced_diet<br>
obesity<br>
smoking<br>
passive_smoker etc. <br><br>

Dataset: https://data.world/cancerdatahp/lung-cancer-data <br><br>
## Techniques
- Planning to implement classification algorithms such as Linear Discriminant Analysis, KNN classifier and Gaussian NB.
- Implementing grid search for optimal parameter selection.
- Determining confusion matrix, accuracy score, RSME value and other support metrics such as precision recall and F1. 
- Visualizing the results using Tableau or PowerBI. 

## Deployment
Planning to create a webpage for deployment of the model using ‘streamlit’. By the development of the model, it would be easy for end user to utilize the application. Users can rate themselves for the symptoms of lung diseases and predict if the level of severity of lung cancer is high, medium or low. In this way, users can take preventive measures in avoiding daily habits which lead to lung cancer.
