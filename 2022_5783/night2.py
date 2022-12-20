import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

# Load in all datasets 
customers = pd.read_csv('data/noahs-customers.csv')
orders_items = pd.read_csv('data/noahs-orders_items.csv')
orders = pd.read_csv('data/noahs-orders.csv')
products = pd.read_csv('data/noahs-products.csv')

# Search for products with basic keywords
print(products.loc[products['desc'].str.contains('coffee',False)])
print(products.loc[ products['desc'].str.contains('bagel',False)])
print(products.loc[ products['desc'].str.contains('clean',False)])
# DLI1464 | Coffee, Drip
# BKY4234 | Caraway Bagle
# BKY5887 | Sesame Bagel
# HOM8601 | Rug Cleaner

#Filter orders_items dataset to only orders that contain 1 of the above items
coffee_bagel_cleaner_order_items = orders_items.loc[orders_items['sku'].isin(['DLI1464','BKY4234','BKY5887','HOM8601'])]

#Group everything by order and place SKU quantity in each column
possible_orders = pd.pivot(coffee_bagel_cleaner_order_items,index='orderid',columns='sku',values='qty')

#Filter possible orders to those that bought coffee AND rug cleaner
possible_orders.loc[(possible_orders['DLI1464']>0) & possible_orders['HOM8601']>0] # Orderid = 7409

#Filter the customers dataset by the only order number returned above for the answer
customer_orders = orders.join(customers.set_index('customerid'),on='customerid')
print(customer_orders.loc[customer_orders['orderid']==7409]['phone'])



