import os
import requests
import time
import logging

LAMBDA_URL = os.environ.get("LAMBDA_URL", "hi")
EC2_URL = os.environ.get("EC2_URL", "mom")


def lambda_measure_cold_start_latency():
	logging.info("Measuring Lambda Cold Start Performance")
	lambda_start_time = time.time()
	res = requests.get(LAMBDA_URL)
	lambda_end_time = time.time()
	logging.info(f"Request took {(lambda_end_time - lambda_start_time)/10000} ms")
	return (lambda_end_time - lambda_start_time)/10000


def main():
	print(f"{lambda_measure_cold_start_latency()} ms")


if __name__ == "__main__":
	main()