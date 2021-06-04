# AWS Stack Design

## Lambda
* Lambda Funtion to accept two distance values and an unit in POST body.
* Validate Inputs and send a response and proper status code.
* Put the Supported units in Lambda properties. (Start with a local variable in python function, then add a properties later.) 

## API Gateway
* API Gateway integration with the Lambda service, as AWS Proxy integration.

## Cloud Watch
* Cloud watch to collect Lambda logs.
* Log retention for 90 days.

## IAM 
* Assume Role for Lambda to push logs to Cloud Watch.