from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.shopping_cart_page import ShoppingcartPage

def test_add_products_to_cart_view_summary_and_empty_cart(page: Page):
    products_page = ProductsPage(page) 
    shopping_cart_page = ShoppingcartPage(page)

    print("Given user visit the page 'Productos | Vida Verde'")
    products_page.open_products_page()
   
    print("when the user filters by name 'Sansevieria'")
    products_page.filter_by_name("Sansevieria")    

    print("And the user clicks on the add to cart button")
    products_page.adds_product_to_cart("Sansevieria")

    print("And the user clean the filters and see all the products") 
    products_page.clear_filters()
    
    print("And the user adds the Maceta de Barro Grande to the cart")
    products_page.filter_by_name("maceta de barro")
    
    print("And the user clicks on the add to cart button")
    products_page.adds_product_to_cart("Maceta de Barro Grande")

    print("And the user clicks on the shopping cart link")
    products_page.click_cart_page()

    print("And the user sees the Shopping Cart page")    
    shopping_cart_page.open_shopping_cart_page()    

    print("Then the user should see the shopping cart summary with the products added")
    shopping_cart_page.verify_shopping_cart_by_product_name("Sansevieria")
    shopping_cart_page.verify_shopping_cart_by_product_category("Plantas")
    shopping_cart_page.verify_shopping_cart_by_product_price("22.00")

    shopping_cart_page.verify_shopping_cart_by_product_name("Maceta de Barro Grande")
    shopping_cart_page.verify_shopping_cart_by_product_category("Macetas")
    shopping_cart_page.verify_shopping_cart_by_product_price("10.50")
  
    shopping_cart_page.verify_shopping_cart_summary()

    print("And the user should see the products in the shopping cart summary with the price")
    shopping_cart_page.verify_products_in_shopping_cart_summary("Productos (2)32.50 €")  

    print("And the user should see the IVA in the shopping cart summary with the updated price")
    shopping_cart_page.verify_products_iva("6.83 €")

    print("And the user should see the shipping cost in the shopping cart summary")
    shopping_cart_page.verify_products_shipping_cost()

    print("And the user should see the total in the shopping cart summary with the updated price")
    shopping_cart_page.verify_products_total("Total44.33 €")
  
    
    print("When the user clicks on the empty cart button")
    shopping_cart_page.click_empty_cart_button()
    
    print("Then the user should see the message 'Tu carrito está vacío'")
    shopping_cart_page.verify_empty_cart_message()
    
  
def test_remove_products_from_cart_and_view_summary(page: Page):
    products_page = ProductsPage(page)
    shopping_cart_page = ShoppingcartPage(page)

    print("Given user visit the page 'Productos | Vida Verde'")
    products_page.open_products_page()
    
    print("when the user filters by name 'Ficus Lyrata'")
    products_page.filter_by_name("Ficus Lyrata")    
    
    print("And the user clicks on the add to cart button")
    products_page.adds_product_to_cart("Ficus Lyrata")
    
    print("And the user clean the filters and see all the products")    
    products_page.clear_filters()

    print("And the user filters by name 'Tijeras de Podar'")
    products_page.filter_by_name("tijeras")

    print("And the user clicks on the add to cart button")
    products_page.adds_product_to_cart("Tijeras de Podar")

    print("And the user clicks on the shopping cart link")
    products_page.click_cart_page()
       
    print("And the user clicks on the shopping cart link")
    
    shopping_cart_page.open_shopping_cart_page()    
    
    print("And the user removes the Ficus Lyrata from the cart")
    shopping_cart_page.remove_product_of_shopping_cart("Ficus Lyrata")

    print("Then the user should see the updated order summary ")
    shopping_cart_page.verify_shopping_cart_summary()

    print("And the user should see the products in the shopping cart summary with the updated price")
    shopping_cart_page.verify_products_in_shopping_cart_summary("Productos (1)18.50 €")  

    print("And the user should see the IVA in the shopping cart summary with the updated price")
    shopping_cart_page.verify_products_iva("3.88 €")

    print("And the user should see the shipping cost in the shopping cart summary")
    shopping_cart_page.verify_products_shipping_cost()

    print("And the user should see the total in the shopping cart summary with the updated price")
    shopping_cart_page.verify_products_total("Total27.38 €")




