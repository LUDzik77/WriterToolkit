import  csv

def read_csv_tool(csvfile):
    with open(csvfile, 'r', encoding='utf-8') as file:
        content = csv.reader(file)
        headings = next(content)
        output = []
        for row in content: output.append(row)
    return(headings, output)


def csv_format_check(csvfile):
    if csvfile[-3:].lower() != 'csv': raise Exception("Please use CSV format file")
    else: print("Correct format of the file")   