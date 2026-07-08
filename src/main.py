import argparse
import logging
from loader import load_csv
from cleaner import clean_records
from analyzer import analyza_records
from writer import save_csv, save_json, save_text
from reporter import build_markdown_report
from logger_config import setup_logging

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
    setup_logging()
    logging.info("Loadaing dataset...")
    records = load_csv(args.input)
    logging.info(f"Loaded {len(records)} records")
    logging.info("Cleaning records...")
    cleaned_records = clean_records(records)
    logging.info("Analyzing dataset...")
    summary = analyza_records(cleaned_records)
    logging.info("Saving CSV...")
    save_csv(args.csv, cleaned_records)
    logging.info("Saving JSON...")
    save_json(args.json, cleaned_records)
    logging.info("Genarating report...")
    report = build_markdown_report(summary)   
    save_text(report, args.report)
    logging.info("Report saved")


    logging.info("Pipeline completed.")

if __name__ == "__main__":
    main()
