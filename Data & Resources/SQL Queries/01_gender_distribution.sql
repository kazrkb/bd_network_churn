SELECT 
    Gender, 
    COUNT(Gender) AS TotalCount,
    ROUND((COUNT(Gender) / (SELECT COUNT(*) FROM bd_churn.customer_data)) * 100, 2) AS Percentage
FROM bd_churn.customer_data
GROUP BY Gender;
