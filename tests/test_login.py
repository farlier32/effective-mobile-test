from pages.login_page import LoginPage


def test_successful_login(page):
    login = LoginPage(page)
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html", timeout=2000)
    assert "inventory.html" in page.url

def test_wrong_password(page):
    login = LoginPage(page)
    login.login("standard_user", "wrongpass.O_o")
    page.wait_for_selector("[data-test='error']", timeout=2000)


def test_locked_user(page):
    login = LoginPage(page)
    login.login("locked_out_user", "secret_sauce")
    page.wait_for_selector("[data-test='error']", timeout=2000)



def test_empty_user(page):
    login = LoginPage(page)
    login.login("", "")
    page.wait_for_selector("[data-test='error']", timeout=2000)




def test_glith_user(page):
    login = LoginPage(page)
    login.login("performance_glitch_user", "secret_sauce")
    page.wait_for_url("**/inventory.html", timeout=10000)

