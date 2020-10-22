import json

def lambda_handler(event, context):
    result = exp_func(int(event['queryStringParameters']["x"]), int(event['queryStringParameters']["y"]))
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',

        },
        'body': json.dumps(result)
    }
def exp_func(x, y):
    if (not isinstance(x, int)) or (not isinstance(y, int)):
        return "please input integers"
    exp = bin(y)
    # print(exp)
    value = x
 
    for i in range(3, len(exp)):
        value = value * value
        if(exp[i:i+1]=='1'):
            value = value*x
    return value

# print(exp_func(2, 1023))