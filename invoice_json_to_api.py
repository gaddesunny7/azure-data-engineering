import pandas as pd
import requests
import numpy as np

# URL of your endpoint
URL = "https://api-dev-az.azure-api.net/fa-dev-az/HttpTriggerSendInvoiceDataToEventHub"


#read the jsonfile

data = pd.read_json("sample_invoice_data.json")

# write all the rows from the testfile to the api as put request
for i in data.index:
    try:
        # convert the row to json
        export = data.loc[i].to_json()

        #send it to the api
        response = requests.post(URL, data = export)

        # print the returncode
        print(export)
        print(response)
    except:
        print(data.loc[i])