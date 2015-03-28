import psycopg2 as pg
from psycopg2.extras import DictCursor
from pandas.io.sql import read_sql
import pandas as pd
import numpy as np
import networkx as nx


conn = pg.connect("dbname=hackoregon user=jonathan.streater")
cur = conn.cursor()

###
#useful functions
###

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

def get_tablenames():
    cur.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
    table_names = cur.fetchall()
    return map(lambda x: x[0], table_names)

table = get_table('working_transactions')
se_transactions = table_to_df(table)
#se_candidate_committees = table_to_df(get_table('working_candidate_committees'))
#se_candidate_filings = table_to_df(get_table('working_candidate_filings'))
#se_working_committees = table_to_df(get_table('working_committees'))





G = nx.Graph()













cur.close()
conn.close()













#make a graph of transactions with networkx

#for transactions -- use pandas to groupby and orderby week

#visualize with d3 or mayavi

#investigate network flows and network flows over time, perhaps month to month or week to week





# research algorithms that are relevant

# explore data -- figure out what is where
#network analysis?
#influence of variables?
#adding rows for wins?  what can you predict?

# help jon with d3
