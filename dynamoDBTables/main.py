import boto3

# Initialize a session using Amazon Dynamodb
dynamodb = boto3.resource('dynamodb')
table_name = 'YourTableName'
table = dynamodb.Table(table_name)

def get_item(key):
    """
    Retrieve an item from the DynamoDB table by its key.

    :param key: The primary key of the item to retrieve.
    :return: The item if found, otherwise None.
    """
    try:
        response = table.get_item(Key=key)
        return response.get('Item', None)
    except Exception as e:
        print(f"Error retrieving item: {e}")
        return None

