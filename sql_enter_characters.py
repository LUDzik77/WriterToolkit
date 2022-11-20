import mysql.connector
import WTcredentials
import csv
#from functools import reduce

db = mysql.connector.connect(
    host = WTcredentials.host,
    user = WTcredentials.user,
    passwd = WTcredentials.passwd,
    database= WTcredentials.database)

mycursor = db.cursor()

#to verify the basic excel spreeedsheet have columns as per  database
def get_columns_names(table_name):
    sql_query  =  """
    SELECT COLUMN_NAME
    FROM `INFORMATION_SCHEMA`.`COLUMNS`
    WHERE `TABLE_SCHEMA` = (%s)
    AND `TABLE_NAME` = (%s)
    """
    sql_values = (db.database, table_name)
    mycursor.execute(sql_query, sql_values)
    return([a[0] for a in list(mycursor)])
#print(get_columns_names('character'))

def csv_format_check(csvfile):
    print(csvfile[-3:].lower())
    if csvfile[-3:].lower() != 'csv': raise Exception("Please use CSV format file")
    else: print("Correct format of the file")
#csv_format_check("testADD_CHARACTERS.csv")    

def enter_characters(csvfile):
    pass

def read_csv(csvfile):
    with open(csvfile, 'r', encoding='utf-8') as file:
        content = csv.reader(file)
        headings = next(content)
        output = []
        for row in content:
            output.append(row)
    return(headings, output)

lines_to_verify = read_csv("testADD_CHARACTERS.csv")
#print(lines_to_verify[0])
#print(*lines_to_verify[1])

"""
SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='yourdatabasename' 
    AND `TABLE_NAME`='yourtablename';
"""


'''
INSERT INTO `storytool_test`.`character`
(`character_id`,
`first_name`,
`family_name`,
`nickname`,
`principal`,
`narrative`,
`description`,
`saying`,
`gender`)
VALUES
(<{character_id: }>,
<{first_name: NOT NULL}>,
<{family_name: }>,
<{nickname: }>,
<{pricipal: 0}>,
<{narrative: }>,
<{description: }>,
<{saying: }>,
<{gender: 0}>);
'''