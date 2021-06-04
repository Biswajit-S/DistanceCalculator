# Impact Assessment - AWS

## Option-A [_Preffered_]

### Stack
* Lambda, API Gateway and Cloud Watch

### Benifits
* Fully Serverless
* Low Cost (__56.88 USD__ per year for 1 billion API requests per month)
* No cost, when no APIs are invoked.


### Drawbacks
* Future improvemnets could be expensive, if the API consumes more memory or processing time


## Option-B
### Stack
* EC2 hosted Application Server (NGINX) + ASG
* API Gateway, Cloud Watch 

### Benifits
* Not much dependency on language or type of application server. Any type of server and architectire can be supported.
* Scalabe and Highly Available with Auto Scalaing Group. 

### Drawbacks
* Locked to a Availability Zone and Region.
* At least 2 EC2 instances should be running all time to support High Availability
* Server and OS maintenance needed.
* Expensive (__759.00 USD__ per year for one EC2 instance of 2 vCPU, 8 GB, 3 years All upfront Reserved)



## Option-C

### Stack
* ECS hosted App Server (NGINX) + Container Auto Scaling
* API Gateway, ECR, Cloud Watch

### Benifits
* Multiple containers can run in same EC2 instance.
* Container level auto scaling according to the traffic volume.

### Drawbacks
* Locked to a Availability Zone and Region.
* Server and OS maintenance needed. Alternately Fargare can be used, but expensice, so discarded.
* Expensive (__1,518.00 USD__ per year for two instances of 2 vCPU, 8 GB, 3 years All upfront Reserved)
