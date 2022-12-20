import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

customers = pd.read_csv('data/noahs-customers.csv')

orders_items = pd.read_csv('data/noahs-orders_items.csv')

orders = pd.read_csv('data/noahs-orders.csv')

products = pd.read_csv('data/noahs-products.csv')
print(products.loc[products['desc'].str.contains('coffee',False)])
print(products.loc[ products['desc'].str.contains('bagel',False)])
print(products.loc[ products['desc'].str.contains('clean',False)])
# DLI1464 | Coffee, Drip
# BKY4234 | Caraway Bagle
# BKY5887 | Sesame Bagel
# HOM8601 | Rug Cleaner

coffee_bagel_cleaner_order_items = orders_items.loc[orders_items['sku'].isin(['DLI1464','BKY4234','BKY5887','HOM8601'])]
coffee_bagel_cleaner_order_items.head()

possible_orders = pd.pivot(coffee_bagel_cleaner_order_items,index='orderid',columns='sku',values='qty')

possible_orders.loc[(possible_orders['DLI1464']>0) & possible_orders['HOM8601']>0] # Orderid = 7409

customer_orders = orders.join(customers.set_index('customerid'),on='customerid')
customer_orders.loc[customer_orders['orderid']==7409]


