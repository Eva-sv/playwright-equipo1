from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

class ShoppingcartPage:
    def __init__(self, page: Page):
         self.page = page
         self.url = 'https://web-qa.dev.adalab.es/cart'
         
    
#EVA

    def click_proceed_to_check_out(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()

   # def verify_order_summary(self):
        #expect(self.page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()
        #expect(self.page.get_by_text("Juego de Palas15.99 €")).to_be_visible()
        #expect(self.page.get_by_text("Subtotal (1)15.99 €")).to_be_visible()
        #expect(self.page.get_by_text("IVA (21%)3.36 €")).to_be_visible()
        #expect(self.page.get_by_text("Envío5.00 €")).to_be_visible()
        #expect(self.page.get_by_text("Total24.35 €")).to_be_visible()

#Yohana
    def open_shopping_cart_page(self):
        self.page.goto(self.url)
    
    def verify_shopping_cart_by_product_name(self, product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    def verify_shopping_cart_by_product_category(self, category):
        expect(self.page.get_by_text(category)).to_be_visible()
    
    def verify_shopping_cart_by_product_price(self, price):
        expect(self.page.get_by_text(price)).to_be_visible()

    def verify_shopping_cart_subtotal(self, subtotal):
        expect(self.page.get_by_text("Subtotal")).to_be_visible()
    
    def verify_shopping_cart_summary(self):
        expect(self.page.get_by_role("heading", name="Resumen del Pedido")).to_be_visible()

    def verify_products_in_shopping_cart_summary(self, products):
        expect(self.page.get_by_text(products)).to_be_visible()
           
    def verify_products_iva(self, iva):
        expect(self.page.get_by_text("IVA (21%)"+iva)).to_be_visible()
               
    def verify_products_shipping_cost(self):            
        expect( self.page.locator("dt", has_text="Envío")).to_be_visible()
   
    def verify_products_total(self, total):
        expect(self.page.get_by_text(total)).to_be_visible()
          
    def click_empty_cart_button(self):
       self.page.get_by_role("button", name="Vaciar Carrito").click()
    
    def verify_empty_cart_message(self):
        expect(self.page.get_by_text("Tu carrito está vacío")).to_be_visible()

    def remove_product_of_shopping_cart(self, product_name):
        self.page.get_by_role("button", name=f"Eliminar {product_name} del carrito").click()
    
    def verify_removed_from_the_shopping_cart(self,product_name):
        expect(self.page.get_by_role("heading", name=product_name)).not_to_be_visible()

    

        