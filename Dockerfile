FROM mcr.microsoft.com/playwright/python:v1.57.0-jammy

WORKDIR /app

COPY requirements.txt .
COPY pages/ ./pages/
COPY tests/ ./tests/
COPY pytest.ini .

RUN pip install --no-cache-dir \
    pytest==9.0.2 \
    pytest-playwright==0.7.2 \
    allure-pytest==2.15.3 \
    pytest-base-url==2.1.0

RUN mkdir -p /app/allure-results /app/reports

CMD ["pytest", "tests/", "--alluredir=allure-results", "-v", "-s"]
