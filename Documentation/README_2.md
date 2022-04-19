#Machine Learning Phase

In this phase, we are modelling the data to predict the target variable "CASE_STATUS". We have used various methodologies to achieve the required result. The data from EDA Phase 1 has been exported as a CSV file. The exported cleansed CSV file is used for modelling. 

##Dropping unwanted columns

We have dropped unwanted columns like CASE_NUMBER and DECISION_DATE which aren't helpful in modelling. These features do not have any influence on the target variable. We also made sure that features which had personal information such as phone number, employee address etc are eliminated. Ethicality has been followed in data selection. 

##Indexing Categorical Variables

- The data contains many categorical columns such as EMPLOYER_NAME,EMPLOYER_STATE etc. 
- Therefore, we converted all the categorical variables to integers using category codes. 
- Original columns have been dropped to eliminate redundancy. 
- All the columns in the updated dataframe are either integer or float types.
- Hence, modelling can be easily performed without any hassles. 

![image](https://user-images.githubusercontent.com/93351186/164070872-bcc02265-58af-4ffa-bfd7-2174053a10b9.png)

##Pearson Correlation

- Pearson correlation is a measure of how closely two sets of data are related. 
- It depicts normalized covariance measurement, with the result always ranging between -1 and 1.
- The image below shows that attributes like Country of citizenship, salary etc have positive correlation.
- Other attrinutes like Job experience, Job level etc have negative correlation.

![image](https://user-images.githubusercontent.com/93351186/164072839-8ef91976-e490-43f3-8968-8bdb06aba2a8.png)

