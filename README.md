# Benchmarking LAMBDA and EC2 with Go
This repository contains the source code for a simple HTTP server to benchmark the differences in performance between Lambda functions and EC2 containers on AWS. This performance test will focus on response times and throughput.

## Design
### EC2 Container
A simple HTTP server will be created with one endpoint. It will respond with "Hello World!" when a GET request is made. 

### Lambda Function
Due to the nature of the Lambda function abstraction, little code is required to create an HTTP endpoint. It also returns "Hello World!" in plain text.

## Tests
The benchmark program makes as many requests to both the Lambda function and the ECS container as possible. It measures the response times for both and writes the data to a CSV file. This can be analyzed and graphed in Excel to draw conclusions about the relaive performance of the two paradigms/technologies.
