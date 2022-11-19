import mysql.connector
from datetime import datetime
import WTcredentials
import csv

db = mysql.connector.connect(
    host = WTcredentials.host,
    user = WTcredentials.user,
    passwd = WTcredentials.passwd,
    database= WTcredentials.database)

mycursor = db.cursor()

#sql_query = "INSERT INTO mapping_to_type VALUES (%s)"
#sql_query = ("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS"
#"WHERE TABLE_SCHEMA=(%s) AND TABLE_NAME=(%s);")
#sql_values = ('storytool_test', 'character')
#mycursor.execute(sql_query, sql_values)


sql_query  =  """
SELECT COLUMN_NAME
FROM `INFORMATION_SCHEMA`.`COLUMNS`
WHERE `TABLE_SCHEMA` = 'storytool_test'
AND `TABLE_NAME` = 'character'
"""
mycursor.execute(sql_query)
for col in mycursor.fetchall():
    print(col)
#WORKS!!!!!!!!!!"



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
print(lines_to_verify[0])
print(*lines_to_verify[1])

"""
SELECT `COLUMN_NAME` 
FROM `INFORMATION_SCHEMA`.`COLUMNS` 
WHERE `TABLE_SCHEMA`='yourdatabasename' 
    AND `TABLE_NAME`='yourtablename';
"""
WTcredentials.database

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