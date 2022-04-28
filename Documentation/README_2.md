# Machine Learning Phase

In this phase, we are modelling the data to predict the target variable "CASE_STATUS". We have used various methodologies to achieve the required result. The data from EDA Phase 1 has been exported as a CSV file. The exported cleansed CSV file is used for modelling. 

## Dropping unwanted columns

We have dropped unwanted columns like CASE_NUMBER and DECISION_DATE which aren't helpful in modelling. These features do not have any influence on the target variable. We also made sure that features which had personal information such as phone number, employee address etc are eliminated. Ethicality has been followed in data selection. 

## Indexing Categorical Variables

- The data contains many categorical columns such as EMPLOYER_NAME,EMPLOYER_STATE etc. 
- Therefore, we converted all the categorical variables to integers using category codes. 
- Original columns have been dropped to eliminate redundancy. 
- All the columns in the updated dataframe are either integer or float types.
- Hence, modelling can be easily performed without any hassles. 

  ![image](https://user-images.githubusercontent.com/93351186/164070872-bcc02265-58af-4ffa-bfd7-2174053a10b9.png)

## Pearson Correlation

- Pearson correlation is a measure of how closely two sets of data are related. 
- It depicts normalized covariance measurement, with the result always ranging between -1 and 1.
- The image below shows that attributes like Country of citizenship, salary etc have positive correlation.
- Other attrinutes like Job experience, Job level etc have negative correlation.

  ![image](https://user-images.githubusercontent.com/93351186/164072839-8ef91976-e490-43f3-8968-8bdb06aba2a8.png)

## Train Test Split

- The entire data has been divided into train and test data with the proportions of 70% and 30% respectively. 
- Random shuffling has been enabled to ensure maximum possible variety of data in train and test sets. 
- CASE_STATUS_I (indexed case status) is the target variable and hence been considered as data_y
- All the remaining attributes are stored in data_x

## Using Standard Scalar

- Standard scalar scales down attributes to uniform thereby ensuring that the model handles bias well. 
- H1B case status is random pick and hence, the possibility of outliers is very high. Scandard scalar handles outliers well. 
- Training and testing data have been fit into standard scalar. 
- New data is stored in x_train and x_test

# Model implementation

Multiple models have been implemented. However, top 3 best performing models are being documented. 

## Support Vector Machine

- Since H1B is a random pick, various features are considered in data modelling. 
- Support Vector Machine is performed to reduce the number of features to a more manageable quantity.
- SVM has given an accuracy score of 81.04%
- The model was highly biased towards certified cases since recall score for class 0 (Certified cases) is much higher when compared to class 1 (Denied cases)

## KNeighbors Classifier

- KNN Classifier works well in making real time predictions. It is very important to scale all features to the same level. 
- Hence, standard scalar technique has been implemented before hand while building a model with KNN.
- <b>Grid Search</b> has been implemented for optimal parameter selection
  ![image](https://user-images.githubusercontent.com/93356110/165654886-26a012fb-d41f-407b-ac12-1e2db78db221.png)
- Grid Search gave the optimal value of k to be 5.
- KNN has given an accuracy score of 80.70%
- Precision and recall scores for both classes are relatively better than SVM. 

## Random Forest Classifier

- Ensemble models perform better with data with high variance. It reduces overfitting of the data. 
- Random Forest gave the best results with accuracy score of 83.01%. 
- Precision and recall scores for both the classes are above 0.7. 
- Hence, Random Forest Classifier is being used to deploy the machine learning model in streamlit. 

# Results

<table>
  <tr>
    <th>Model</th>
    <th>Precision (Class 0)</th>
    <th>Recall (Class 0)</th>
    <th>Precision (Class 1)</th>
    <th>Recall (Class 1)</th>
    <th>Accuracy</th>
  </tr>
  <tr>
    <td>Support Vector Machine</td>
    <td>0.81</td>
    <td>0.92</td>
    <td>0.21</td>
    <td>0.13</td>
    <td>81.04%</td>
  </tr>
 
  <tr>
    <td>KNeighbors Classifier</td>
    <td>0.84</td>
    <td>0.95</td>
    <td>0.48</td>
    <td>0.22</td>
    <td>80.70%</td>
  </tr>
  
  <tr>
    <td>Random Forest Classifier</td>
    <td>0.85</td>
    <td>0.96</td>
    <td>0.62</td>
    <td>0.51</td>
    <td>83.10%</td>
  </tr>
  
</table>


<b> Random Forest Classifier is being deployed using streamlit since it is the best performing model </b>
