import argparse
from loader import load_csv
from cleaner import clean_records
from analyzer import analyza_records
from writer import save_csv, save_json, save_text
from reporter import build_markdown_report

def parse_args():

    parser = argparse.ArgumentParser(
        description="description"
    )
    parser.add_argument("--input")
    parser.add_argument("--csv")
    parser.add_argument("--json")
    parser.add_argument("--report")
    return parser.parse_args()

def main():
    args = parse_args()
    records = load_csv(args.input)
    cleaned_records = clean_records(records)
    summary = analyza_records(cleaned_records)
    save_csv(args.csv, cleaned_records)
    save_json(args.json, cleaned_records)
    report = build_markdown_report(summary)   
    save_text(report, args.report)
    print("Saved outputs")


if __name__ == "__main__":
    main()
