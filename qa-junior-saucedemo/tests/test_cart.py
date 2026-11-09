from playwright.sync_api import Page, expect

def test_adicionar_produto_carrinho(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    expect(page.locator(".title")).to_have_text("Products")

    page.locator(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()

    expect(
        page.locator("[data-test='shopping-cart-badge']")
    ).to_have_text("1")

    page.locator("[data-test='shopping-cart-link']").click()

    expect(
        page.locator("[data-test='inventory-item-name']")
    ).to_have_text("Sauce Labs Backpack")
