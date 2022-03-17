import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        json_data = req.get_body()
        json_loads_py = json.loads(json_data)
        logging.info("JSON Data is Passed Successfully.")
        logging.info(json_loads_py)

        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Ok",
              status_code=200
        )
        
    except ValueError as err:
            logging.error(err)
            
            return func.HttpResponse(
                f"Error: {err}",
                 status_code=400
        )

        



