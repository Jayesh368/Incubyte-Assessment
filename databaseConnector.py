#!/usr/bin/env python


import cx_Oracle
import pandas as pd


con=cx_Oracle.connect('system/1234@127.0.0.1/XE')
if con!=None:
    print(con.version)
    print("connection done")
else:
    print("not done")
    


cur=con.cursor()
query='''select * from patients'''
cur.execute(query)



table_rows=cur.fetchall()
df=pd.read_sql('select * from patients', con=con)

print(df) 




df.set_index(['CUST_ID'], inplace=True)  

ans = df.loc[df['COUNTRY'] == "IND"]


def show_data(country):
    data = df.loc[df['COUNTRY'] == country]
    print(data)



def get_file(country):
    data = df.loc[df['COUNTRY'] == country]
    file_name = str(country)
    data.to_csv(country + ".csv")
    print("File has been created to the specified path")



show_data("AU")
get_file("AU")



show_data("USA")
get_file("USA")



show_data("PHIL")
get_file("PHIL")



show_data("NYC")
get_file("NYC")


show_data("IND")
get_file("IND")




