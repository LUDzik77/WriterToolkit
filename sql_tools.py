import csv
from WTK_main import db, mycursor

#to verify the basic excel spreeedsheet have columns as per  database
def get_columns_names(table_name):
    sql_query  =  """
    SELECT COLUMN_NAME
    FROM `INFORMATION_SCHEMA`.`COLUMNS`
    WHERE `TABLE_SCHEMA` = (%s)
    AND `TABLE_NAME` = (%s)
    order by ORDINAL_POSITION;
    """
    sql_values = (db.database, table_name)
    mycursor.execute(sql_query, sql_values)
    return([a[0] for a in list(mycursor)])
#print(get_columns_names('character'))

def get_columns_names_without(table_name, *column_name):
    result = get_columns_names(table_name)
    for col in column_name:
        result.remove(col)
    return(result)
#print(get_columns_names_without('character', 'character_id'))

def list_to_str_with_escape_characters(given_list):
    result = str(tuple(given_list)).replace("'","`")
    #print(result)
    return(result)

def csv_format_check(csvfile):
    #print(csvfile[-3:].lower())
    if csvfile[-3:].lower() != 'csv': raise Exception("Please use CSV format file")
    else: print("Correct format of the file")
#csv_format_check(USER_CSV)    

def read_csv(csvfile):
    with open(csvfile, 'r', encoding='utf-8') as file:
        content = csv.reader(file)
        headings = next(content)
        output = []
        for row in content: output.append(row)
    return(headings, output)
#csv_read = read_csv(USER_CSV)
#print(lines_to_verify[0])
#print(*lines_to_verify[1])

def pair_actions(headings, lines):
    temp, result = list(), list()
    for line in lines: temp.append(zip(headings,line))
    for line in temp: result.append(dict(tuple(line))) 
    return(result)
#print(pair_actions(*csv_read))