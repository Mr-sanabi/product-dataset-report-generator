import csv
import json

def save_csv(filename, rows):
    if not rows:
        return
    
    fields = rows[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def save_json(filename, rows):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(rows, file, indent=4, ensure_ascii=False)

def save_text(text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)    