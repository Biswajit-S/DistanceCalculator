import json

'''
For now supported units are defined as a local variable. 
This should be read from a Lambda property.
'''
supported_units = ["METERS"]

'''
Lambda handler to acccept the request and server a response.

'''
def handler(event,context):
  print(event)
  response = {}
  status_code = 200
  try:
    payload = event['body']
    json_data = json.loads(payload)
    distance = json_data.get("distance")
    unit = json_data.get("unit")
    
    # Validate the input parameter, before processing. If no exception thrown, proceed.
    if(validate_inputs(distance, unit)):
      response["result"] = distance[0] + distance[1]
      response["unit"] = unit

  # If input validation fails, set status code as 400 and return the error message.        
  except ValueError as e:
      response["error_message"] = str(e)
      status_code = 400

  except Exception as e:    
      response["error_message"] = "Server could not process the request"
      status_code = 500       
  
  return {
    'body': json.dumps(response),
    'headers': {
      'Content-Type': 'application/json'
    },
    'statusCode': status_code
  }

'''
Check, if the distance attribute has exactly two values and the unit provided is allowed.
'''
def validate_inputs(distance, unit):
    if len(distance) != 2:
        raise ValueError("TWO values should be provided for distance")
    
    if unit.upper() not in supported_units:
        raise ValueError("Unit not Supported")
    
    return True
