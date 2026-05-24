CREATE VIEW bd_churn.vw_JoinData AS
SELECT * 
FROM bd_churn.prod_customer_data 
WHERE Customer_Status = 'Joined';
