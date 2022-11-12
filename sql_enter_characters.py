import mysql.connector
from datetime import datetime
import WTcredentials

db = mysql.connector.connect(
    host = WTcredentials.host,
    user = WTcredentials.user,
    passwd = WTcredentials.passwd,
    database= WTcredentials.database)

mycursor = db.cursor()

sql_query = "INSERT INTO mapping_to_type VALUES (%s, %s)"
sql_values = [
    (0, 'NULL'),

]

mycursor.execute(sql_query, sql_values)
db.commit()

print(mycursor.rowcount, "was inserted.")



def enter_characters(csvfile):
    pass

def map_csv(csvfile):
    pass

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