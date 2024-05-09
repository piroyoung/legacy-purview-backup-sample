DOCKER_IMAGE = "pvsnapshot:local"

.PHONY: build
build:
	@echo "Building..."
	docker build -t $(DOCKER_IMAGE) .

run: build
	@echo "Running..."
	docker run -it --rm \
		-e CLIENT_ID=$(CLIENT_ID) \
		-e CLIENT_SECRET=$(CLIENT_SECRET) \
		-e TENANT_ID=$(TENANT_ID) \
		-e PURVIEW_ENDPOINT=$(PURVIEW_ENDPOINT) \
		--name pvsnapshot \
		$(DOCKER_IMAGE)

test: build
	@echo "Running tests..."
	docker run -it --rm \
		-e CLIENT_ID=$(CLIENT_ID) \
		-e CLIENT_SECRET=$(CLIENT_SECRET) \
		-e TENANT_ID=$(TENANT_ID) \
		-e PURVIEW_ENDPOINT=$(PURVIEW_ENDPOINT) \
		--name pvsnapshot \
		$(DOCKER_IMAGE) poetry run pytest
