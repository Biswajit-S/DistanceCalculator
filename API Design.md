# Distance Claculator

This file describes, how the API is structured, input and output response.

## Method - POST
* Accepting Input Data, hence POST

## Input Attributes
* distance: Integer Array (_Max Two Values_)
* unit: String

## Input Validation
* Check distance attribute has only 2 values.
* Unit contains only Meters.
* Support for any additional Unit, without much change in the business logic.

## API Structure
* API is accessible via API Gateway
* https://api-gateway-host/distance

## Content Type
* Content-Type: application/json
* Accept: application/json

## Response Attributes / Structure

### Success
* result: Integer
* unit: String

### Failure
* error_message: String

## Sample Request

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

### Failure Response

```
{
    "error_message": "Unit not Supported"
}

```