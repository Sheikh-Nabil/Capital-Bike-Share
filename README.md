#  Capital Bike Share Washington DC


# Table of Contents
1. [Introduction](#Introduction)
2. [The Data](#The-Data)
3. [Data Wrangling](#Data-Wrangling)
4. [Basic Exploratory Analysis](#Basic-Exploratory-Analysis)
5. [Facebook Prophet](#facebook-Prophet)
6. [Flask App](#Flask-App)
7. [End Note](#End-Note)

<p align="center">
  <img width="500" height="300" src="https://cdn.vox-cdn.com/thumbor/1ZuKzZDhEda7zQjFfsADOTY45iI=/0x0:5148x3793/1200x800/filters:focal(2163x1486:2985x2308)/cdn.vox-cdn.com/uploads/chorus_image/image/65091873/shutterstock_400258885.0.jpg">
</p>



## Introduction 

This project focuses on the bike share business of the famous bike share company [Capital Bike Share](https://www.capitalbikeshare.com/). According to their official document Capital Bikeshare is metro DC's largest bikeshare service, with 
4,500 bikes and 500+ stations across 7 jurisdictions: Washington, DC.; Arlington, VA; Alexandria, VA; Montgomery, MD; Prince George's County, MD; Fairfax County, VA; and the City of Falls Church, VA. Designed for quick trips with convenience in mind, it’s a fun and affordable way to get around. 
The main objectives of this project is to work with  previous data from capital bike share, analyse it following time series prediction and finally publish it using Heroku based on a machine learning model.


<p align="left">
<a href="https://www.animatedimages.org/cat-wine-706.htm"><img src="https://www.animatedimages.org/data/media/706/animated-wine-image-0005.gif" border="0" alt="animated-wine-image-0005" /></a><br></pre>
</details>

## Used Tools:

![](https://img.shields.io/badge/Wrangling-Python-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/Visualization-SNS_Matplotlib-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/ML-AdaBoost-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/Timeseries-FB_Prophet-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)

![](https://img.shields.io/badge/Deployment-Flask_Heroku-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=2bbc8a)



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



## Facebook Prophet: 

<p align="center">
  <img width="300" height="100" src="https://cdn.analyticsvidhya.com/wp-content/uploads/2018/05/tumblr_inline_omh3tnv5zk1r1x9ql_500.png">
</p>

According to the official [website](https://facebook.github.io/prophet/), Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

Useful resources for further development- 

. [Homepage](https://facebook.github.io/prophet/)

. [Source code repository](https://github.com/facebook/prophet)

. [Prophet Python package](https://pypi.python.org/pypi/fbprophet)



## Flask App: 

<p align="center">
  <img width="300" height="100" src="https://www.codeacademyberlin.com/static/ecdc3d3b1090c073cbccd8d542bc50e7/flask.svg">
</p>

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.In this stage, we made an app with Flask to get a prediction of rented bikes per hour by using AdaBoostRegressor as regression. It takes an input of weekday, hour, month, member type and is a holiday or not, and gives a prediction of bike usage within the hour. The app is launched on [Heroku](https://devcenter.heroku.com/) which can be accessed [here](https://bike-share-count.herokuapp.com).



[![Flask App Deployment Tutorial](http://img.youtube.com/vi/n8yXd4tZylg/0.jpg)](http://www.youtube.com/watch?v=n8yXd4tZylg "Flask App Deployment Tutorial")

Tutorial Credit [Sekhar Biswas](https://github.com/shekharbiswas).

Timeseries analysis credit for [Davide Della Valle](https://github.com/davidellavalle).



## End Note:

As the data of Capital Bike Share get uploaded every month so this is an ongoing project. More Modification wil follow. Thanks a lot for reading. 
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