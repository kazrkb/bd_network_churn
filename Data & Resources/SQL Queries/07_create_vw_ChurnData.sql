CREATE VIEW bd_churn.vw_ChurnData AS
SELECT * 
FROM bd_churn.prod_customer_data 
WHERE Customer_Status IN ('Churned', 'Stayed');
