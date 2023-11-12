run: build
	docker run -it --rm --name ec2-bench -p 8080:8080 kevharv/go-ec2-bench

push: build
	docker push kevharv/go-ec2-bench

build:
	docker build . -t kevharv/go-ec2-bench:latest

clean:
	docker rmi kevharv/go-ec2-bench