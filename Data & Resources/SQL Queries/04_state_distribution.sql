SELECT 
    State, 
    COUNT(State) AS TotalCount,
    ROUND((COUNT(State) / (SELECT COUNT(*) FROM bd_churn.customer_data)) * 100, 2) AS Percentage
FROM bd_churn.customer_data
GROUP BY State
ORDER BY Percentage DESC;
