.PHONY: help install run test clean docker-build docker-run docker-stop

help:
	@echo "Available commands:"
	@echo "  make install      - Install dependencies"
	@echo "  make run          - Run the API server"
	@echo "  make test         - Run tests"
	@echo "  make clean        - Clean cache and build files"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-run   - Run Docker container"
	@echo "  make docker-stop  - Stop Docker container"

install:
	pip install -r requirements.txt

run:
	uvicorn api.server:app --reload --port 7860

test:
	pytest tests/ -v --tb=short

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov dist build *.egg-info

docker-build:
	docker build -t openenv-support-agent:latest .

docker-run:
	docker-compose up -d

docker-stop:
	docker-compose down

docker-logs:
	docker-compose logs -f app
