import pandas as pd 
import os
import json
import jsonschema
import logging


#To Get the System Path
system_path = os.getcwd()
#print(system_path)

#To Get the Invoice Data
invoice_data = pd.read_csv('C:/Users/user/Desktop/real_streaming_data/dataset/sample.csv', encoding='cp1252')
#print(invoice_data.head())


df_groupby = invoice_data.groupby(['InvoiceNo','CustomerID','Country','InvoiceDate'])[['StockCode','Description','Quantity','UnitPrice']].apply(lambda x:x.to_dict(orient = 'records'))
df = pd.DataFrame(df_groupby).reset_index()
df.columns = ['InvoiceNo','CustomerID','Country','InvoiceDate','StockDetails']

#df = df.to_dict(orient='records')

#print(df)

# Print the Data to Json as a File	
df.to_json("C:/Users/user/Desktop/real_streaming_data/dataset/sample_invoice_data.json",orient="records",lines=True)