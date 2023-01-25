import logging
from typing import List
import azure.functions as func


def main(event: List[func.EventHubEvent],
        outputDocumentData: func.Out[func.Document]):

    for events in event:
        json_data = events.get_body()
        logging.info('Event has been triggered into Cosmos Db')
        outputDocumentData.set(func.Document.from_json(json_data))
        logging.info('Event has been inserted into Cosmos Db')
