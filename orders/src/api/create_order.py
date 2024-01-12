import os
import boto3
from decimal import Decimal
import json
import uuid
from datetime import datetime

# Globals
orders_table = os.getenv('TABLE_NAME')
dynamodb = boto3.resource('dynamodb')

def add_order(event, context):
    detail = json.loads(event['body'])
    restaurantId = detail['restaurantId']
    totalAmount = detail['totalAmount']
    orderItems = detail['orderItems']
    userId = event['requestContext']['authorizer']['claims']['sub']
    orderTime = datetime.strftime(datetime.utcnow(), '%Y-%m-%dT%H:%M:%SZ')
    orderId = detail['orderId']

    ddb_item = {
        'orderId': orderId,
        'userId': userId,
        'data': {
            'orderId': orderId,
            'userId': userId,
            'restaurantId': restaurantId,
            'totalAmount': totalAmount,
            'orderItems': orderItems,
            'status': 'PLACED',
            'orderTime': orderTime,
        }
    }
    ddb_item = json.loads(json.dumps(ddb_item), parse_float=Decimal)
    table = dynamodb.Table(orders_table)
    table.put_item(Item=ddb_item)
    detail['orderId'] = orderId
    detail['status'] = 'PLACED'
    return detail

def lambda_handler(event, context):
    """Handles the lambda method invocation"""
    try:
        orderDetail = add_order(event, context)
        response = {
            "statusCode": 200,
            "headers": {},
            "body": json.dumps(orderDetail)
        }
        return response
    except Exception as err:
        raise
