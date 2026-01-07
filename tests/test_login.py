import allure
import pytest
from pages.login_page import LoginPage


@allure.epic("Saucedemo AQA")
@allure.feature("Авторизация")
@pytest.mark.smoke
class TestLogin:


    @allure.story("Успешная авторизация")
    @allure.title("Стандартный пользователь → inventory.html")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверяет успешный вход standard_user с корректными данными")
    def test_successful_login(self, page):
        login = LoginPage(page)
        login.login("standard_user", "secret_sauce")
        page.wait_for_url("**/inventory.html", timeout=2000)
        assert "inventory.html" in page.url


    @allure.story("Неверные учетные данные")
    @allure.title("Неправильный пароль → сообщение об ошибке")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("negative")
    def test_wrong_password(self, page):
        login = LoginPage(page)
        login.login("standard_user", "wrongpass.O_o")
        page.wait_for_selector("[data-test='error']", timeout=2000)


    @allure.story("Заблокированный пользователь")
    @allure.title("locked_out_user → ошибка доступа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("negative")
    def test_locked_user(self, page):
        login = LoginPage(page)
        login.login("locked_out_user", "secret_sauce")
        page.wait_for_selector("[data-test='error']", timeout=2000)


    @allure.story("Пустые поля")
    @allure.title("Пустой username/password → валидация формы")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("negative", "validation")
    def test_empty_user(self, page):
        login = LoginPage(page)
        login.login("", "")
        page.wait_for_selector("[data-test='error']", timeout=2000)


    @allure.story("Медленный пользователь")
    @allure.title("performance_glitch_user → медленный вход (10s)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_glith_user(self, page):
        login = LoginPage(page)
        login.login("performance_glitch_user", "secret_sauce")
        page.wait_for_url("**/inventory.html", timeout=10000)

