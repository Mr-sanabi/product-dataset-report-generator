from loader import load_csv
from cleaner import clean_records

def main():
    input_path = "data/raw/amazon-products.csv"
    records = load_csv(input_path)
    cleaned_records = clean_records(records)
    print(len(cleaned_records))
    print(cleaned_records[1])

if __name__ == "__main__":
    main()
