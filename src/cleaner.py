def clean_records(records):
    cleaned_records = []
    for record in records:
        cleaned_record = {}
        for key, value in record.items():
            if value is None:
                cleaned_record[key] = ""
            elif isinstance(value, str):
                cleaned_record[key] = value.strip()
            else:
                cleaned_record[key] = value
            
        cleaned_records.append(cleaned_record)

    return cleaned_records 
