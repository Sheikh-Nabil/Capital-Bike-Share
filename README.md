#  Capital Bike Share Washington DC


<p align="center">
  <img width="500" height="300" src="https://mobilitylab.org/wp-content/uploads/2016/06/Penn-CaBi-Elvert-Barnes.jpg">
</p>



# Table of Contents
1. [Introduction](#Introduction)
2. [The Data](#The-Data)
3. [Data processing](Data-Processinng)
4. [Basic Exploratory Analysis](#Basic-Exploratory-Analysis)
5. [Facebook Prophet](#facebook-Prophet)
6. [Flask App](#Flask-App)
7. [End Note](#End-Note)


## Introduction 

This project focuses on the bike share business of the famous bike share company [Capital Bike Share](https://www.capitalbikeshare.com/). The main goal here is to work with some previous data, analyse it following time series prediction and finally publish it using Heroku based on a machine learning model. 

## The data:
All the data used in this project are included in the respective folders. The data was collected from the capital bike share [website](https://www.capitalbikeshare.com/system-data) where they publish their bike ride data. There are data from two different timeframe 2011-12, and 2018-19-20. Al the used data included in this project were in .json format and transformed into .csv format for further analysis.  

## Data Wrangling:

This part we wrangle the raw data to an excecutable format. Although Capital Bike Share provides very well structured data compared to other data sources but to make the data useful for using in exploratory analysis and machine learning model, we preapared the data as it needed to be. Data wrangling, sometimes referred to as data munging, is the process of transforming and mapping data from one "raw" data form into another format with the intent of making it more appropriate and valuable for a variety of downstream purposes such as analytics. There is a silver lining between data processing and of data wrangling which we used.Please refer [here](https://en.wikipedia.org/wiki/Data_wrangling) to have a bit understanding of our used process. 


## Basic Exploratory Analysis:

This part of the project focuses mainly on processing of the data to get insights such as:
 1. Daily total users based on the seasonality. 
 2. Weekly bike distribution based on temmprature and working day. 
 3. Monthly user  distributation. 
 4. monthly distribution of total users based on the data. 
 5. User count based on temparature. 
 6. Weather dependency on bike demand.

analysis credit for [Davide Della Valle](https://github.com/davidellavalle). 


## Facebook Prophet:

According to the official [website](https://facebook.github.io/prophet/), Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.




## Flask App: 

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.


## End Note:

Please follow the social media links of the author_

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->

<!-- display the social media buttons in your README -->


[![alt text][1.1]][1]
[![alt text][2.1]][2]


<!-- links to social media icons -->
<!-- no need to change these -->

<!-- icons with padding -->


[1.1]: http://i.imgur.com/yCsTjba.png (google plus icon with padding)
[2.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

<!-- icons without padding -->


[1.2]: http://i.imgur.com/VlgBKQ9.png (google plus icon without padding)
[2.2]: http://i.imgur.com/9I6NRUm.png (github icon without padding)


<!-- links to your social media accounts -->
<!-- update these accordingly -->


[1]: https://myaccount.google.com/profile
[2]: https://github.com/Sheikh-Nabil

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->