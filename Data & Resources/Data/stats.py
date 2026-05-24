import csv

with open('Customer_Data.csv', 'r', encoding='utf-8-sig') as f:
    reader = list(csv.DictReader(f))
    
    ages = sorted([int(r['Age']) for r in reader if r.get('Age')])
    tenures = sorted([int(r['Tenure_in_Months']) for r in reader if r.get('Tenure_in_Months')])
    
    def print_stats(name, data):
        if not data: return
        n = len(data)
        print(f"{name} Stats:")
        print(f"  Min: {min(data)}")
        print(f"  25th: {data[n//4]}")
        print(f"  Median: {data[n//2]}")
        print(f"  75th: {data[(3*n)//4]}")
        print(f"  Max: {max(data)}")
        print()

    print_stats("Age", ages)
    print_stats("Tenure_in_Months", tenures)
