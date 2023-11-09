# Benchmarking LAMBDA and EC2 with Go
This repository contains the source code for a simple HTTP server to benchmark the differences in performance between Lambda functions and EC2 containers on AWS. This performance test will focus on response times and throughput.

## Design
### EC2 Container
A simple HTTP server will be created with one endpoint. It will provide a simple response when a GET request is made to the endpoint.

### Lambda Function
Due to the nature of the Lambda function abstraction, little code is required to create an HTTP endpoint. The function will simply return a value to the request at the endpoint exposed by the function URL.

## Tests
The test suite will compare the times for first response after various time intervals. The program will wait 0.1, 0.5, 1, 5, 10, 30, and 60 seconds between requests and see how the performance changes. Additionally, the response time for the first cold start API call will be measured.

Measurement of throughput will be achieved by sending as many requests with as many threads as possible to each of the programs and measuring how many responses are returned in a given timeframe. Each thread will wait for a response before sending the next request, but there will be multiple threads to avoid the client bottlenecking the test.
