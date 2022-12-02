# for most parts
# instead of tests and/or unit tests basic  function calls 
# are commented out below the definitions

import mysql.connector
import WTcredentials
#import csv
from sql_tools import pair_actions as  st
import entering_data as ed

db = mysql.connector.connect(
    host = WTcredentials.host,
    user = WTcredentials.user,
    passwd = WTcredentials.passwd,
    database= WTcredentials.database)

mycursor = db.cursor()

#file to get data from
USER_CSV = "testADD_CHARACTERS.csv"
csv_read = st.read_csv(USER_CSV)

def proceed_actions(pair_actions):
    for line in pair_actions:
        if line['ACTION'] == 'ADD':
            ed.enter_character(line)

if __name__ == "__main__":
    proceed_actions(st.pair_actions(*csv_read))

  




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

#TEST --->WORKS fine
#sql_query = """
#INSERT INTO `storytool_test`.`character`
#(`first_name`, `family_name`, `nickname`, `principal`, `description`, `gender`, `skill`, `idea`, `saying`, `narrative`)
#VALUES ('Łukasz', 'Sikora', 'Szeryf', '1', 'tall, medium hair', '1', 'bjj', 'centrism', '', '');
#"""
#mycursor.execute(sql_query)
#db.commit()

#(`first_name`, `family_name`, `nickname`, `principal`, `description`, `gender`, `skill`, `idea`, `saying`, `narrative`)
#('first_name', 'family_name', 'nickname', 'principal', 'description', 'gender', 'skill', 'idea', 'saying', 'narrative')