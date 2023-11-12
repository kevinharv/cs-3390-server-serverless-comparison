import os
import requests
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from constants import *

def lambda_measure_cold_start_latency():
	logging.info("Measuring Lambda Cold Start Performance")
	lambda_start_time = time.time()
	res = requests.get(LAMBDA_URL)
	lambda_end_time = time.time()
	logging.info(f"Request took {(lambda_end_time - lambda_start_time)/10000} ms")
	return (lambda_end_time - lambda_start_time)/10000


def main():
	with ThreadPoolExecutor(max_workers=4) as executor:
		execs = []
		for i in range(500):
			a = executor.submit(pow, 2, 2000)
			# instead of power, this should make requests, but like for 30 seconds
			execs.append(a)

		for e in execs:
			print(e.result())


if __name__ == "__main__":
	main()