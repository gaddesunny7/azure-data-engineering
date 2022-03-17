
import pandas as pd
import json


#Read the File
moddata = pd.read_csv('sample.csv', encoding='cp1252')

finalList = []
finalDict = {}

#Group by the data using customerid,country,invoicedate,invoiceno
grouped = moddata.groupby(['CustomerID','Country','InvoiceDate','InvoiceNo'])


for key, value in grouped:
    
    dictionary = {}
    j = grouped.get_group(key).reset_index(drop=True)
    dictionary['CustomerID'] = j.at[0, 'CustomerID']
    dictionary['Country'] = j.at[0, 'Country']
    dictionary['InvoiceDate'] = j.at[0, 'InvoiceDate']
    dictionary['InvoiceNo'] = j.at[0, 'InvoiceNo']
    
    dictList = []
    anotherDict = {}
    #loop over the multiple stocks over a particular invoice,customer,country,invoicedate
    for i in j.index:

        anotherDict['StockCode'] = int(j.at[i, 'StockCode'])
        anotherDict['Description'] = j.at[i, 'Description']
        anotherDict['Quantity'] = int(j.at[i, 'Quantity']) ##int(store['count'].iloc[i])
        anotherDict['UnitPrice'] = j.at[i, 'UnitPrice']


        dictList.append(anotherDict.copy())

    dictionary['stockdetails'] = dictList


    finalList.append(dictionary)

# Print the Data to Json	
jsondata = json.dumps(finalList)
jsonFile = open("sample_invoice_data.json", "w")
jsonFile.write(jsondata)
jsonFile.close()