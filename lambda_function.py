import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Babu That the GitHub Actions Lambda Deployment!')
    }

