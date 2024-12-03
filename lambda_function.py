import json
import boto3
from datetime import datetime

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorsData')

def lambda_handler(event, context):
    try:
        # Log the entire event for debugging purposes
        print("Received event:", json.dumps(event))
        
        # Convert the JSON-formatted string from the event's body into a Python dictionary
        if 'body' not in event:
            raise ValueError("Missing 'body' in event")

        body = json.loads(event['body'])

        # Check if the necessary 'page' key is part of the input data
        if 'page' not in body:
            raise ValueError("Missing 'page' key in event")

        # Retrieve the 'page' value from the parsed event body
        page = body['page']
        
        # Log the page value to ensure it's captured correctly
        print(f"Page value extracted: {page}")

        # Add the current timestamp in ISO format
        current_timestamp = datetime.now().isoformat()

        # Prepare the item to be stored in DynamoDB
        item = {
            'Timestamp': current_timestamp,  # Partition Key
            'Page': page                      # Sort Key
        }

        # Log the item to be inserted to DynamoDB
        print(f"Item to be inserted into DynamoDB: {item}")

        # Store the item in DynamoDB
        table.put_item(Item=item)

        # Return a success status code and message if data is added successfully
        return {
            'statusCode': 200,
            'body': json.dumps('Page visit recorded successfully!')
        }
    
    except Exception as e:
        # Log the exception detail for debugging
        print(f"Error occurred: {str(e)}")
        
        # Return an error status code and message if an exception occurs
        return {
            'statusCode': 400,
            'body': json.dumps(f"Error: {str(e)}")
        }