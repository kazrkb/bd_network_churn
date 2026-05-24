SELECT 
    Customer_Status, 
    COUNT(Customer_Status) AS TotalCount, 
    SUM(Total_Revenue) AS TotalRev,
    ROUND((SUM(Total_Revenue) / (SELECT SUM(Total_Revenue) FROM bd_churn.customer_data)) * 100, 2) AS RevPercentage
FROM bd_churn.customer_data
GROUP BY Customer_Status;
