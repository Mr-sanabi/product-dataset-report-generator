def build_markdown_report(summary):
    lines = []
    total_records = summary["total_records"]
    total_columns = summary["total_columns"]
    lines.append("# Product Dataset Report")
    lines.append("")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Total records: {total_records}")
    lines.append(f"- Total columns: {total_columns}")
    lines.append("")
    lines.append("")
    lines.append("## Columns")
    
    for column in summary["columns"]:
        lines.append(f"- {column}")
    
    lines.append("")
    lines.append("")
    lines.append("## Missing Values")
    
    for column, count in summary["missing_values"].items():
        lines.append(f"- {column}: {count}")

    return "\n".join(lines)