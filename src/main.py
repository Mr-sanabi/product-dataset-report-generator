from loader import load_csv
from cleaner import clean_records
from analyzer import analyza_records

def main():
    input_path = "data/raw/amazon-products.csv"
    records = load_csv(input_path)
    cleaned_records = clean_records(records)
    summary = analyza_records(cleaned_records)
    print(summary)

if __name__ == "__main__":
    main()
