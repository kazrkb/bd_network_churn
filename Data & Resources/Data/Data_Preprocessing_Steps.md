# Data Preprocessing Steps

This document outlines the step-by-step preprocessing applied to the raw telecom customer churn dataset to transform it into the clean, Bangladesh-specific dataset we have now.

---

## 1. Geographic & Identifier Mapping

The original dataset contained geographic data for India, which was remapped to Bangladesh's administrative divisions to contextualize the data.

*   **State Mapping**: 22 Indian States and Union Territories were consolidated into **8 Bangladesh Divisions** (Dhaka, Chattogram, Khulna, Rajshahi, Rangpur, Sylhet, Barishal, Mymensingh) based on a proportional distribution.
*   **Customer ID Suffix Update**: The `Customer_ID` field originally ended with Indian state abbreviations (e.g., `-DEL`, `-MAH`). These were replaced with the corresponding 3-letter abbreviations of the new Bangladesh divisions (e.g., `-DHK`, `-CTG`) to maintain data consistency.

## 2. Infrastructure & Service Adaptation

Certain categorical values were outdated or not reflective of the Bangladesh telecom market. These were updated to match local realities:

*   **Internet Type Replacements**:
    *   `DSL` (1,502 rows) → **`Fiber Optic`**: DSL is largely obsolete in Bangladesh; Fiber Optic (FTTH) is the dominant broadband technology.
    *   `Cable` (762 rows) → **`Mobile Broadband`**: Coaxial cable internet is rare; Mobile Broadband (4G/5G) is the primary alternative to Fiber Optic.
*   **Payment Method Replacements**:
    *   `Mailed Check` (349 rows) → **`Mobile Banking (bKash/Nagad)`**: Mailed checks are virtually non-existent for telecom payments in Bangladesh, whereas Mobile Financial Services (MFS) like bKash and Nagad dominate the market.

## 3. Financial Transformation (Currency Conversion)

The financial columns in the original dataset used generic or USD-like numerical values that were not realistic for the Bangladeshi market.

*   **Conversion to BDT**: All six monetary columns were multiplied by a factor of **7.5** to convert the generic values into realistic **Bangladeshi Taka (BDT)**.
    *   `Monthly_Charge`
    *   `Total_Charges`
    *   `Total_Refunds`
    *   `Total_Extra_Data_Charges`
    *   `Total_Long_Distance_Charges`
    *   `Total_Revenue`
*   *Result*: The average monthly charge shifted from ~63.65 to a realistic **~477 BDT**, perfectly aligning with typical BD telecom packages.

## 4. Missing Value Imputation

The original dataset contained **26,052 missing (blank) values** across 13 columns. These were not random errors, but rather structural missingness based on customer subscriptions. All missing values were imputed using deterministic, context-aware logic:

| Feature(s) | Blank Count | Imputation Rule Applied | Rationale |
| :--- | :--- | :--- | :--- |
| `Value_Deal` | 3,548 | Replaced with **`"No Deal"`** | The customer was not subscribed to any promotional deal. |
| `Multiple_Lines` | 622 | Replaced with **`"No"`** | These customers had `Phone_Service = "No"`. Without phone service, multiple lines cannot exist. |
| `Internet_Type` | 1,390 | Replaced with **`"None"`** | These customers had `Internet_Service = "No"`. |
| *8 Internet Add-ons*\* | 1,390 each | Replaced with **`"No"`** | These customers had `Internet_Service = "No"`. Without base internet service, add-ons cannot exist. |
| `Churn_Category` | 4,686 | Replaced with **`"Not Applicable"`** | These customers had a `Customer_Status` of `"Stayed"` or `"Joined"`. |
| `Churn_Reason` | 4,686 | Replaced with **`"Not Applicable"`** | Same as above; only `"Churned"` customers have a churn reason. |

*\*The 8 Internet Add-on columns are: `Online_Security`, `Online_Backup`, `Device_Protection_Plan`, `Premium_Support`, `Streaming_TV`, `Streaming_Movies`, `Streaming_Music`, and `Unlimited_Data`.*

---

### Final Dataset Status
After applying these preprocessing steps, the dataset is **100% complete with 0 missing values**, localized for **Bangladesh**, and features realistic financial metrics in **BDT**.
