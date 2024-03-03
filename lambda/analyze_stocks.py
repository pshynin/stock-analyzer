def lambda_handler(event, context):
    # Extracting data from the event
    name = event.get('name', 'World')

    # Constructing the response
    message = f'Hello, {name}!'

    # Returning the response
    return {
        'statusCode': 200,
        'body': message
    }
