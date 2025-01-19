def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},   #it really works by Hector Duran!
        "body": "<h1>Hello World</h1>"
    }

