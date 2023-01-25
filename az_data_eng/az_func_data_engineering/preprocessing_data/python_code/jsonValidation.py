import json
# jsonschema is an implementation of the JSON Schema specification for Python.
import jsonschema
from jsonschema import validate
from pprint import pprint

transaction_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
            "InvoiceNo": {
                "type": "integer"
            },
        "StockCode": {
                "type": "integer"
                },
        "Description": {
                "type": "string"
                },
        "Quantity": {
                "type": "integer",
                },
        "InvoiceDate": {
                "type": "string"
                },
        "UnitPrice": {
                "type": "number"
                },
        "CustomerID": {
                "type": "integer"
                },
        "Country": {
                "type": "string"
                }
    },
    "required": [
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "CustomerID",
        "InvoiceDate",
        "UnitPrice"

    ]
}

# create a validation function


def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True


def validate_json_schema(json_data, my_schema):
    """REF: https://json-schema.org/ """
    schema = my_schema
    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is not valid "
        return False, err
    error_message = "Given JSON is valid."
    return True, error_message

#if __name__ == '__main__':

 #   with open("./data/data_subset.json") as json_file:
  #      data = json.load(json_file)

   # valid_transaction_dict = data[0]
    #pprint(valid_transaction_dict)
    