import csv

def load_csv(file_path):
    records = []
    with open(file_path, "r", encoding="utf-8") as file:
        csv.field_size_limit(10_000_000)
        rows = csv.DictReader(file)
        for row in rows:
            records.append(row)
        
        return records
    