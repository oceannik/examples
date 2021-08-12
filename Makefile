.PHONY:
	build
	run
	clean

build:
	cd examples-test-app; docker build -t oceannik/examples-test-app -f Containerfile .

run:
	docker run -d -p 8080 -e APP_WORKSPACE=MakefileCMD --name oceannik-test-app oceannik/examples-test-app

clean:
	docker stop oceannik-test-app
	docker rm oceannik-test-app
