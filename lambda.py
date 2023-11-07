import urllib3
import json
http = urllib3.PoolManager()

def process_message(input):
    try:
        # Loading JSON into a string
        raw_json = json.loads(input)
        # Outputing as JSON with indents
        output = json.dumps(raw_json, indent=4)
    except:
        output = input
    return output


def lambda_handler(event, context):
    url = "SLACK WEBHOOK"
    msg = {
        "channel": "#CHANNEL",
        "text": process_message(event['Records'][0]['Sns']['Message']),
        "icon_emoji": ""
    }
    
    encoded_msg = json.dumps(msg).encode('utf-8')
    resp = http.request('POST',url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'], 
        "status_code": resp.status, 
        "response": resp.data
    })