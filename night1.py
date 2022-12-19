import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

customers = pd.read_csv("./data/noahs-customers.csv")
customers[['first_name','last_name']]=customers['name'].str.split(' ', n= 1,expand=True)
customers['last_name_len']=customers['last_name'].str.len()
customers['phone_num']=customers['phone'].str.replace('-','')

t9 = {
    2:['A','B','C'],
    3:['D','E','F'],
    4:['G','H','I'],
    5:['J','K','L'],
    6:['M','N','O'],
    7:['P','Q','R','S'],
    8:['T','U','V'],
    9:['W','X','Y','Z']
}

q = """
    SELECT a.last_name,a.phone,a.customerid,phone_num
    FROM customers a
    Where last_name_len in (4,7,10)
"""
possible_matches=pysqldf(q)

pm_dict = possible_matches.to_dict('records')
comparrison_dict = {person['last_name']:[int(num) for num in person['phone_num'][-len(person['last_name']):]] for person in pm_dict}

subset = []
for name,phone_num in comparrison_dict.items():
    include_person = 1
    for index,digit in enumerate(phone_num):
        if name[index].upper() not in t9.get(digit,[]):
            include_person = 0
    if include_person == 1:
        subset.append({name:phone_num})

pi = list(subset[0].keys())[0]

q = f"SELECT a.last_name,a.phone,a.customerid,phone_num FROM customers a Where last_name = '{pi}'"

print(pysqldf(q)['phone'])



