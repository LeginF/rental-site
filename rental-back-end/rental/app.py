import json
import logging
import boto3
from http import HTTPStatus, HTTPMethod
import util
import reservation
import inventory
import customer
import health
import reservation
import payment
# import requests

# set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(event)
    path = event['path']
    params = event['queryStringParameters']

    match path:
        case "health":
            return health.handler(event, context, logger)
        case "inventory":
            return inventory.handler(event, context, logger)
        case "reservation":
            return reservation.handler(event, context, logger)
        case "customer":
            return customer.handler(event, context, logger)
        case "payment":
            return payment.handler(event, context, logger)
        case _:
            return util.buildResponse(HTTPStatus.NOT_FOUND)



