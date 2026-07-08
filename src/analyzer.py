def analyza_records(records):
    summary = {}
    if not records:
        summary = {
            "total_records": 0,
            "total_columns": 0,
            "columns": [],
            "missing_values": {}
        }
        return summary

    
    columns = records[0].keys()
    missing_values = {}
        
    for column in columns:
        count = 0

        for record in records:
            value = record.get(column)

            if value == "" or value is None:
                count +=1
            
            missing_values[column] = count
    
    summary = {
        "total_records": len(records),
        "total_columns": len(columns),
        "columns": columns,
        "missing_values": missing_values}
    
    return summary