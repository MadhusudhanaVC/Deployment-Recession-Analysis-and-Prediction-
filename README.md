#  Deployment Recession Analysis and Prediction (including deployment)


## Introduction 
This project aims to analyze historical economic data to predict recessions using machine learning techniques. By leveraging various algorithms and statistical methods, we've developed a model that can forecast economic downturns with reasonable accuracy. Additionally, we've deployed this model for easy access and visualization.

## Current Economic Data 

#### Current Ecocnomic Data of India , Q1 2024

| Indicator        | Value (Latest)       |
|--------------------|----------------------|
| GDP                | $4.112 trillion      |
| Unemployment Rate  | 3.1%                 |
| Inflation Rate     | 5.1%                 |
| GDP Growth         | 6.1%                 |
| Exchange Rate      | 1 USD = 82.75 INR    |
| Forex Reserves     | $619.07 billion      |

### Description

- **GDP (Gross Domestic Product)**: The total monetary value of all goods and services produced within a country's borders in a specific time period, usually annually or quarterly. [Source: IMF]

- **Unemployment Rate**: The percentage of the labor force that is unemployed and actively seeking employment. It's a key indicator of economic health, reflecting the balance between job supply and demand. [Source: Economic Times]

- **Inflation Rate**: The rate at which the general level of prices for goods and services is rising, leading to a decrease in purchasing power over time. High inflation can erode the value of money. [Source: Forbes]

- **GDP Growth**: The percentage increase in GDP from one period to another. It indicates the pace at which the economy is expanding or contracting. [Source: IMF]

- **Exchange Rate**: The value of one currency in relation to another. It determines the purchasing power of a currency in international trade. [Source: Economic Times]

- **Forex Reserves (Foreign Exchange Reserves)**: The foreign currency deposits and bonds held by central banks and monetary authorities. They serve as a buffer to stabilize the domestic currency and ensure liquidity in the foreign exchange market. [Source: IMF]



## Video Demo ▶️
To get a glimpse of how the project works and its capabilities, check out our video demo:

https://github.com/user-attachments/assets/3ac284d7-f5be-49c6-aa20-8b301f19a76f


### Usability Terms 📊

| Field              | Range                | Instructions               |
|--------------------|----------------------|----------------------------|
| Select year        | 1950 to 2050         |  Input a year within the specified range (1950-2050).        |
| Quarter            | First to Fourth Quarter |  Select a quarter from First to Fourth Quarter.            |
| GDP Growth         | 0 to 10              |  Input GDP growth rate within the range of 0 to 10.       |
| Inflation Rate     | 0 to 20              |  Input inflation rate within the range of 0 to 20.       |
| Industrial Production | -5 to 5            |  Input industrial production within the range of -5 to 5.  |
| Jobs in Market     | 10000 to 100000      |  Input number of jobs within the range of 10000 to 100000. |


## Model Accuracy



| Serial | Models                   | Description                      | Accuracy |
|--------|--------------------------|----------------------------------|----------|
| 0      | LogisticRegression()     | Logistic Regression model        | 88.44    |
| 1      | RandomForestClassifier() | RandomForest Classifier model    | 100.00   |
| 2      | DecisionTreeClassifier()| Decision Tree Classifier model   | 100.00   |
| 3      | KNN()                      | K-Nearest Neighbors model        | 86.56    |
| 4      | SVC()                      | Support Vector Classifier model  | 88.44    |




