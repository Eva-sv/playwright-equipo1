from playwright.sync_api import Page, expect
from pages import confirmation_page
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingcartPage
from pages.confirmation_page import ConfirmationPage



def test_checkout_with_valid_payment_details(page: Page):
    products_page = ProductsPage(page)
    check_out_page = CheckoutPage(page)
    shopping_cart_page = ShoppingcartPage(page)

    
    # Logica del ProductsPAge
    print("When the user enters to the products page")
    products_page.open_products_page()

    print("When they filter by name 'Palas'")
    products_page.filter_by_name("Palas")

    print("And add the product to the cart")
    products_page.adds_product_to_cart("Juego de Palas")

    print("And visit the cart page")
    products_page.click_cart_page()
    
    # Logica del CartsPage
    print("And click on 'Proceed to checkout'")
    shopping_cart_page.click_proceed_to_check_out()

    print("Then they should see the order summary whith the folliwing details: ")
    shopping_cart_page.verify_shopping_cart_summary()

    print("The product name: Juego de Palas")
    shopping_cart_page.verify_products_in_shopping_cart_summary("Juego de Palas15.99 €")

    print("The subtotal(1)15.99 €")   
    shopping_cart_page.verify_shopping_cart_subtotal("Subtotal(1)15.99 €")

    print("The IVA (21%)3.36 €")
    shopping_cart_page.verify_products_iva("3.36 €")

    print("The shipping cost: 5.00 €")
    shopping_cart_page.verify_products_shipping_cost()

    print("The total: 24.35 €")
    shopping_cart_page.verify_products_total("Total24.35 €")

    print("When they fill in the valid name field 'Maria Diaz'")
    check_out_page.fill_valid_name_field()

    print("And fill in the valid email field")
    check_out_page.fill_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    check_out_page.fill_valid_adress()

    print("And add a valid card number ")
    check_out_page.add_credit_card("4242424242424242")

    print("And click on 'Complete purchase'")
    check_out_page.click_complete_purchase()

    print("Then they should see the message 'Purchase completed successfully")
    confirmation_page = ConfirmationPage(page)
    confirmation_page.verify_message_purchase_completed_succesfully()

    print("And they should see the completed order page with: 'Resumen del pedido'")
    confirmation_page.verify_shopping_cart_summary("Resumen del Pedido")

    print("And they should see The product name: Juego de Palas15.99 €")
    confirmation_page.verify_product_name("Juego de Palas15.99 €")

    print("And they should see The subtotal(1)15.99 €")
    confirmation_page.verify_shopping_cart_subtotal("Subtotal(1)15.99 €")

    print("And they should see The IVA (21%)3.36 €")
    confirmation_page.verify_products_iva("3.36 €")

    print("And they should see The shipping cost: 5.00 €")
    confirmation_page.verify_products_shipping_cost()

    print("And they should see The total: 24.35 €")
    confirmation_page.verify_products_total("Total24.35 €")

    print("When they click on 'Back to store'")
    confirmation_page.click_back_store()

    print("Then they should see the products page: https://web_qa.dev.adalab.es/products")
    check_out_page.verify_see_products_page()

    
def test_checkout_with_invalid_card_details(page: Page):

    products_page = ProductsPage(page)
    check_out_page = CheckoutPage(page)
    shopping_cart_page = ShoppingcartPage(page)
    
    print("When the user enters to the products page")
    products_page.open_products_page()

    print("When they filter by name 'palas'")
    products_page.filter_by_name("Palas")

    print("And add the product to the cart")
    products_page.adds_product_to_cart("Juego de Palas")

    print("And visit the cart page")
    products_page.click_cart_page()

    print("And click on 'Proceed to checkout'")
    shopping_cart_page.click_proceed_to_check_out()

    print("When they fill in the valid name field 'Maria Diaz'")
    check_out_page.fill_valid_name_field()

    print("And fill in the valid email field")
    check_out_page.fill_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    check_out_page.fill_valid_adress()

    print("And add an invalid card number")
    check_out_page.add_credit_card("1111424242424242")

    print("And click on 'Complete purchase'")
    check_out_page.click_complete_purchase()

    print("Then they should see a message with 'Tarjeta de crédito no válida'")
    check_out_page.verify_message_invalid_card()


def test_checkout_without_card_details(page: Page):

    products_page = ProductsPage(page)
    check_out_page = CheckoutPage(page)
    shopping_cart_page = ShoppingcartPage(page)

    print("When the user enters to the products page")
    products_page.open_products_page()

    print("When they filter by name 'palas'")
    products_page.filter_by_name("Palas")

    print("And add the product to the cart")
    products_page.adds_product_to_cart("Juego de Palas")

    print("And visit the cart page")
    products_page.click_cart_page()

    print("And click on 'Proceed to checkout'")
    shopping_cart_page.click_proceed_to_check_out()

    print("When they fill in the valid name field 'Maria Diaz'")
    check_out_page.fill_valid_name_field()

    print("And fill in the valid email field")
    check_out_page.fill_valid_email_field()

    print("And fill in the valid adress 'Calle Aragón, 25, Madrid'")
    check_out_page.fill_valid_adress()

    print("And click on 'Complete purchase'")
    check_out_page.click_complete_purchase()
    
    print("Then the user should remain on the checkout page and the page URL should be 'https://web-qa.dev.adalab.es/checkout'")
    check_out_page.verify_remain_checkout_page_and_url_checkout()

    