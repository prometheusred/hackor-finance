import psycopg2 as pg
import pandas.io.sql as psql
from pandas.io.sql import read_sql
#from pandas.io.sql import read_sql_table
import pandas as pd
import numpy as np

#matplotlib


conn = pg.connect("dbname=hackoregon user=jonathan.streater")
cur = conn.cursor()

#cur.execute("select sum(amount), filer from  raw_committee_transactions where contributor_payee = 'Fulcrum Political, LLC' group by filer order by sum(amount) desc;")
#d = cur.execute("SELECT pg_size_pretty(pg_database_size('hackoregon'));")


cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")

#cur.execute("select * from pg_catalog.pg_tables"

table_names = cur.fetchall()
table_names = map(lambda x: x[0], table_names)

#cur.execute("select * from ac_grass_roots_in_state")
root_query = "select * from "

###df = read_sql(())

#df = read_sql(('select "*" from "ac_grass_roots_in_state" '), cur)
                     #'where "Timestamp" BETWEEN %(dstart)s AND %(dfinish)s'),
df = pd.read_sql("SELECT * from raw_committee_transactions", cur)

#df = read_sql_table(cur,cur)

#cur.execute("select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = '';")
#print cur.fetchall()



cur.close()
conn.close()


# put a table into dataframe

# find out data schema of all tables

# put all tables into dataframes
