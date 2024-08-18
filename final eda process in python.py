# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:37:17 2024

@author: haroon ajaz
"""

import pandas as pd
data = pd.read_csv(r"C:\users\haroon ajaz\Desktop\merged_economic_data.csv")
# first moment decesion 
# measure of central tendency # mean
mean_1=data['Coal_RB_4800_FOB_London_Close_USD'].mean()
print(mean_1)
mean_2=data['Coal_RB_5500_FOB_London_Close_USD'].mean()
print(mean_2)
mean_3=data['Coal_RB_5700_FOB_London_Close_USD'].mean()
print(mean_3)
mean_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].mean()
print(mean_4)
mean_5=data['Coal_India_5500_CFR_London_Close_USD'].mean()
print(mean_5)
mean_6=data['Price_WTI'].mean()
print(mean_6)
mean_7=data['Price_Brent_Oil'].mean()
print(mean_7)
mean_8=data['Price_Dubai_Brent_Oil'].mean()
print(mean_8)
mean_9=data['Price_ExxonMobil'].mean()
print(mean_9)
mean_10=data['Price_NTPC'].mean()
print(mean_10)
mean_11=data['Price_Shenhua'].mean()
print(mean_11)
mean_12=data['tempmax_RB'].mean()
print(mean_12)
mean_13=data['tempmin_RB'].mean()
print(mean_13)
mean_14=data['temp_RB'].mean()
print(mean_14)
mean_15=data['dew_RB'].mean()
print(mean_15)
mean_16=data['humidity_RB'].mean()
print(mean_16)
mean_17=data['precip_RB'].mean()
print(mean_17)
mean_19=data['windspeed_RB'].mean()
print(mean_19)
mean_20=data['tempmax_Limpopo'].mean()
print(mean_20)
mean_21=data['tempmin_Limpopo'].mean()
print(mean_21)
mean_22=data['temp_Limpopo'].mean()
print(mean_22)
mean_23=data['dew_Limpopo'].mean()
print(mean_23)
mean_24=data['humidity_Limpopo'].mean()
print(mean_24)
mean_25=data['precip_Limpopo'].mean()
print(mean_25)
mean_27=data['windspeed_Limpopo'].mean()
print(mean_27)
# median
median_1=data['Coal_RB_4800_FOB_London_Close_USD'].median()
print(mean_1)
median_2=data['Coal_RB_5500_FOB_London_Close_USD'].median()
print(median_2)
median_3=data['Coal_RB_5700_FOB_London_Close_USD'].median()
print(median_3)
median_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].median()
print(median_4)
median_5=data['Coal_India_5500_CFR_London_Close_USD'].median()
print(median_5)
median_6=data['Price_WTI'].median()
print(median_6)
median_7=data['Price_Brent_Oil'].median()
print(median_7)
median_8=data['Price_Dubai_Brent_Oil'].median()
print(median_8)
median_9=data['Price_ExxonMobil'].median()
print(median_9)
median_10=data['Price_NTPC'].median()
print(median_10)
median_11=data['Price_Shenhua'].median()
print(median_11)
median_12=data['tempmax_RB'].median()
print(median_12)
median_13=data['tempmin_RB'].median()
print(median_13)
median_14=data['temp_RB'].median()
print(median_14)
median_15=data['dew_RB'].median()
print(median_15)
median_16=data['humidity_RB'].median()
print(median_16)
median_17=data['precip_RB'].median()
print(median_17)
median_19=data['windspeed_RB'].median()
print(median_19)
median_20=data['tempmax_Limpopo'].median()
print(median_20)
median_21=data['tempmin_Limpopo'].median()
print(median_21)
median_22=data['temp_Limpopo'].median()
print(median_22)
median_23=data['dew_Limpopo'].median()
print(median_23)
median_24=data['humidity_Limpopo'].median()
print(median_24)
median_25=data['precip_Limpopo'].median()
print(median_25)
median_27=data['windspeed_Limpopo'].median()
print(median_27)
#mode
mode_1=data['Coal_RB_4800_FOB_London_Close_USD'].mode()
print(mode_1)
mode_2=data['Coal_RB_5500_FOB_London_Close_USD'].mode()
print(mode_2)
mode_3=data['Coal_RB_5700_FOB_London_Close_USD'].mode()
print(mode_3)
mode_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].mode()
print(mean_4)
mode_5=data['Coal_India_5500_CFR_London_Close_USD'].mode()
print(mode_5)
mode_6=data['Price_WTI'].mode()
print(mode_6)
mode_7=data['Price_Brent_Oil'].mode()
print(mode_7)
mode_8=data['Price_Dubai_Brent_Oil'].mode()
print(mode_8)
mode_9=data['Price_ExxonMobil'].mode()
print(mode_9)
mode_10=data['Price_NTPC'].mode()
print(mode_10)
mode_11=data['Price_Shenhua'].mode()
print(mode_11)
mode_12=data['tempmax_RB'].mode()
print(mode_12)
mode_13=data['tempmin_RB'].mode()
print(mode_13)
mode_14=data['temp_RB'].mode()
print(mode_14)
mode_15=data['dew_RB'].mode()
print(mode_15)
mode_16=data['humidity_RB'].mode()
print(mode_16)
mode_17=data['precip_RB'].mode()
print(mode_17)
mode_18=data['preciptype_RB'].mode()
print(mode_18)
mode_19=data['windspeed_RB'].mode()
print(mode_19)
mode_20=data['tempmax_Limpopo'].mode()
print(mode_20)
mode_21=data['tempmin_Limpopo'].mode()
print(mode_21)
mode_22=data['temp_Limpopo'].mode()
print(mode_22)
mode_23=data['dew_Limpopo'].mode()
print(mode_23)
mode_24=data['humidity_Limpopo'].mode()
print(mode_24)
mode_25=data['precip_Limpopo'].mode()
print(mode_25)
mode_26=data['preciptype_Limpopo'].mode()
print(mode_26)
mode_27=data['windspeed_Limpopo'].mode()
print(mode_27)

## second moment decesion
# standard deviation
std_1=data['Coal_RB_4800_FOB_London_Close_USD'].std()
print(std_1)
std_2=data['Coal_RB_5500_FOB_London_Close_USD'].std()
print(std_2)
std_3=data['Coal_RB_5700_FOB_London_Close_USD'].std()
print(std_3)
std_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].std()
print(std_4)
std_5=data['Coal_India_5500_CFR_London_Close_USD'].std()
print(std_5)
std_6=data['Price_WTI'].std()
print(std_6)
std_7=data['Price_Brent_Oil'].std()
print(std_7)
std_8=data['Price_Dubai_Brent_Oil'].std()
print(std_8)
std_9=data['Price_ExxonMobil'].std()
print(std_9)
std_10=data['Price_NTPC'].std()
print(std_10)
std_11=data['Price_Shenhua'].std()
print(std_11)
std_12=data['tempmax_RB'].std()
print(std_12)
std_13=data['tempmin_RB'].std()
print(std_13)
std_14=data['temp_RB'].std()
print(std_14)
std_15=data['dew_RB'].std()
print(std_15)
std_16=data['humidity_RB'].std()
print(std_16)
std_17=data['precip_RB'].std()
print(std_17)
std_19=data['windspeed_RB'].std()
print(std_19)
std_20=data['tempmax_Limpopo'].std()
print(std_20)
std_21=data['tempmin_Limpopo'].std()
print(std_21)
std_22=data['temp_Limpopo'].std()
print(std_22)
std_23=data['dew_Limpopo'].std()
print(std_23)
std_24=data['humidity_Limpopo'].std()
print(std_24)
std_25=data['precip_Limpopo'].std()
print(std_25)
std_27=data['windspeed_Limpopo'].std()
print(std_27)

# range

range_1=data['Coal_RB_4800_FOB_London_Close_USD'].max()-data['Coal_RB_4800_FOB_London_Close_USD'].min()
print(range_1)
range_2=data['Coal_RB_5500_FOB_London_Close_USD'].max()-data['Coal_RB_5500_FOB_London_Close_USD'].min()
print(range_2)
range_3=data['Coal_RB_5700_FOB_London_Close_USD'].max()-data['Coal_RB_5700_FOB_London_Close_USD'].min()
print(range_3)
range_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].max()-data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].min()
print(range_4)
range_5=data['Coal_India_5500_CFR_London_Close_USD'].max()-data['Coal_India_5500_CFR_London_Close_USD'].min()
print(range_5)
range_6=data['Price_WTI'].max()-data['Price_WTI'].min()
print(range_6)
range_7=data['Price_Brent_Oil'].max()-data['Price_Brent_Oil'].min()
print(range_7)
range_8=data['Price_Dubai_Brent_Oil'].max()-data['Price_Dubai_Brent_Oil'].min()
print(range_8)
range_9=data['Price_ExxonMobil'].max()-data['Price_ExxonMobil'].min()
print(range_9)
range_10=data['Price_NTPC'].max()-data['Price_NTPC'].min()
print(range_10)
range_11=data['Price_Shenhua'].max()-data['Price_Shenhua'].min()
print(range_11)
range_12=data['tempmax_RB'].max()-data['tempmax_RB'].min()
print(range_12)
range_13=data['tempmin_RB'].max()-data['tempmin_RB'].min()
print(range_13)
range_14=data['temp_RB'].max()-data['temp_RB'].min()
print(range_14)
range_15=data['dew_RB'].max()-data['dew_RB'].min()
print(range_15)
range_16=data['humidity_RB'].max()-data['humidity_RB'].min()
print(range_16)
range_17=data['precip_RB'].max()-data['precip_RB'].min()
print(range_17)
range_19=data['windspeed_RB'].max()-data['windspeed_RB'].min()
print(range_19)
range_20=data['tempmax_Limpopo'].max()-data['tempmax_Limpopo'].min()
print(range_20)
range_21=data['tempmin_Limpopo'].max()-data['tempmin_Limpopo'].min()
print(range_21)
range_22=data['temp_Limpopo'].max()-data['temp_Limpopo'].min()
print(range_22)
range_23=data['dew_Limpopo'].max()-data['dew_Limpopo'].min()
print(range_23)
range_24=data['humidity_Limpopo'].max()-data['humidity_Limpopo'].min()
print(range_24)
range_25=data['precip_Limpopo'].max()-data['precip_Limpopo'].min()
print(range_25)
range_27=data['windspeed_Limpopo'].max()-data['windspeed_Limpopo'].min()
print(range_27)

#variance

var_1=data['Coal_RB_4800_FOB_London_Close_USD'].var()
print(var_1)
var_2=data['Coal_RB_5500_FOB_London_Close_USD'].var()
print(var_2)
var_3=data['Coal_RB_5700_FOB_London_Close_USD'].var()
print(var_3)
var_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].var()
print(var_4)
var_5=data['Coal_India_5500_CFR_London_Close_USD'].var()
print(var_5)
var_6=data['Price_WTI'].var()
print(var_6)
var_7=data['Price_Brent_Oil'].var()
print(var_7)
var_8=data['Price_Dubai_Brent_Oil'].var()
print(var_8)
var_9=data['Price_ExxonMobil'].var()
print(var_9)
var_10=data['Price_NTPC'].var()
print(var_10)
var_11=data['Price_Shenhua'].var()
print(var_11)
var_12=data['tempmax_RB'].var()
print(var_12)
var_13=data['tempmin_RB'].var()
print(var_13)
var_14=data['temp_RB'].var()
print(var_14)
var_15=data['dew_RB'].var()
print(var_15)
var_16=data['humidity_RB'].var()
print(var_16)
var_17=data['precip_RB'].var()
print(var_17)
var_19=data['windspeed_RB'].var()
print(var_19)
var_20=data['tempmax_Limpopo'].var()
print(var_20)
var_21=data['tempmin_Limpopo'].var()
print(var_21)
var_22=data['temp_Limpopo'].var()
print(var_22)
var_23=data['dew_Limpopo'].var()
print(var_23)
var_24=data['humidity_Limpopo'].var()
print(var_24)
var_25=data['precip_Limpopo'].var()
print(var_25)
var_27=data['windspeed_Limpopo'].var()
print(var_27)


## third moment decesion
# skewness

skew_1=data['Coal_RB_4800_FOB_London_Close_USD'].skew()
print(skew_1)
skew_2=data['Coal_RB_5500_FOB_London_Close_USD'].skew()
print(skew_2)
skew_3=data['Coal_RB_5700_FOB_London_Close_USD'].skew()
print(skew_3)
skew_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].skew()
print(skew_4)
skew_5=data['Coal_India_5500_CFR_London_Close_USD'].skew()
print(skew_5)
skew_6=data['Price_WTI'].skew()
print(skew_6)
skew_7=data['Price_Brent_Oil'].skew()
print(skew_7)
skew_8=data['Price_Dubai_Brent_Oil'].skew()
print(skew_8)
skew_9=data['Price_ExxonMobil'].skew()
print(skew_9)
skew_10=data['Price_NTPC'].skew()
print(skew_10)
skew_11=data['Price_Shenhua'].skew()
print(skew_11)
skew_12=data['tempmax_RB'].skew()
print(skew_12)
skew_13=data['tempmin_RB'].skew()
print(skew_13)
skew_14=data['temp_RB'].skew()
print(skew_14)
skew_15=data['dew_RB'].skew()
print(skew_15)
skew_16=data['humidity_RB'].skew()
print(skew_16)
skew_17=data['precip_RB'].skew()
print(skew_17)
skew_19=data['windspeed_RB'].skew()
print(skew_19)
skew_20=data['tempmax_Limpopo'].skew()
print(skew_20)
skew_21=data['tempmin_Limpopo'].skew()
print(skew_21)
skew_22=data['temp_Limpopo'].skew()
print(skew_22)
skew_23=data['dew_Limpopo'].skew()
print(skew_23)
skew_24=data['humidity_Limpopo'].skew()
print(skew_24)
skew_25=data['precip_Limpopo'].skew()
print(skew_25)
skew_27=data['windspeed_Limpopo'].skew()
print(skew_27)

# fourth moment decesion
# kurtosis
kurt_1=data['Coal_RB_4800_FOB_London_Close_USD'].kurtosis()
print(kurt_1)
kurt_2=data['Coal_RB_5500_FOB_London_Close_USD'].kurtosis()
print(kurt_2)
kurt_3=data['Coal_RB_5700_FOB_London_Close_USD'].kurtosis()
print(kurt_3)
kurt_4=data['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].kurtosis()
print(kurt_4)
kurt_5=data['Coal_India_5500_CFR_London_Close_USD'].kurtosis()
print(kurt_5)
kurt_6=data['Price_WTI'].kurtosis()
print(kurt_6)
kurt_7=data['Price_Brent_Oil'].kurtosis()
print(kurt_7)
kurt_8=data['Price_Dubai_Brent_Oil'].kurtosis()
print(kurt_8)
kurt_9=data['Price_ExxonMobil'].kurtosis()
print(kurt_9)
kurt_10=data['Price_NTPC'].kurtosis()
print(kurt_10)
kurt_11=data['Price_Shenhua'].kurtosis()
print(kurt_11)
kurt_12=data['tempmax_RB'].kurtosis()
print(kurt_12)
kurt_13=data['tempmin_RB'].kurtosis()
print(kurt_13)
kurt_14=data['temp_RB'].kurtosis()
print(kurt_14)
kurt_15=data['dew_RB'].kurtosis()
print(kurt_15)
kurt_16=data['humidity_RB'].kurtosis()
print(kurt_16)
kurt_17=data['precip_RB'].kurtosis()
print(kurt_17)
kurt_19=data['windspeed_RB'].kurtosis()
print(kurt_19)
kurt_20=data['tempmax_Limpopo'].kurtosis()
print(kurt_20)
kurt_21=data['tempmin_Limpopo'].kurtosis()
print(kurt_21)
kurt_22=data['temp_Limpopo'].kurtosis()
print(kurt_22)
kurt_23=data['dew_Limpopo'].kurtosis()
print(kurt_23)
kurt_24=data['humidity_Limpopo'].kurtosis()
print(kurt_24)
kurt_25=data['precip_Limpopo'].kurtosis()
print(kurt_25)
kurt_27=data['windspeed_Limpopo'].kurtosis()
print(kurt_27)


## graphical representation

import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10, 6))

# Univariate Analysis
# Histogram for Coal_RB_4800_FOB_London_Close_USD
plt.hist(data['Coal_RB_4800_FOB_London_Close_USD'], bins=20)
plt.title('Histogram of Coal_RB_4800_FOB_London_Close_USD')
plt.xlabel('Coal_RB_4800_FOB_London_Close_USD')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# defing the functioning to plot the histogram for all the columns by using the for loop .

data.describe
data.columns
#list of columns 

columns = [
    'Coal_RB_5500_FOB_London_Close_USD',
    'Coal_RB_5700_FOB_London_Close_USD',
    'Coal_RB_6000_FOB_CurrentWeek_Avg_USD',
    'Coal_India_5500_CFR_London_Close_USD',
    'Price_WTI',
    'Price_Brent_Oil',
    'Price_Dubai_Brent_Oil',
    'Price_ExxonMobil',
    'Price_NTPC',
    'Price_Shenhua',
    'tempmax_RB',
    'tempmin_RB',
    'temp_RB',
    'dew_RB',
    'humidity_RB',
    'precip_RB',
    'windspeed_RB',
    'tempmax_Limpopo',
    'tempmin_Limpopo',
    'temp_Limpopo',
    'dew_Limpopo',
    'humidity_Limpopo',
    'precip_Limpopo',
    'windspeed_Limpopo'
]


# function to plot the histogram for each given column
import pandas as pd
import matplotlib.pyplot as plt





# Function to plot the histogram for each given column
def plot_histogram(column):
    plt.hist(data[column].dropna(), bins=20)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Plot histograms for each column
for column in columns:
    plot_histogram(column)

    
    
    
import pandas as pd   
import seaborn as sns    
import matplotlib.pyplot as plt    

#loaded data
data=pd.read_csv(r"C:\users\haroon ajaz\Desktop\merged_economic_data.csv")    
    
    
# Selecting columns for correlation
columns_of_interest = ['Coal_RB_5500_FOB_London_Close_USD',
'Coal_RB_5700_FOB_London_Close_USD',
'Coal_RB_6000_FOB_CurrentWeek_Avg_USD',
'Coal_India_5500_CFR_London_Close_USD',
'Price_WTI',
'Price_Brent_Oil',
'Price_Dubai_Brent_Oil',
'Price_ExxonMobil',
'Price_NTPC',
'Price_Shenhua',
'tempmax_RB',
'tempmin_RB',
'temp_RB',
'dew_RB',
'humidity_RB',
'precip_RB',
'windspeed_RB',
'tempmax_Limpopo',
'tempmin_Limpopo',
'temp_Limpopo',
'dew_Limpopo',
'humidity_Limpopo',
'precip_Limpopo',
'windspeed_Limpopo'
]
# Calculate correlation matrix
corr = data[columns_of_interest].corr()

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Commodity Prices and Weather')
plt.show()
    
     
# data cleansing or data preprocessing 
# type casting
# handling duplicates
# outlier treatment
# zero and near zero variances features
# missing values
# normalization
# discretization/binning/grouping
#dummy variable creation
# transformations


### Identify duplicate records in the data ###
import pandas as pd
data = pd.read_csv(r"C:\users\haroon ajaz\Desktop\merged_economic_data.csv")

# Duplicates in rows
help(data.duplicated)

duplicate = data.duplicated()  # Returns Boolean Series denoting duplicate rows.
duplicate

sum(duplicate)


# Removing Duplicates
data1 = data.drop_duplicates() # Returns DataFrame with duplicate rows removed.

# Parameters

data1 = data.drop_duplicates(keep = 'last')

data1 = data.drop_duplicates(keep = False)


# Duplicates in Columns
# We can use correlation coefficient values to identify columns which have duplicate information

import pandas as pd

data = pd.read_csv(r"C:\users\haroon ajaz\Desktop\merged_economic_data.csv")


# replacing the missing values with 

categoriacal_columns = data.select_dtypes(include=['object']).columns
data['preciptype_RB']=data['preciptype_RB'].fillna('no rain')
print(data)


categoriacal_columns = data.select_dtypes(include=['object']).columns
data['preciptype_Limpopo']=data['preciptype_Limpopo'].fillna('no rain')
print(data)

### forward fill on the misssing values in the numerical column
forward_fill=data.ffill(inplace =True)
data.isnull().sum()
backward_fill=data.bfill(inplace =True)
data.isnull().sum()

### replacing the outliers with the nan values

import pandas as pd
import numpy as np

def replace_outliers(df):
    # Iterate through all numeric columns
    for column in data.select_dtypes(include=['number']).columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data[column] = np.where((data[column] > upper_bound) | (data[column] < lower_bound), np.nan, data[column])
    return data
replace_outliers(data)
### performing linear interpolation on data
import pandas as pd
import numpy as np

import pandas as pd

#
# Perform linear interpolation
df_interpolated = data.interpolate(method='linear',limit_direction='both',inplace=True)

print(df_interpolated)
data.dtypes
# how to convert data into csv file 
df_interpolated.to_csv('df_interpolated.csv',index = False)
 
### auto eda libraries
# Auto EDA
# Sweetviz
# Autoviz
# Dtale
# Pandas Profiling
# Dataprep

# sweetviz
#pip install sweetviz

import sweetviz as sv
s = sv.analyze(data)
s.show_html()

#Dtale
import dtale
import pandas as pd

df = pd.DataFrame(data)

d = dtale.show(df)
d.open_browser()


# typecasting converting object int float

df_interpolated.dtypes
data['Date'] = pd.to_datetime(data['Date'])

# converting data into csv file

data.to_csv('coal analysis eda.csv', index = False)






