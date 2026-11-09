from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"

def test_login_valido(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(page.locator(".title")).to_have_text("Products")


def test_login_senha_incorreta(page: Page):
    page.goto(BASE_URL)

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("senha_errada")
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_be_visible()


def test_login_campos_vazios(page: Page):
    page.goto(BASE_URL)

    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_be_visible()
    expect(page).to_have_url(BASE_URL)
