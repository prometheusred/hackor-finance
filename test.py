import psycopg2 as pg
#import psycopg2.extras as pge
from psycopg2.extras import DictCursor

from pandas.io.sql import read_sql
#from pandas.io.sql import read_sql_table
import pandas as pd
import numpy as np

#matplotlib
conn = pg.connect("dbname=hackoregon user=jonathan.streater")
cur = conn.cursor()

def table_to_df(table, sort=False):
    if sort:
        table = sorted(table, key=lambda tup: tup[1])
    column_names = [name[0] for name in cur.description]
    labeled_table = map(lambda d: dict(zip(column_names, d)), table)
    return pd.DataFrame(labeled_table)

def get_table(table_name):
    query = "select * from " + table_name
    cur.execute(query)
    return cur.fetchall()


#cur.execute("select sum(amount), filer from  raw_committee_transactions where contributor_payee = 'Fulcrum Political, LLC' group by filer order by sum(amount) desc;")
#d = cur.execute("SELECT pg_size_pretty(pg_database_size('hackoregon'));")

#cur.execute("select * from pg_catalog.pg_tables"
cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
table_names = cur.fetchall()
table_names = map(lambda x: x[0], table_names)

#cur.execute("select * from ac_grass_roots_in_state")


se_transactions = table_to_df(get_table('working_transactions'), True)
se_candidate_committees = table_to_df(get_table('working_candidate_committees'))
se_candidate_filings = table_to_df(get_table('working_candidate_filings'))
se_working_committees = table_to_df(get_table('working_committees'))
#se_transactions = pd.Series(sorted_table)



#cur.execute("select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = '';")
#print cur.fetchall()




cur.close()
conn.close()


# write script to transfer given table to series DONE
# script to transfer tables to data frames (can also do series)

# research algorithms that are relevant

# explore data -- figure out what is where
#network analysis?
#influence of variables?
#adding rows for wins?  what can you predict?

# help jon with d3
