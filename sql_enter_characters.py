# for most parts
# instead of tests and/or unit tests basic  function calls 
# are commented out below the definitions

import mysql.connector
import WTcredentials
from csv_tools import read_csv_tool

db = mysql.connector.connect(
    host = WTcredentials.host,
    user = WTcredentials.user,
    passwd = WTcredentials.passwd,
    database= WTcredentials.database)

mycursor = db.cursor()

#temp test paths
CHARACTERS_CSV = "testADD_CHARACTERS.csv"
SCENES_CSV = "testADD_CHARACTERS.csv"
CHAPTERS_CSV = "testADD_CHARACTERS.csv"
BOOKS_CSV = "testADD_CHARACTERS.csv"
          
ADD_OR_MODIFY_CHARACTERS = read_csv_tool(CHARACTERS_CSV)
ADD_OR_MODIFY_SCENES = read_csv_tool(SCENES_CSV)
ADD_OR_MODIFY_CHAPTERS  = read_csv_tool(CHAPTERS_CSV)
ADD_OR_MODIFY_BOOKS = read_csv_tool(BOOKS_CSV)

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
    return(result)

def pair_actions(headings, lines):
    temp, result = list(), list()
    for line in lines: temp.append(zip(headings,line))
    for line in temp: result.append(dict(tuple(line))) 
    return(result)
#print(pair_actions(*ADD_OR_MODIFY_CHARACTERS))

def enter_character(line_with_headings):
    sql_query = "INSERT INTO `storytool_test`.`character`"\
        +list_to_str_with_escape_characters(get_columns_names_without('character', 'character_id'))\
        + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_values = list()
    for heading in get_columns_names_without('character', 'character_id'):
        sql_values.append(line_with_headings[heading])
    mycursor.execute(sql_query, tuple(sql_values))
    db.commit()
#enter_character({'ACTION': 'ADD', 'character_id': '', 'first_name': 'Łukasz', 'family_name': 'Sikora','nickname': 'Szeryf',\
#                 'principal': '1', 'description': 'tall, medium hair', 'gender': '1', 'skill': 'bjj', 'idea': 'centrism', 'saying': '', 'narrative': ''})

####/TODO
####/TODO
####/TODO
####/TODO  --->#need to get change <proceed actions  and  filenames etc>
def enter_book(line_with_headings):
    sql_query = "INSERT INTO `storytool_test`.`book`"\
        +list_to_str_with_escape_characters(get_columns_names_without('book'))\
        + " VALUES (%s, %s, %s, %s)"
    sql_values = list()
    for heading in get_columns_names_without('book'):
        sql_values.append(line_with_headings[heading])
    print(sql_query)
    print(sql_values)
    mycursor.execute(sql_query, tuple(sql_values))
    db.commit()
enter_book({'ACTION': 'ADD', 'name': 'Dzieciaki', 'completed':'0', 'description':'sci-fi  novel', 'narrative':'' })


def proceed_actions(pair_actions):
    for line in pair_actions:
        if line['ACTION']== "ADD":
            enter_character(line)

            



if __name__ == "__main__": 
    proceed_actions(pair_actions(*ADD_OR_MODIFY_CHARACTERS))



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