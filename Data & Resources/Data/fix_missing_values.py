"""
fix_missing_values.py
---------------------
Fills all missing/blank values in Customer_Data.csv with appropriate values.

Missing Value Strategy:
-----------------------
1. Value_Deal (3,548 blank) -> "No Deal" (customer has no promotional deal)
2. Multiple_Lines (622 blank, all Phone_Service=No) -> "No" (no phone = no multiple lines)
3. Internet_Type (1,390 blank, all Internet_Service=No) -> "None" (no internet service)
4. Online_Security, Online_Backup, Device_Protection_Plan, Premium_Support,
   Streaming_TV, Streaming_Movies, Streaming_Music, Unlimited_Data
   (1,390 blank each, all Internet_Service=No) -> "No" (no internet = no add-ons)
5. Churn_Category (4,686 blank, all non-Churned) -> "Not Applicable"
6. Churn_Reason (4,686 blank, all non-Churned) -> "Not Applicable"
"""

import csv

input_file = "Customer_Data.csv"
output_file = "Customer_Data_NoMissing.csv"

# Track counts for each fix
fix_counts = {
    "Value_Deal": 0,
    "Multiple_Lines": 0,
    "Internet_Type": 0,
    "Internet_Addons": 0,
    "Churn_Category": 0,
    "Churn_Reason": 0,
}

# Internet add-on columns (all blank when Internet_Service=No)
INTERNET_ADDON_COLS = [
    "Online_Security", "Online_Backup", "Device_Protection_Plan",
    "Premium_Support", "Streaming_TV", "Streaming_Movies",
    "Streaming_Music", "Unlimited_Data"
]

with open(input_file, "r", encoding="utf-8-sig") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:

        # 1. Value_Deal: blank -> "No Deal"
        if row["Value_Deal"].strip() == "":
            row["Value_Deal"] = "No Deal"
            fix_counts["Value_Deal"] += 1

        # 2. Multiple_Lines: blank (Phone_Service=No) -> "No"
        if row["Multiple_Lines"].strip() == "":
            row["Multiple_Lines"] = "No"
            fix_counts["Multiple_Lines"] += 1

        # 3. Internet_Type: blank (Internet_Service=No) -> "None"
        if row["Internet_Type"].strip() == "":
            row["Internet_Type"] = "None"
            fix_counts["Internet_Type"] += 1

        # 4. Internet add-on columns: blank (Internet_Service=No) -> "No"
        for col in INTERNET_ADDON_COLS:
            if row[col].strip() == "":
                row[col] = "No"
                fix_counts["Internet_Addons"] += 1

        # 5. Churn_Category: blank (non-Churned) -> "Not Applicable"
        if row["Churn_Category"].strip() == "":
            row["Churn_Category"] = "Not Applicable"
            fix_counts["Churn_Category"] += 1

        # 6. Churn_Reason: blank (non-Churned) -> "Not Applicable"
        if row["Churn_Reason"].strip() == "":
            row["Churn_Reason"] = "Not Applicable"
            fix_counts["Churn_Reason"] += 1

        writer.writerow(row)

# Print summary
print("=== Missing Values Fixed ===\n")
print(f"  Value_Deal:      {fix_counts['Value_Deal']:,} blanks -> 'No Deal'")
print(f"  Multiple_Lines:  {fix_counts['Multiple_Lines']:,} blanks -> 'No'")
print(f"  Internet_Type:   {fix_counts['Internet_Type']:,} blanks -> 'None'")
print(f"  Internet Addons: {fix_counts['Internet_Addons']:,} blanks -> 'No' (8 columns x {fix_counts['Internet_Type']:,} rows)")
print(f"  Churn_Category:  {fix_counts['Churn_Category']:,} blanks -> 'Not Applicable'")
print(f"  Churn_Reason:    {fix_counts['Churn_Reason']:,} blanks -> 'Not Applicable'")
total = sum(fix_counts.values())
print(f"\n  Total cells fixed: {total:,}")
print(f"\nOutput saved to: {output_file}")

# Verify no remaining blanks
print("\n=== Verification ===")
data = list(csv.DictReader(open(output_file, "r", encoding="utf-8-sig")))
remaining_blanks = 0
for col in data[0].keys():
    blanks = sum(1 for r in data if r[col].strip() == "")
    if blanks > 0:
        print(f"  WARNING: {col} still has {blanks} blanks!")
        remaining_blanks += blanks

if remaining_blanks == 0:
    print("  All columns have ZERO missing values. Dataset is complete!")
