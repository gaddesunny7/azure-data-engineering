import pandas as pd
import fire
import os 
import requests
import time
#from dotenv import load_dotenv

#load_dotenv()

OCP_APIM_SUBSCRIPTION_VALUE = "11111111111111111111111111111111111111"
URL = "1111111111111111111111111111111111111111111111"

headers = {
    'Host': '**************************************',
    'Ocp-Apim-Subscription-Key': '**************************************',
    'Ocp-Apim-Trace': 'true'
}


invoice_sample = pd.read_json(
        "./dataset/sample_invoice_data.json",
        orient="records", lines=True)
invoices = 6
if invoices < 20:  # tweets_stream_sample.shape[0]:
    invoice_stream_sample = invoice_sample.iloc[:invoices, ]
    for i in invoice_stream_sample.index:

        print(invoice_stream_sample.iloc[i])
        records_for_export = invoice_stream_sample.iloc[i].to_json()
        request = requests.post(
            url=URL, data=records_for_export, headers=headers)
        if request.status_code == 200:
            print(f"Request number {i} is succesfullly posted.")
            print(records_for_export)
            time.sleep(10)
            print(request.content)
            print(request.status_code)
        else:
                print(
                    f"Request number {i} NOT succeded! Status code {request.status_code}")
else:
    print(f"Maximum number of Invoices is {invoice_sample.shape[0]}, and you have chosen: {invoices}. Please choose a smaller number!")

    
    
