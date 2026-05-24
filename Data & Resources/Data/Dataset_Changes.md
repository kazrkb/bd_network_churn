# Dataset Changes: India → Bangladesh

This document describes the differences between the **original India dataset** and the **new Bangladesh dataset**.

---

## Summary of Changes

| Aspect               | Original (India)                    | New (Bangladesh)                        |
|----------------------|-------------------------------------|-----------------------------------------|
| **Country**          | India                               | Bangladesh                              |
| **Geographic Units** | 22 Indian States/UTs                | 8 Bangladesh Administrative Divisions   |
| **Column `State`**   | Indian state names                  | Bangladesh division names               |
| **Column `Customer_ID`** | Suffix = Indian state abbreviation (e.g., `DEL`, `MAH`) | Suffix = Bangladesh division abbreviation (e.g., `DHK`, `CTG`) |
| **`Internet_Type`**  | `Fiber Optic`, `Cable`, `DSL`       | `Fiber Optic`, `Mobile Broadband`, `None` |
| **`Payment_Method`** | `Credit Card`, `Bank Withdrawal`, `Mailed Check` | `Credit Card`, `Bank Withdrawal`, `Mobile Banking (bKash/Nagad)` |
| **Currency**         | Generic / unspecified               | **Bangladeshi Taka (BDT)** (×7.5 multiplier applied) |
| **Missing Values**   | 26,052 blank cells across 13 columns | **0 missing values** (all filled)       |
| **Total Records**    | 6,418                               | 6,418 (unchanged)                       |
| **Total Columns**    | 32                                  | 32 (unchanged)                          |

---

## What Changed

### 1. `State` Column

The `State` column previously contained **22 Indian states and union territories**. It now contains **8 Bangladesh divisions**.

#### Mapping Used

| Indian State(s)                              | → Bangladesh Division | ID Suffix |
|----------------------------------------------|----------------------|-----------|
| Uttar Pradesh, Maharashtra, Delhi            | **Dhaka**            | DHK       |
| Bihar, West Bengal, Jharkhand                | **Chattogram**       | CTG       |
| Tamil Nadu, Karnataka, Puducherry            | **Khulna**           | KHU       |
| Kerala, Andhra Pradesh, Telangana            | **Rajshahi**         | RAJ       |
| Gujarat, Rajasthan, Uttarakhand              | **Rangpur**          | RAN       |
| Madhya Pradesh, Chhattisgarh, Jammu & Kashmir| **Sylhet**           | SYL       |
| Punjab, Haryana                              | **Barishal**         | BAR       |
| Assam, Odisha                                | **Mymensingh**       | MYM       |

#### Record Distribution Comparison

| Original (India)     | Count | → | New (Bangladesh) | Count |
|----------------------|-------|---|------------------|-------|
| Uttar Pradesh        | 540   |   | **Dhaka**        | 1,260 |
| Maharashtra          | 575   |   |                  |       |
| Delhi                | 145   |   |                  |       |
| Bihar                | 280   |   | **Chattogram**   | 817   |
| West Bengal          | 360   |   |                  |       |
| Jharkhand            | 177   |   |                  |       |
| Tamil Nadu           | 465   |   | **Khulna**       | 1,111 |
| Karnataka            | 485   |   |                  |       |
| Puducherry           | 161   |   |                  |       |
| Kerala               | 310   |   | **Rajshahi**     | 876   |
| Andhra Pradesh       | 350   |   |                  |       |
| Telangana            | 216   |   |                  |       |
| Gujarat              | 370   |   | **Rangpur**      | 656   |
| Rajasthan            | 235   |   |                  |       |
| Uttarakhand          | 51    |   |                  |       |
| Madhya Pradesh       | 275   |   | **Sylhet**       | 667   |
| Chhattisgarh         | 145   |   |                  |       |
| Jammu & Kashmir      | 247   |   |                  |       |
| Punjab               | 365   |   | **Barishal**     | 740   |
| Haryana              | 375   |   |                  |       |
| Assam                | 165   |   | **Mymensingh**   | 291   |
| Odisha               | 126   |   |                  |       |

### 2. `Customer_ID` Column

The suffix after the hyphen was updated to reflect the new Bangladesh division abbreviation.

**Examples:**

| Original ID     | New ID        | Change Reason                   |
|-----------------|---------------|---------------------------------|
| `19877-DEL`     | `19877-DHK`   | Delhi → Dhaka                   |
| `58353-MAH`     | `58353-DHK`   | Maharashtra → Dhaka             |
| `25063-WES`     | `25063-CTG`   | West Bengal → Chattogram        |
| `59787-KAR`     | `59787-KHU`   | Karnataka → Khulna              |
| `28544-TAM`     | `28544-KHU`   | Tamil Nadu → Khulna             |
| `73588-KER`     | `73588-RAJ`   | Kerala → Rajshahi               |
| `65618-GUJ`     | `65618-RAN`   | Gujarat → Rangpur               |
| `88912-MAD`     | `88912-SYL`   | Madhya Pradesh → Sylhet         |
| `46640-PUN`     | `46640-BAR`   | Punjab → Barishal               |
| `46172-ASS`     | `46172-MYM`   | Assam → Mymensingh              |

> **Note:** The numeric portion of each Customer_ID remains unchanged.

### 3. `Internet_Type` Column

Bangladesh's internet infrastructure is dominated by **Fiber Optic (FTTH)** and **Mobile Broadband (4G/5G)**. DSL and Cable are largely obsolete in Bangladesh.

| Original Value | → New Value | Rows Affected | Reason |
|---------------|------------|---------------|--------|
| `DSL` | `Fiber Optic` | 1,502 | DSL is obsolete in BD; most ISPs use fiber |
| `Cable` | `Mobile Broadband` | 762 | Cable internet is rare in BD; mobile broadband is the alternative |
| `Fiber Optic` | `Fiber Optic` | 2,764 | No change needed |

