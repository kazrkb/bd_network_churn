SELECT 
    Contract, 
    COUNT(Contract) AS TotalCount,
    ROUND((COUNT(Contract) / (SELECT COUNT(*) FROM bd_churn.customer_data)) * 100, 2) AS Percentage
FROM bd_churn.customer_data
GROUP BY Contract;
