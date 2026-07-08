from loader import load_csv

def main():
    input_path = "data/raw/amazon-products.csv"
    records = load_csv(input_path)
    print(len(records))
    print(records[1])

if __name__ == "__main__":
    main()
