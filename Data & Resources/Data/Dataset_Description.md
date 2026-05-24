# Bangladesh Telecom Customer Churn Dataset

## Overview

This dataset contains **6,418 customer records** from a telecommunications company operating across all **8 administrative divisions of Bangladesh**. It captures customer demographics, service subscriptions, billing information, and churn behavior — making it suitable for customer churn prediction, segmentation analysis, and business intelligence tasks.

---

## Dataset Summary

| Property             | Value                  |
|----------------------|------------------------|
| **Total Records**    | 6,418                  |
| **Total Features**   | 32 (including target)  |
| **File Format**      | CSV                    |
| **Target Variable**  | Customer_Status        |
| **Geographic Scope** | Bangladesh (8 divisions) |
| **Age Range**        | 18 – 85 years          |
| **Missing Values**   | None (0)               |

---

## Column Descriptions

### Customer Information

| Column                 | Data Type   | Description                                                     |
|------------------------|-------------|-----------------------------------------------------------------|
| `Customer_ID`          | String      | Unique customer identifier (format: `XXXXX-DIV`, e.g., `19877-DHK`) |
| `Gender`               | Categorical | Customer gender — `Male` (2,370) or `Female` (4,048)           |
| `Age`                  | Integer     | Customer age in years (range: 18–85)                            |
| `Married`              | Categorical | Marital status — `Yes` (3,195) or `No` (3,223)                 |
| `State`                | Categorical | Administrative division of Bangladesh (see Division Breakdown)  |
| `Number_of_Referrals`  | Integer     | Number of referrals made by the customer                        |
| `Tenure_in_Months`     | Integer     | Duration of the customer's relationship with the company (months)|

### Service Details

| Column                   | Data Type   | Description                                                   |
|--------------------------|-------------|---------------------------------------------------------------|
| `Value_Deal`             | Categorical | Active promotional deal — `Deal 1` through `Deal 5`, or `No Deal` |
| `Phone_Service`          | Categorical | Whether the customer has phone service — `Yes` / `No`         |
| `Multiple_Lines`         | Categorical | Whether the customer has multiple phone lines — `Yes` / `No`  |
| `Internet_Service`       | Categorical | Whether the customer has internet service — `Yes` / `No`      |
| `Internet_Type`          | Categorical | Type of internet connection — `Fiber Optic` (4,266), `Mobile Broadband` (762), or `None` (1,390) |
| `Online_Security`        | Categorical | Online security add-on — `Yes` / `No`                         |
| `Online_Backup`          | Categorical | Online backup add-on — `Yes` / `No`                           |
| `Device_Protection_Plan` | Categorical | Device protection add-on — `Yes` / `No`                       |
| `Premium_Support`        | Categorical | Premium tech support — `Yes` / `No`                           |
| `Streaming_TV`           | Categorical | TV streaming service — `Yes` / `No`                           |
| `Streaming_Movies`       | Categorical | Movie streaming service — `Yes` / `No`                        |
| `Streaming_Music`        | Categorical | Music streaming service — `Yes` / `No`                        |
| `Unlimited_Data`         | Categorical | Unlimited data plan — `Yes` / `No`                            |

### Billing & Contract

| Column                        | Data Type   | Description                                                        |
|-------------------------------|-------------|--------------------------------------------------------------------|
| `Contract`                    | Categorical | Contract type — `Month-to-Month` (3,286), `One Year` (1,413), `Two Year` (1,719) |
| `Paperless_Billing`           | Categorical | Whether the customer uses paperless billing — `Yes` / `No`         |
| `Payment_Method`              | Categorical | Payment method — `Credit Card` (2,494), `Bank Withdrawal` (3,575), `Mobile Banking (bKash/Nagad)` (349) |
| `Monthly_Charge`              | Float       | Monthly charge amount in BDT (avg ~477, range -75 to 891)         |
| `Total_Charges`               | Float       | Total charges over the customer's tenure in BDT                    |
| `Total_Refunds`               | Float       | Total refunds issued to the customer in BDT                        |
| `Total_Extra_Data_Charges`    | Float       | Total extra data charges incurred in BDT                           |
| `Total_Long_Distance_Charges` | Float       | Total long distance call charges in BDT                            |
| `Total_Revenue`               | Float       | Total revenue generated from the customer in BDT (avg ~22,754)     |

### Target / Churn Variables

| Column            | Data Type   | Description                                                              |
|-------------------|-------------|--------------------------------------------------------------------------|
| `Customer_Status` | Categorical | Current customer status — `Stayed` (4,275), `Churned` (1,732), `Joined` (411) |
| `Churn_Category`  | Categorical | Reason category for churn — `Competitor`, `Attitude`, `Dissatisfaction`, `Price`, `Other`, or `Not Applicable` |
| `Churn_Reason`    | String      | Specific reason for churn, or `Not Applicable` for non-churned customers |

---

## Division Breakdown

| Division       | Records | Percentage |
|----------------|---------|------------|
| **Dhaka**      | 1,260   | 19.6%      |
| **Khulna**     | 1,111   | 17.3%      |
| **Rajshahi**   | 876     | 13.6%      |
| **Chattogram** | 817     | 12.7%      |
| **Barishal**   | 740     | 11.5%      |
| **Sylhet**     | 667     | 10.4%      |
| **Rangpur**    | 656     | 10.2%      |
| **Mymensingh** | 291     | 4.5%       |

---

## Customer Status Distribution

| Status      | Count | Percentage |
|-------------|-------|------------|
| **Stayed**  | 4,275 | 66.6%      |
| **Churned** | 1,732 | 27.0%      |
| **Joined**  | 411   | 6.4%       |

---

## Churn Category Breakdown (Churned Customers Only)

| Category            | Count | Percentage |
|---------------------|-------|------------|
| **Competitor**      | 761   | 43.9%      |
| **Attitude**        | 301   | 17.4%      |
| **Dissatisfaction** | 300   | 17.3%      |
| **Price**           | 196   | 11.3%      |
| **Other**           | 174   | 10.1%      |

---

## Potential Use Cases

- **Customer Churn Prediction** — Build classification models to predict which customers are likely to churn
- **Customer Segmentation** — Cluster customers based on demographics, services, and billing patterns
- **Revenue Analysis** — Analyze revenue drivers across divisions and service types
- **Service Optimization** — Identify which services and contract types lead to higher retention
- **Geographic Analysis** — Compare churn rates and customer behavior across Bangladesh's divisions

---

## Notes

- **No missing values** — all blank cells have been filled with contextually appropriate defaults
- `Value_Deal = "No Deal"` indicates the customer has no active promotional deal
- `Internet_Type = "None"` indicates the customer does not have internet service
- `Churn_Category` and `Churn_Reason` are `"Not Applicable"` for non-churned customers (Stayed/Joined)
- The `Customer_ID` suffix corresponds to the division abbreviation: DHK (Dhaka), CTG (Chattogram), KHU (Khulna), RAJ (Rajshahi), RAN (Rangpur), SYL (Sylhet), BAR (Barishal), MYM (Mymensingh)
- All monetary values are in **Bangladeshi Taka (BDT)**
- `Internet_Type` reflects Bangladesh's current infrastructure: `Fiber Optic` (dominant) and `Mobile Broadband` (4G/5G)
- `Payment_Method` includes `Mobile Banking (bKash/Nagad)` — the most popular digital payment platform in Bangladesh
