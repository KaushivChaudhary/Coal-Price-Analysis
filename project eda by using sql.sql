create database projects;
use projects;
	Create table merged_data(Date date,	Coal_RB_4800_FOB_London_Close_USD varchar(20),	
Coal_RB_5500_FOB_London_Close_USD varchar(20),	Coal_RB_5700_FOB_London_Close_USD varchar(20),	
Coal_RB_6000_FOB_CurrentWeek_Avg_USD varchar(20),	Coal_India_5500_CFR_London_Close_USD varchar(20));
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/merged_data_csv.csv"
INTO TABLE merged_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
select * from merged_data;

# First Moment Business Decision / Measures of Central Tendency

SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data;
SELECT  AVG(Coal_RB_5500_FOB_London_Close_USD) FROM merged_data;
SELECT AVG(Coal_RB_5700_FOB_London_Close_USD) FROM merged_data;
SELECT AVG(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM merged_data;
SELECT AVG(	Coal_India_5500_CFR_London_Close_USD) FROM merged_data;

# Second Moment Business Decision / Measures of Dispersion

SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) AS Coal_RB_4800_FOB_London_Close_USD_stddev
FROM merged_data;
SELECT STDDEV(Coal_RB_5500_FOB_London_Close_USD) AS Coal_RB_5500_FOB_London_Close_USD_stddev
 FROM merged_data;
 SELECT STDDEV(Coal_RB_5700_FOB_London_Close_USD) AS Coal_RB_5700_FOB_London_Close_USD_stddev
 FROM merged_data;
 SELECT STDDEV(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) As Coal_RB_6000_FOB_CurrentWeek_Avg_USD_stddev
 FROM merged_data;
 SELECT STDDEV(Coal_India_5500_CFR_London_Close_USD) As Coal_India_5500_CFR_London_Close_USD_stddev
 FROM merged_data;
 
 # Range:
 
SELECT MAX(Coal_RB_4800_FOB_London_Close_USD) - MIN(Coal_RB_4800_FOB_London_Close_USD) AS Coal_RB_4800_FOB_London_Close_USD_range
FROM merged_data;
SELECT MAX(Coal_RB_5500_FOB_London_Close_USD) -MIN(Coal_RB_5500_FOB_London_Close_USD) As Coal_RB_5500_FOB_London_Close_USD_range
FROM merged_data;
SELECT MAX(Coal_RB_5700_FOB_London_Close_USD) -MIN(Coal_RB_5700_FOB_London_Close_USD) As Coal_RB_5700_FOB_London_Close_USD_range
FROM merged_data;
SELECT MAX(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) - MIN(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) As Coal_RB_6000_FOB_CurrentWeek_Avg_USD_range
FROM merged_data;
SELECT MAX(Coal_India_5500_CFR_London_Close_USD) -MIN(Coal_India_5500_CFR_London_Close_USD) As Coal_India_5500_CFR_London_Close_USD_range
FROM merged_data;

# Variance
SELECT VARIANCE(Coal_RB_4800_FOB_London_Close_USD) AS variance_Coal_RB_4800_FOB_London_Close_USD
FROM merged_data_table; 
SELECT VARIANCE(Coal_RB_5500_FOB_London_Close_USD) AS variance_Coal_RB_5500_FOB_London_Close_USD
FROM merged_data;
SELECT VARIANCE(Coal_RB_5700_FOB_London_Close_USD) AS variance_Coal_RB_5700_FOB_London_Close_USD
FROM merged_data;
SELECT VARIANCE(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) AS variance_Coal_RB_6000_FOB_CurrentWeek_Avg_USD
FROM merged_data;
SELECT VARIANCE(Coal_India_5500_CFR_London_Close_USD) AS variance_Coal_India_5500_CFR_London_Close_USD
FROM merged_data;

# Third Moment Business Decision / Skewness

SELECT
(
SUM(POWER(Coal_RB_4800_FOB_London_Close_USD- (SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data), 3))
) AS skewness FROM merged_data;

SELECT
(
SUM(POWER(Coal_RB_5500_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5500_FOB_London_Close_USD) FROM merged_data), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5500_FOB_London_Close_USD) FROM merged_data), 3))
) AS skewness FROM merged_data;

SELECT
(
SUM(POWER(Coal_RB_5700_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5700_FOB_London_Close_USD) FROM merged_data), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5700_FOB_London_Close_USD) FROM merged_data), 3))
) AS skewness
FROM merged_data;

SELECT
(
SUM(POWER(Coal_RB_6000_FOB_CurrentWeek_Avg_USD- (SELECT AVG(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM merged_data), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM merged_data), 3))
) AS skewness
FROM merged_data;

SELECT
(
SUM(POWER(Coal_India_5500_CFR_London_Close_USD- (SELECT AVG(Coal_India_5500_CFR_London_Close_USD) FROM merged_data), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_India_5500_CFR_London_Close_USD) FROM merged_data), 3))
) AS skewness
FROM merged_data;


# Fourth Moment Business Decision / Kurtosis

SELECT
(
(SUM(POWER(Coal_RB_4800_FOB_London_Close_USD- (SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM MERGED_DATA), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) FROM MERGED_DATA), 4))) - 3
) AS kurtosis
FROM MERGED_DATA;


SELECT
(
(SUM(POWER(Coal_RB_5500_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5500_FOB_London_Close_USD) FROM MERGED_DATA), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5500_FOB_London_Close_USD) FROM MERGED_DATA), 4))) - 3
) AS kurtosis
FROM MERGED_DATA;


SELECT
(
(SUM(POWER(Coal_RB_5700_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5700_FOB_London_Close_USD) FROM MERGED_DATA), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5700_FOB_London_Close_USD) FROM MERGED_DATA), 4))) - 3
) AS kurtosis
FROM MERGED_DATA;


SELECT
(
(SUM(POWER(Coal_RB_6000_FOB_CurrentWeek_Avg_USD- (SELECT AVG(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM MERGED_DATA), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM MERGED_DATA), 4))) - 3
) AS kurtosis
FROM MERGED_DATA;


SELECT
(
(SUM(POWER(Coal_India_5500_CFR_London_Close_USD- (SELECT AVG(Coal_India_5500_CFR_London_Close_USD) FROM MERGED_DATA), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_India_5500_CFR_London_Close_USD) FROM MERGED_DATA), 4))) - 3
) AS kurtosis
FROM MERGED_DATA;
