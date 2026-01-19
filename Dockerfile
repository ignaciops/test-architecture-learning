FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

# Copy framework and tests
COPY framework/ framework/
COPY tests/ tests/

RUN mkdir -p allure-results

# Run tests by default
CMD ["pytest", "tests/", "-v", "--alluredir=allure-results"]