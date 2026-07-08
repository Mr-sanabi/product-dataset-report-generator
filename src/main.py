from loader import load_csv
from cleaner import clean_records
from analyzer import analyza_records
from writer import save_csv, save_json, save_text
from reporter import build_markdown_report

def main():
    input_path = "data/raw/amazon-products.csv"
    records = load_csv(input_path)
    cleaned_records = clean_records(records)
    summary = analyza_records(cleaned_records)
    save_csv("data/processed/cleaned_products.csv", cleaned_records)
    save_json("data/processed/products.json", cleaned_records)
    report = build_markdown_report(summary)   
    save_text(report, "reports/report.md")
    print("Saved outputs")


if __name__ == "__main__":
    main()
