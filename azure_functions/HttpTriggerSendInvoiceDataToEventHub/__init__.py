import logging
import json
import jsonschema
from jsonschema import validate

import azure.functions as func

invoice_schema = {
    "type": "object",
    "properties": {
        "CustomerID": {
            "type": "integer"
        },
        "Country": {
            "type": "string"
        },
        "InvoiceDate": {
            "type": "string"
        },
        "InvoiceNo": {
            "type": "string"
        },
    "stockdetails": {
            "type": "array",
            "items": {
            "type": "object",
            "properties": {
                "StockCode": {
                    "type":"number"
                },
                "Description": {
                    "type":"string"
                },
                "Quantity": {
                    "type":"number"
                },
                "UnitPrice": {
                    "type":"number"
                },
            },
        }
        },   
        
    },
    "required": [
        "CustomerID",
        "Country",
        "InvoiceDate",
        "InvoiceNo",
        "stockdetails"
    ]
}



def main(req: func.HttpRequest,
         outputEventHubMessage: func.Out[bytes]
         ) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        json_data = req.get_body()
        json_loads_py = json.loads(json_data)
        logging.info("JSON Data is Passed Successfully.")
        logging.info(json_loads_py)

        
        ### Do different unit tests
        validate(instance=json_loads_py, schema=invoice_schema)
        logging.info("JSON schema is valid!")

        outputEventHubMessage.set(json_data)
        logging.info("Invoice is sent to Event Hub")

        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Ok",
              status_code=200
        )
        
        
    except json.JSONDecodeError as err:

        logging.error(f"Invalid JSON passed! Error: {err}")

        return func.HttpResponse(
            f"Invalid json passed! Error: {err}",
            status_code=400
        )

    except jsonschema.exceptions.ValidationError as err:

        logging.error(f"JSON Schema is not valid! Error: {err}")

        return func.HttpResponse(
            f"JSON Schema is not valid! Error: {err}",
            status_code=400
        )

    except ValueError as err:
        logging.error(err)

        return func.HttpResponse(
            f"Error: {err}",
            status_code=400
        )

        



