.PHONY:
	build
	run
	clean

build:
	cd example-test-app; docker build -t oceannik/example-test-app -f Containerfile .

run:
	docker run -d -p 8080 \
		-e APP_WORKSPACE=user \
		--name oceannik-test-app \
		oceannik/example-test-app

clean:
	docker stop oceannik-test-app
	docker rm oceannik-test-app
