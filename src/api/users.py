import json
import uuid
import os
import boto3
from datetime import datetime

USERS_TABLE = os.getenv('USERS_TABLE', None)
dynamodb = boto3.resource('dynamodb')
userTable = dynamodb.Table(USERS_TABLE)


def lambda_handler(event, context):
    print("--------Users event")
    print(event)
    route_key = f"{event['httpMethod']} {event['resource']}"
    response_body = {'Message': 'Unsupported route'}
    status_code = 400
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
        }

    try:

        if route_key == 'GET /users':
            ddb_response = userTable.scan(Select='ALL_ATTRIBUTES')
            response_body = ddb_response['Items']
            status_code = 200

        if route_key == 'GET /users/{userid}':
            ddb_response = userTable.get_item(
                Key={'userid': event['pathParameters']['userid']}
            )
            if 'Item' in ddb_response:
                response_body = ddb_response['Item']
            else:
                response_body = {}
            status_code = 200
        
        if route_key == 'DELETE /users/{userid}':
            userTable.delete_item(
                Key={'userid': event['pathParameters']['userid']}
            )
            response_body = {}
            status_code = 200

        if route_key == 'POST /users':
            request_json = json.loads(event['body'])
            request_json['timestamp'] = datetime.now().isoformat()
            if 'userid' not in request_json:
                request_json['userid'] = str(uuid.uuid1())
            userTable.put_item(
                Item=request_json
            )
            response_body = request_json
            status_code = 200

        if route_key == 'PUT /users/{userid}':
            # update item in the database
            request_json = json.loads(event['body'])
            request_json['timestamp'] = datetime.now().isoformat()
            request_json['userid'] = event['pathParameters']['userid']
            userTable.put_item(
                Item=request_json
            )
            response_body = request_json
            status_code = 200
    except Exception as err:
        status_code = 400
        response_body = {'Error:': str(err)}
        print(str(err))

    return {
        'statusCode': status_code,
        'body': json.dumps(response_body),
        'headers': headers
    }