**Final distribution:** Fiber Optic (4,266) · Mobile Broadband (762) · blank/no internet (1,390)

### 4. `Payment_Method` Column

Bangladesh's payment landscape is dominated by **mobile financial services** (bKash, Nagad). Mailed checks are virtually non-existent.

| Original Value | → New Value | Rows Affected | Reason |
|---------------|------------|---------------|--------|
| `Mailed Check` | `Mobile Banking (bKash/Nagad)` | 349 | bKash/Nagad are BD's dominant payment platforms |
| `Credit Card` | `Credit Card` | 2,494 | No change needed |
| `Bank Withdrawal` | `Bank Withdrawal` | 3,575 | No change needed |

### 5. Financial Columns (Currency Conversion to BDT)

All 6 monetary columns were multiplied by **×7.5** to convert from generic units to realistic **Bangladeshi Taka (BDT)** values.

| Column | Original Avg | → New Avg (BDT) | Original Range | → New Range (BDT) |
|--------|------------|-----------------|---------------|-------------------|
| `Monthly_Charge` | 63.65 | **477.40** | -10 to 118.75 | -75 to 890.62 |
| `Total_Charges` | 2,280 | **17,103** | 18.8 to 8,685 | 141 to 65,136 |
| `Total_Refunds` | 1.92 | **14.44** | 0 to 49.79 | 0 to 373.43 |
| `Total_Extra_Data_Charges` | 6.72 | **50.39** | 0 to 150 | 0 to 1,125 |
| `Total_Long_Distance_Charges` | 748.70 | **5,615** | 0 to 3,565 | 0 to 26,735 |
| `Total_Revenue` | 3,034 | **22,754** | 21.36 to 11,979 | 160.2 to 89,845 |

**Validation against real BD market:**
- Avg monthly charge of **~477 BDT** aligns with typical BD telecom plans (350–800 BDT/month)
- Grameenphone ARPU is ~148 BDT for basic mobile, but bundled services (internet + streaming + phone) justify higher values

### 6. Missing Values (All Filled)

The original dataset contained **26,052 blank cells** across 13 columns. All have been filled with contextually appropriate values.

| Column(s) | Blank Count | Fill Value | Rationale |
|-----------|-------------|------------|----------|
| `Value_Deal` | 3,548 | `"No Deal"` | Customer has no active promotional deal |
| `Multiple_Lines` | 622 | `"No"` | All 622 had `Phone_Service=No` — no phone means no multiple lines |
| `Internet_Type` | 1,390 | `"None"` | All 1,390 had `Internet_Service=No` — no internet service |
| `Online_Security` | 1,390 | `"No"` | No internet = no add-on services |
| `Online_Backup` | 1,390 | `"No"` | No internet = no add-on services |
| `Device_Protection_Plan` | 1,390 | `"No"` | No internet = no add-on services |
| `Premium_Support` | 1,390 | `"No"` | No internet = no add-on services |
| `Streaming_TV` | 1,390 | `"No"` | No internet = no streaming |
| `Streaming_Movies` | 1,390 | `"No"` | No internet = no streaming |
| `Streaming_Music` | 1,390 | `"No"` | No internet = no streaming |
| `Unlimited_Data` | 1,390 | `"No"` | No internet = no data plan |
| `Churn_Category` | 4,686 | `"Not Applicable"` | All 4,686 are non-churned (Stayed/Joined) |
| `Churn_Reason` | 4,686 | `"Not Applicable"` | All 4,686 are non-churned (Stayed/Joined) |
| **Total** | **26,052** | | |

---

## What Did NOT Change

The following **18 columns** had their values completely unchanged:

| Category             | Unchanged Columns                                                                                                     |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Demographics**     | `Gender`, `Age`, `Married`, `Number_of_Referrals`, `Tenure_in_Months`                                                |
| **Service Plans**    | `Phone_Service`, `Internet_Service`, `Contract`                                                                       |
| **Billing**          | `Paperless_Billing`                                                                                                   |
| **Churn**            | `Customer_Status`                                                                                                     |

### Key Stats (Unchanged)

| Metric                  | Value          |
|-------------------------|----------------|
| Total Records           | 6,418          |
| Stayed                  | 4,275 (66.6%)  |
| Churned                 | 1,732 (27.0%)  |
| Joined                  | 411 (6.4%)     |
| Male / Female           | 2,370 / 4,048  |
| Age Range               | 18 – 85        |
| Month-to-Month Contracts| 3,286          |
| One Year Contracts      | 1,413          |
| Two Year Contracts      | 1,719          |

---

## Why These Changes Were Made

The original dataset was designed for the **Indian telecom market** with Indian state-level geography. To adapt it for **Bangladesh-based analysis**, the following changes were made:

- **22 Indian states** were consolidated into **8 Bangladesh divisions** (the top-level administrative units of Bangladesh)
- **Customer ID suffixes** were updated to maintain consistency between the ID format and the geographic field
- **Internet types** were updated to reflect Bangladesh's infrastructure (Fiber Optic + Mobile Broadband instead of DSL/Cable)
- **Payment methods** were updated to include Bangladesh's dominant mobile banking platforms (bKash/Nagad)
- **Financial values** were converted to **BDT** using a ×7.5 multiplier to match realistic Bangladesh telecom pricing
- **26,052 missing values** were filled with contextually appropriate defaults (e.g., `"No Deal"`, `"None"`, `"No"`, `"Not Applicable"`)
- **All other data was preserved** to maintain the statistical properties, distributions, and relationships in the dataset
