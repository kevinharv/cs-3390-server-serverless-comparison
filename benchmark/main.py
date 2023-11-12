import requests
import time
import csv
from concurrent.futures import ThreadPoolExecutor
from constants import *

def benchmark(endpoint, thread):
	results = []
	for i in range(500):
		start_time = time.time()
		res = requests.get(endpoint)
		end_time = time.time()
		duration = (end_time - start_time)
		print(f"Request {i} in thread {thread} took {duration}s")
		results.append({
			"thread": thread,
			"sequence": i,
			"start": start_time,
			"end": end_time,
			"duration": duration,
			"success": res.status_code
		})
	return results

def main():
	lambda_results = []
	ec2_results = []
	print("Starting Benchmark")
	with ThreadPoolExecutor(max_workers=6) as executor:
		a = executor.submit(benchmark, LAMBDA_URL, 1)
		b = executor.submit(benchmark, LAMBDA_URL, 2)
		c = executor.submit(benchmark, LAMBDA_URL, 3)
		print("Lambda Threads Started")

		# lambda_results.append(a.result())
		lambda_results += a.result()
		print("Lambda 1 Complete")
		# lambda_results.append(b.result())
		lambda_results += b.result()
		print("Lambda 2 Complete")
		# lambda_results.append(c.result())
		lambda_results += c.result()
		print("Lambda 3 Complete")
	    


		d = executor.submit(benchmark, EC2_URL, 4)
		e = executor.submit(benchmark, EC2_URL, 5)
		f = executor.submit(benchmark, EC2_URL, 6)
		ec2_results += d.result()
		print("EC2 1 Complete")
		# ec2_results.append(e.result())
		ec2_results += e.result()
		print("EC2 2 Complete")
		# ec2_results.append(f.result())
		ec2_results += f.result()
		print("EC2 3 Complete")
        
	print("Writing Results")
	with open('lambda_res.csv', 'w') as file:
		writer = csv.DictWriter(file, lambda_results[1].keys())
		writer.writeheader()
		writer.writerows(lambda_results)

	with open('ec2_res.csv', 'w') as file:
		writer = csv.DictWriter(file, ec2_results[1].keys())
		writer.writeheader()
		writer.writerows(ec2_results)

	print("Benchmark Complete")


if __name__ == "__main__":
	main()
