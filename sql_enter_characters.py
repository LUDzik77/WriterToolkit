# for most parts
# instead of tests and/or unit tests basic  function calls 
# are commented out below the definitions

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

def read_csv(csvfile):
    with open(csvfile, 'r', encoding='utf-8') as file:
        content = csv.reader(file)
        headings = next(content)
        output = []
        for row in content: output.append(row)
    return(headings, output)
csv_read = read_csv("testADD_CHARACTERS.csv")
#print(lines_to_verify[0])
#print(*lines_to_verify[1])

def pair_actions(headings, lines):
    temp, result = list(), list()
    for line in lines: temp.append(zip(headings,line))
    for line in temp: result.append(dict(tuple(line))) 
    return(result)
print(pair_actions(*csv_read))
#[print(*pair) for pair in pair_actions(*csv_read)]

#def proceed_actions(pair_actions):
    # 



#def enter_characters(csvfile):
    #sql_query = """
    #INSERT INTO `storytool_test`.`character`
    #(
    #`first_name`,
    #`family_name`,
    #`nickname`,
    #`principal`,
    #`description`,
    #`gender`,
    #`skill`,
    #`idea`,
    #`saying`,
    #`narrative`)
    #VALUES ('Ludwik', 'Papaj', 'LUDzik', 1, '', 1, 'coding', 'capitalist', 'Allright', '');
    #"""
    #mycursor.execute(sql_query)
    #db.commit()





#sql_query = """
#INSERT INTO `storytool_test`.`character`
#(`character_id`,
#`first_name`,
#`family_name`,
#`nickname`,
#`principal`,
#`description`,
#`gender`,
#`skill`,
#`idea`,
#`saying`,
#`narrative`)
#VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
#"""
#sql_values = lines_to_verify[1][0]
#print(lines_to_verify[1][0][1:])
#mycursor.execute(sql_query, sql_values)
#db.commit()


#TEST --->WORKS fine
#sql_query = """
#INSERT INTO `storytool_test`.`character`
#(
#`first_name`,
#`family_name`,
#`nickname`,
#`principal`,
#`description`,
#`gender`,
#`skill`,
#`idea`,
#`saying`,
#`narrative`)
#VALUES ('Ludwik', 'Papaj', 'LUDzik', 1, '', 1, 'coding', 'capitalist', 'Allright', '');
#"""
#mycursor.execute(sql_query)
#db.commit()



