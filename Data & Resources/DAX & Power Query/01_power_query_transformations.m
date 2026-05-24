// --------------------------------------------------------
// Power Query Transformations for bd_networking_churn
// --------------------------------------------------------

// 1. Add a new column in prod_Churn
Churn Status = if [Customer_Status] = "Churned" then 1 else 0
// -> Change Churn Status data type to numbers

// 2. Add Monthly Charge Range column
Monthly Charge Range = if [Monthly_Charge] < 20 then "< 20" else if [Monthly_Charge] < 50 then "20-50" else if [Monthly_Charge] < 100 then "50-100" else "> 100"

// --------------------------------------------------------
// 3. Create a New Table Reference for mapping_AgeGrp
// -> Keep only Age column and remove duplicates
Age Group = if [Age] < 20 then "< 20" else if [Age] < 36 then "20 - 35" else if [Age] < 51 then "36 - 50" else "> 50"
AgeGrpSorting = if [Age Group] = "< 20" then 1 else if [Age Group] = "20 - 35" then 2 else if [Age Group] = "36 - 50" then 3 else 4
// -> Change data type of AgeGrpSorting to numbers

// --------------------------------------------------------
// 4. Create a new table reference for mapping_TenureGrp
// -> Keep only Tenure_in_Months and remove duplicates
Tenure Group = if [Tenure_in_Months] < 6 then "< 6 Months" else if [Tenure_in_Months] < 12 then "6-12 Months" else if [Tenure_in_Months] < 18 then "12-18 Months" else if [Tenure_in_Months] < 24 then "18-24 Months" else ">= 24 Months"
TenureGrpSorting = if [Tenure_in_Months] = "< 6 Months" then 1 else if [Tenure_in_Months] =  "6-12 Months" then 2 else if [Tenure_in_Months] = "12-18 Months" then 3 else if [Tenure_in_Months] = "18-24 Months " then 4 else 5
// -> Change data type of TenureGrpSorting to numbers

// --------------------------------------------------------
// 5. Create a new table reference for prod_Services
// -> Unpivot services columns
// -> Rename Columns: Attribute >> Services | Value >> Status
