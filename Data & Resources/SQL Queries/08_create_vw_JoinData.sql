CREATE OR REPLACE VIEW bd_churn.vw_JoinData AS
SELECT * 
FROM bd_churn.customer_data 
WHERE Customer_Status = 'Joined';


