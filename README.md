# Product Dataset Report Generator

Python CLI tool for cleaning e-commerce product CSV datasets and generating structured CSV, JSON, and Markdown outputs.

## Features

- Loads raw e-commerce product CSV files
- Cleans empty and whitespace-heavy values
- Handles large CSV fields
- Analyzes dataset structure
- Counts total records and columns
- Detects missing values per column
- Exports cleaned CSV files
- Exports JSON files
- Generates a Markdown data quality report
- Provides CLI arguments for input and output paths
- Shows pipeline progress with logging

## Tech Stack

- Python
- CSV
- JSON
- argparse
- logging
- pathlib

## Project Structure

    product-dataset-report-generator/
      src/
        main.py
        loader.py
        cleaner.py
        analyzer.py
        writer.py
        reporter.py
        logger_config.py

      data/
        raw/
          amazon-products.csv
        processed/
          cleaned_products.csv
          products.json

      reports/
        report.md

      README.md
      requirements.txt
      .gitignore

## Usage

Run the pipeline from the project root:

    python src/main.py --input data/raw/amazon-products.csv --csv data/processed/cleaned_products.csv --json data/processed/products.json --report reports/report.md

## Output

The pipeline generates:

    data/processed/cleaned_products.csv
    data/processed/products.json
    reports/report.md

## Report Contents

The Markdown report includes:

- Total number of records
- Total number of columns
- Dataset column list
- Missing value count for each column

Example report sections:

    # Product Dataset Report

    ## Summary
    - Total records: 1000
    - Total columns: 55

    ## Columns
    - timestamp
    - title
    - seller_name
    - brand
    - description

    ## Missing Values
    - timestamp: 0
    - title: 0
    - seller_name: 174
    - brand: 1

## Dataset

Sample e-commerce dataset from:

    luminati-io/eCommerce-dataset-samples

This project currently uses:

    amazon-products.csv

## Purpose

This project demonstrates a clean data-processing pipeline for raw product datasets:

    raw CSV
    → load records
    → clean values
    → analyze dataset quality
    → export cleaned CSV
    → export JSON
    → generate Markdown report

It is designed as a portfolio project for data extraction, data cleaning, reporting, and automation workflows.

## Status

Portfolio-ready v1.