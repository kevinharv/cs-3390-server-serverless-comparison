run:
	docker run -it --rm --name ec2-bench -p 8080:8080 kevinharv/go-ec2-bench

build:
	docker build . -t kevinharv/go-ec2-bench:latest

clean:
	docker rmi kevinharv/go-ec2-bench