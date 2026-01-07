# Effective Mobile AQA **5/5 PASSED**

**Автоматизация тестирования авторизации**  

- **5 тестов авторизации** (все сценарии)
- **Page Object Model** (`pages/login_page.py`)
- **Playwright**
- **Проверка URL + элементов**
- **Allure отчетность**
- **Python 3.10**
- **Docker**

## Локальный запуск
```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/ --alluredir=allure-results -v -s -W ignore
allure serve allure-results/ # localhost:8080
```

## Docker
 
**bash / Linux / macOS**
```
docker build -t emtest .
docker run --rm -v $(pwd)/allure-results:/app/allure-results emtest
allure serve allure-results/
```

**Windows PowerShell**
```
docker build -t emtest .
docker run --rm -v ${PWD}/allure-results:/app/allure-results emtest
allure serve allure-results/
```
![Allur Overview](https://github.com/user-attachments/assets/bf17fa2c-1211-4317-8131-42072a5d98eb)
![Allur Graphs](https://github.com/user-attachments/assets/891ff3bb-ff68-487b-bd33-762b724be491)
