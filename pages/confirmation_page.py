from playwright.sync_api import Page, expect

class ConfirmationPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/confirmation"
    

    def verify_message_purchase_completed_succesfully(self):
        expect(self.page.get_by_role("heading", name="¡Compra Realizada con Éxito!")).to_be_visible()

      
    def click_back_store(self):
        self.page.get_by_role("link", name="Volver a la Tienda").click()


    def verify_shopping_cart_summary(self, summary):
        expect(self.page.get_by_role("heading", name=summary)).to_be_visible()

    def verify_product_name(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def verify_shopping_cart_subtotal(self, subtotal):
        expect(self.page.get_by_text("Subtotal")).to_be_visible()
           
    def verify_products_iva(self, iva):
        expect(self.page.get_by_text("IVA (21%)"+iva)).to_be_visible()
               
    def verify_products_shipping_cost(self):            
        expect( self.page.locator("dt", has_text="Envío")).to_be_visible()
   
    def verify_products_total(self, total):
        expect(self.page.get_by_text(total)).to_be_visible()

