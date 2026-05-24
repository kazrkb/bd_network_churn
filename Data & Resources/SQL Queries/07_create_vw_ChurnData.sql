CREATE OR REPLACE VIEW bd_churn.vw_ChurnData AS
SELECT * 
FROM bd_churn.customer_data 
WHERE Customer_Status IN ('Churned', 'Stayed');
