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

def create_adjacencies(table):
    adjacencies = {}
    count = 0

    for row in table:

        count += 1

        filer = row[2]
        payee = row[3]
        amount = row[5]
        direction = row[17]

        if filer is None or payee is None:
            continue

        if direction == 'out':
            giver = filer
            receiver = payee
        elif direction == 'in':
            giver = payee
            receiver = filer

        '''
        print count
        print row
        print giver
        print receiver
        print amount
        print direction
        '''

        if giver in adjacencies:
            #{receiver: {weight:x}, receiver: {weight:x}}
            if receiver in adjacencies[giver]:
                old_amount = adjacencies.get(giver).get(receiver).get('weight')
                new_amount = old_amount + amount
                adjacencies[giver][receiver] = {'weight': new_amount}
            else:
                adjacencies[giver][receiver] = {'weight': amount}
        else:
            adjacencies[giver] =  {receiver: {'weight': amount}}

    return adjacencies

table = get_table('working_transactions')
#se_transactions = table_to_df(table)

#se_candidate_committees = table_to_df(get_table('working_candidate_committees'))
#se_candidate_filings = table_to_df(get_table('working_candidate_filings'))
#se_working_committees = table_to_df(get_table('working_committees'))


adj = create_adjacencies(table)
G = nx.MultiDiGraph(adj, multigraph_input=True)

'''
for node in G.iter_nodes():
    outties =
'''

cur.close()
conn.close()





#a node is a comm
#edges are directed transaction sums

#we have transaction time-series: from, to, in/out, amount
#build nodes by:








#make a graph of transactions with networkx 1
#visualize with d3 or mayavi
#investigate network flows and network flows over time, perhaps month to month or week to week

#for transactions -- use pandas to groupby and orderby week
#good questions:
#which comm has most out
#which comm has most in
#which comm has biggeest diff between in and out
#which comm has smallest diff between in and out






# research algorithms that are relevant

# explore data -- figure out what is where
#network analysis?
#influence of variables?
#adding rows for wins?  what can you predict?

# help jon with d3
