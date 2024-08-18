Create database project;
Create table merged_data_table(Date date,	Coal_RB_4800_FOB_London_Close_USD varchar(20),	
Coal_RB_5500_FOB_London_Close_USD varchar(20),	Coal_RB_5700_FOB_London_Close_USD varchar(20),	
Coal_RB_6000_FOB_CurrentWeek_Avg_USD varchar(20),	Coal_India_5500_CFR_London_Close_USD varchar(20));
drop table merged_data_table;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/merged_data.csv'
INTO TABLE merged_data_table
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from merged_data_table;

# First Moment Business Decision / Measures of Central Tendency

SELECT AVG(Coal_RB_4800_FOB_London_Close_USD)
FROM merged_data_table;
SELECT AVG(Coal_RB_5500_FOB_London_Close_USD)
FROM merged_data_table;
SELECT AVG(Coal_RB_5700_FOB_London_Close_USD)
FROM merged_data_table;
SELECT AVG(Coal_RB_6000_FOB_CurrentWeek_Avg_USD)
FROM merged_data_table;
SELECT AVG(Coal_India_5500_CFR_London_Close_USD)
FROM merged_data_table;

# Second Moment Business Decision / Measures of Dispersion

# Standard Deviation
SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) AS Coal_RB_4800_FOB_London_Close_USD_stddev
FROM merged_data_table;
SELECT STDDEV(Coal_RB_5500_FOB_London_Close_USD) AS Coal_RB_5500_FOB_London_Close_USD_stddev
FROM merged_data_table;
SELECT STDDEV(Coal_RB_5700_FOB_London_Close_USD) AS Coal_RB_5700_FOB_London_Close_USD_stddev
FROM merged_data_table;
SELECT STDDEV(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) AS Coal_RB_6000_FOB_CurrentWeek_Avg_USD_stddev
FROM merged_data_table;
SELECT STDDEV(Coal_India_5500_CFR_London_Close_USD) AS Coal_India_5500_CFR_London_Close_USD_stddev
FROM merged_data_table;

# Range:
SELECT MAX(Coal_RB_4800_FOB_London_Close_USD) - MIN(Coal_RB_4800_FOB_London_Close_USD) AS Coal_RB_4800_FOB_London_Close_USD_range
FROM merged_data_table;
SELECT MAX(Coal_RB_5500_FOB_London_Close_USD) - MIN(Coal_RB_5500_FOB_London_Close_USD) AS Coal_RB_5500_FOB_London_Close_USD_range
FROM merged_data_table;
SELECT MAX(Coal_RB_5700_FOB_London_Close_USD) - MIN(Coal_RB_5700_FOB_London_Close_USD) AS Coal_RB_5700_FOB_London_Close_USD_range
FROM merged_data_table;
SELECT MAX(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) - MIN(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) AS Coal_RB_6000_FOB_CurrentWeek_Avg_USD_range
FROM merged_data_table;
SELECT MAX(Coal_India_5500_CFR_London_Close_USD) - MIN(Coal_India_5500_CFR_London_Close_USD) AS Coal_India_5500_CFR_London_Close_USD_range
FROM merged_data_table;

# Variance
SELECT VARIANCE(Coal_RB_4800_FOB_London_Close_USD) AS variance_Coal_RB_4800_FOB_London_Close_USD
FROM merged_data_table;
SELECT VARIANCE(Coal_RB_5500_FOB_London_Close_USD) AS variance_Coal_RB_5500_FOB_London_Close_USD
FROM merged_data_table;
SELECT VARIANCE(Coal_RB_5700_FOB_London_Close_USD) AS variance_Coal_RB_5700_FOB_London_Close_USD
FROM merged_data_table;
SELECT VARIANCE(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) AS variance_Coal_RB_6000_FOB_CurrentWeek_Avg_USD
FROM merged_data_table;
SELECT VARIANCE(Coal_India_5500_CFR_London_Close_USD) AS variance_Coal_India_5500_CFR_London_Close_USD
FROM merged_data_table;

# Third Moment Business Decision / Skewness

SELECT
(
SUM(POWER(Coal_RB_4800_FOB_London_Close_USD- (SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data_table), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) FROM merged_data_table), 3))
) AS skewness
FROM merged_data_table;

SELECT
(
SUM(POWER(Coal_RB_5500_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5500_FOB_London_Close_USD) FROM merged_data_table), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5500_FOB_London_Close_USD) FROM merged_data_table), 3))
) AS skewness
FROM merged_data_table;

SELECT
(
SUM(POWER(Coal_RB_5700_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5700_FOB_London_Close_USD) FROM merged_data_table), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5700_FOB_London_Close_USD) FROM merged_data_table), 3))
) AS skewness
FROM merged_data_table;

SELECT
(
SUM(POWER(Coal_RB_6000_FOB_CurrentWeek_Avg_USD- (SELECT AVG(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM merged_data_table), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM merged_data_table), 3))
) AS skewness
FROM merged_data_table;

SELECT
(
SUM(POWER(Coal_India_5500_CFR_London_Close_USD- (SELECT AVG(Coal_India_5500_CFR_London_Close_USD) FROM merged_data_table), 3)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_India_5500_CFR_London_Close_USD) FROM merged_data_table), 3))
) AS skewness
FROM merged_data_table;


# Fourth Moment Business Decision / Kurtosis

SELECT
(
(SUM(POWER(Coal_RB_4800_FOB_London_Close_USD- (SELECT AVG(Coal_RB_4800_FOB_London_Close_USD) FROM MERGED_DATA_TABLE), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_4800_FOB_London_Close_USD) FROM MERGED_DATA_TABLE), 4))) - 3
) AS kurtosis
FROM MERGED_DATA_TABLE;


SELECT
(
(SUM(POWER(Coal_RB_5500_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5500_FOB_London_Close_USD) FROM MERGED_DATA_TABLE), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5500_FOB_London_Close_USD) FROM MERGED_DATA_TABLE), 4))) - 3
) AS kurtosis
FROM MERGED_DATA_TABLE;


SELECT
(
(SUM(POWER(Coal_RB_5700_FOB_London_Close_USD- (SELECT AVG(Coal_RB_5700_FOB_London_Close_USD) FROM MERGED_DATA_TABLE), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_5700_FOB_London_Close_USD) FROM MERGED_DATA_TABLE), 4))) - 3
) AS kurtosis
FROM MERGED_DATA_TABLE;


SELECT
(
(SUM(POWER(Coal_RB_6000_FOB_CurrentWeek_Avg_USD- (SELECT AVG(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM MERGED_DATA_TABLE), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_RB_6000_FOB_CurrentWeek_Avg_USD) FROM MERGED_DATA_TABLE), 4))) - 3
) AS kurtosis
FROM MERGED_DATA_TABLE;


SELECT
(
(SUM(POWER(Coal_India_5500_CFR_London_Close_USD- (SELECT AVG(Coal_India_5500_CFR_London_Close_USD) FROM MERGED_DATA_TABLE), 4)) /
(COUNT(*) * POWER((SELECT STDDEV(Coal_India_5500_CFR_London_Close_USD) FROM MERGED_DATA_TABLE), 4))) - 3
) AS kurtosis
FROM MERGED_DATA_TABLE;











