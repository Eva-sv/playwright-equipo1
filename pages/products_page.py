
from playwright.sync_api import Page, expect


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Catálogo de Productos"
        
    def open_products_page(self):
        self.page.goto(self.url)

    def verify_products_category(self, category):
        expect(self.page.get_by_text(category).nth(2)).to_be_visible()

    def verify_products_name(self,product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    def verify_products_price(self,price):
        expect(self.page.get_by_text(price)).to_be_visible()

    def verify_products_title(self):
        expect(self.page.locator("h1")).to_contain_text(self.title)

    def verify_products_url(self):
        expect(self.page).to_have_url(self.url)

    #def filter_by_palas(self):
        #self.page.get_by_role("searchbox", name="Nombre").fill("palas")

   # def click_product_to_the_cart(self):
        # self.page.get_by_role("button", name="Añadir Juego de Palas al").click()

    def click_cart_page(self):
        self.page.get_by_role("link", name="Carrito de compra").click()


    #lucia
    #def navigate(self):
        #self.page.goto("https://web-qa.dev.adalab.es/products")

    def filter_by_name(self, name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

    def filter_by_category(self, category):
        self.page.get_by_label("Categoría").select_option(category)

    def filter_by_min_price(self, min_price):
        self.page.get_by_role("spinbutton",name="Precio mínimo").fill(min_price)

    def filter_by_max_price(self, max_price):
        self.page.get_by_role("spinbutton",name="Precio máximo").fill(max_price)

    def filter_by_name(self, name):
        self.page.get_by_role("searchbox", name="Nombre").fill(name)

    def get_no_results_message(self, text_message):
        expect(self.page.get_by_text(text_message)).to_be_visible()
        

    #Yohana
    def clear_filters(self):
        self.page.get_by_role("button", name="Quitar filtros").click()

    def adds_product_to_cart(self, product_name):
        self.page.get_by_role("button", name=f"Añadir {product_name} al carrito").click()
        
    
 
    def verify_filtered_product(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()
    