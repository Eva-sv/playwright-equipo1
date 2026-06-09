from playwright.sync_api import Page, expect
from pages import contact_page
from pages.components.menu import Menu
from pages.home_page import HomePage
from pages.about_us_page import AboutusPage
from pages.products_page import ProductsPage
from pages.contact_page import ContactPage



def test_visit_menu_links(page: Page):
    home_page = HomePage (page)
    menu = Menu(page)
    about_us_page = AboutusPage(page)
    products_page = ProductsPage(page)
    contact_page = ContactPage(page)  


    print("Given the user enters the 'Vida Verde' page")
    home_page.open_home_page()

    print("Then they should see the title 'Vida Verde'")
    home_page.verify_home_page_title()

    print("When the user clicks on 'Quiénes Somos'")
    menu.visit_menu_about_us()

    print("Then they should see the tittle 'Quiénes Somos'")
    about_us_page.verify_about_us_title()

    print("And they should see the URL 'https://web-qa.dev.adalab.es/about'")
    about_us_page.verify_about_us_url()
    
    print("When the user clicks on 'Productos'")
    menu.visit_menu_products()

    print("Then they should see the tittle 'Catálogo de Productos'")
    products_page.verify_products_title()

    print("And they should see the URL 'https://web-qa.dev.adalab.es/products'")
    products_page.verify_products_url()

    print("When the user clicks on 'Contacto'")
    menu.visit_menu_contact()

    print("Then they should see the tittle 'Contáctanos'")
    contact_page.verify_contact_title()
    

    print("And they should see the URL 'https://web-qa.dev.adalab.es/contact'")
    contact_page.verify_contact_url()








    


   
 




