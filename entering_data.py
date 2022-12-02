from sql_tools  import get_columns_names_without, list_to_str_with_escape_characters

def enter_character(line_with_headings):
    sql_query = "INSERT INTO `storytool_test`.`character`"\
        +list_to_str_with_escape_characters(get_columns_names_without('character', 'character_id'))\
        + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_values = list()
    for heading in get_columns_names_without('character', 'character_id'):
        sql_values.append(line_with_headings[heading])
    mycursor.execute(sql_query, tuple(sql_values))
    db.commit()
    print(f"character added: {sql_values[0]} {sql_values[1]} {sql_values[2]}")
#enter_character({'ACTION': 'ADD', 'character_id': '', 'first_name': 'Łukasz', 'family_name': 'Sikora','nickname': 'Szeryf',\
#                 'principal': '1', 'description': 'tall, medium hair', 'gender': '1', 'skill': 'bjj', 'idea': 'centrism', 'saying': '', 'narrative': ''})
