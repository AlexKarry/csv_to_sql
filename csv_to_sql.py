import sqlite3
import csv

db_filename = '../session_2.db'

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

drop_table_query = "DROP TABLE IF EXISTS weather_newyork"
cursor.execute(drop_table_query)

create_table_query = "CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)"
cursor.execute(create_table_query)

insert_query = 'INSERT INTO weather_newyork (date, mean_temp, precip, events) VALUES (?, ?, ?, ?)'

csv_filename = '../weather_newyork.csv'

wfh = open(csv_filename, 'r')
reader = csv.reader(wfh)
header = next(reader)

for row in reader:
    date = row[0]
    mean_temp = row[1]
    precip = row[17]
    events = row[19]
    if precip == 'T':
        precip = None
    else:
        precip = float(precip)
    cursor.execute(insert_query, (date, int(mean_temp), precip, events))

cursor.execute('SELECT COUNT(*) FROM weather_newyork')
row_count = cursor.fetchone()[0]
print("Number of row in weather_newyork table:", row_count)

conn.commit()
wfh.close() 
conn.close()

