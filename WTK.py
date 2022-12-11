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
CHAPTERS_CSV = "ADD_CHAPTERS.csv"
BOOKS_CSV = "ADD_BOOKS.csv"
          
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

def execute_commit(sql_query, sql_values):
    mycursor.execute(sql_query, sql_values)
    db.commit()
    print(f"entered {sql_values}")
    
def enter_character(line_with_headings):
    sql_query = "INSERT INTO `storytool_test`.`character`"\
        +list_to_str_with_escape_characters(get_columns_names_without('character', 'character_id'))\
        + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_values = list()
    for heading in get_columns_names_without('character', 'character_id'):
        sql_values.append(line_with_headings[heading])
    execute_commit(sql_query, tuple(sql_values))
#enter_character({'ACTION': 'ADD', 'character_id': '', 'first_name': 'Łukasz', 'family_name': 'Sikora','nickname': 'Szeryf',\
#                 'principal': '1', 'description': 'tall, medium hair', 'gender': '1', 'skill': 'bjj', 'idea': 'centrism', 'saying': '', 'narrative': ''})

def enter_book(line_with_headings):
    sql_query = "INSERT INTO `storytool_test`.`book`"\
        +list_to_str_with_escape_characters(get_columns_names_without('book'))\
        + " VALUES (%s, %s, %s, %s)"
    sql_values = list()
    for heading in get_columns_names_without('book'):
        sql_values.append(line_with_headings[heading])
    execute_commit(sql_query, tuple(sql_values))
#enter_book({'ACTION': 'ADD', 'name': 'Dzieciaki', 'completed':'0', 'description':'sci-fi  novel', 'narrative':'' })

def enter_chapter(line_with_headings):
    sql_query = "INSERT INTO `storytool_test`.`chapter`"\
        +list_to_str_with_escape_characters(get_columns_names_without('chapter'))\
        + " VALUES (%s, %s, %s, %s, %s, %s, %s)"
    sql_values = list()
    for heading in get_columns_names_without('chapter'):
        sql_values.append(line_with_headings[heading])
    execute_commit(sql_query, tuple(sql_values))

def map_and_execute(file, func_add, func_modify):
    for line in pair_actions(*file):
        if line['ACTION'] in ("ADD", "add", "a", "A", "+"): func_add(line)
        elif line['ACTION'] in ("MODIFY", "modify", "m", "M"): func_modify(line) 
        else: print("Only ADD or MODIFY as action are allowed")   

def truncate_table(table_name_with_escape_symbols):
    mycursor.execute(f"TRUNCATE `storytool_test`.{table_name_with_escape_symbols};")
    print(f"{table_name_with_escape_symbols} db was truncated ") 

def characters():
    map_and_execute(ADD_OR_MODIFY_CHARACTERS, enter_character, enter_character)     
    truncate_table("`character`")

def scenes():
    map_and_execute(ADD_OR_MODIFY_SCENES, enter_scene, enter_scene)
    truncate_table("`scene`")

def chapters():
    map_and_execute(ADD_OR_MODIFY_CHAPTERS, enter_chapter, enter_chapter)
    truncate_table("`chapter`")

def books():
    map_and_execute(ADD_OR_MODIFY_BOOKS, enter_book, enter_book)
    truncate_table("`book`")

