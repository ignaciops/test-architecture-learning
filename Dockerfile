FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

# Copy framework and tests
COPY framework/ framework/
COPY tests/ tests/
COPY pytest.ini .

# Run tests by default
CMD ["pytest", "tests/", "--alluredir=allure-results"]