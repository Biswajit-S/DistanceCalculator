# DistanceCalculator

A REST API that accepts two distances (numbers) and returns the total distance (sum of both).

## Directory Structure

### Docs
* Contains the design documents and the information used for impact assessment.

### Lambda Function
* Lambda function (index.py) used for the business logic.

### CloudFormation
* The YAML file used to create the AWS stack.

## Testing the API
* The CloudFormation template generates the API URL to be used. After creating the stack with CloudFormation, get the URL from the Outputs.

### Request
```
POST https://DUMMY-API-GATEWAY-HOST.amazonaws.com/distance

Post Body:
{
    "distance": [5, 3],
    "unit": "Meters"
}

Request Header:
Content-Type: application/json
Accept: application/json
```

### Success Response

```
{
    "result": 8,
    "unit": "Meters"
}

```
