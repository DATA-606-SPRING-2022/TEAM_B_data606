# Model Deployment

The model is deployed using Streamlit. Streamlit provides UI components that may be quickly deployed on a website. Every time a user interacts with the components, Streamlit reruns the Python script. Streamlit's straightforward design makes it simple to create interactive webpages.
<br><br>
The website has been develpoed in 2 phases into 2 seperate web pages. A user can toggle between 2 pages using the panel in the left.<br>
1. Analysis<br>
2. Prediction<br><br>

## Analysis

- Initial EDA results have been deployed into streamlit.
- A user can filter based upon year.
- Insights related to data with respect to years will be displayed.

  ![image](https://user-images.githubusercontent.com/93356110/164125872-f8ee54a4-90c5-4fc1-856f-796735d63290.png)

## Prediction

- A user can know if his case will be certified on denied based upon the machine learning model built using Random Forest
- User has to enter the input details corresponding to his case. 
- The web page displays if the case would be certified or denied based upon the inputs. 

  ![image](https://user-images.githubusercontent.com/93356110/164126207-d7a79094-5c23-4c16-b792-642efe4d18ce.png)

