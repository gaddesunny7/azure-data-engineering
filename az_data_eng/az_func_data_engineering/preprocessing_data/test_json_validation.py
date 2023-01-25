import pytest
import json
from jsonschema import validate
import pandas as pd 
from python_code.jsonValidation import validate_json,validate_json_schema


data = pd.read_json("C:/Users/user/Desktop/real_streaming_data/dataset/sample_invoice_data.json",lines = True)

data = data.to_json(orient='records')
    
class TestValidationJson:
    def test_validate_json_Should_return_True_when_valid_json_string(self):
        # Arrange
        #json_string = '[{"InvoiceasdNo": 536370, "StockCode": 22492, "Description": "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45", "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}, {"InvoiceNo": 536372, "StockCode": 22632, "Description": "HAND WARMER RED POLKA DOT", "Quantity": 6, "InvoiceDate": "12/1/2010 9:01", "UnitPrice": 1.85, "CustomerID": 17850, "Country": "United Kingdom"}, {"InvoiceNo": 536389, "StockCode": 22727, "Description": "ALARM CLOCK BAKELIKE RED", "Quantity": 4, "InvoiceDate": "12/1/2010 10:03", "UnitPrice": 3.75, "CustomerID": 12431, "Country": "Australia"}, {"InvoiceNo": 562106, "StockCode": 22993, "Description":"SET OF 4 PANTRY JELLY MOULDS", "Quantity": 1, "InvoiceDate": "8/2/2011 15:19", "UnitPrice": 1.25, "CustomerID": 14076, "Country": "United Kingdom"}]'

        # Act
        is_valid_json = validate_json(data)

        # Assert
        assert is_valid_json == True

    def test_validate_json_Should_return_False_when_invalid_json_string(self):

        # Arrange
        invalid_json_string = '{"InvoiceNo": 536370asdsa "StockCode": 22492, "Description":  "MINI PAINT SET VINTAGE", "Quantity": 36, "InvoiceDate": "12/1/2010 8:45",   "UnitPrice": 0.65, "CustomerID": 12583, "Country": "France"}'

        # Act
        is_valid_json = validate_json(invalid_json_string)

        # Assert
        assert is_valid_json == False 
        

    def test_validate_json_schema_Should_return_True_when_valid_json_schema(self):
        #sample_String 
        sample_String = {"InvoiceNo":"C571637","CustomerID":14688,"Country":"United Kingdom","InvoiceDate":"10\/18\/2011 11:55","StockDetails":[{"StockCode":22381,"Description":"TOY TIDY PINK POLKADOT","Quantity":-1,"UnitPrice":1.85},{"StockCode":23348,"Description":"CHILDRENS TOY COOKING UTENSIL SET","Quantity":-2,"UnitPrice":2.08},{"StockCode":22379,"Description":"RECYCLING BAG RETROSPOT ","Quantity":-39,"UnitPrice":1.85}]}
        # Arrange

        invoice_schema = {
                "type": "object",
                "properties": {
        
                    "InvoiceNo": {
                        "type": "string"
                    },
                    "CustomerID": {
                        "type": "integer"
                    },
                    "Country": {
                        "type": "string"
                    },
                    "InvoiceDate": {
                        "type": "string"
                    },
                "StockDetails": {
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
                    "StockDetails"
                             ]
                        }
                # Act
        is_valid_json_schema, message = validate_json_schema(
            sample_String,  my_schema=invoice_schema)
                # Assert
        assert is_valid_json_schema == True
        assert message == "Given JSON is valid."


   