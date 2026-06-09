from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage


def test_submit_form_empty_required_message(page: Page):
    contact_page = ContactPage(page)
    print("Given the user is on the contact page: Contáctanos | Vida Verde")
    contact_page.open_contact_page()
    
    print("When they fill in the required name field")
    contact_page.fill_contact_name("Marta Diaz")
    
    print("And they fill in the required email field")
    contact_page.fill_contact_email("test@gmail.com")
    
    print("And they click on submit")
    contact_page.press_send_contact()
    
    print("Then they should see an error message: El mensaje es obligatorio")
    contact_page.verify_message_error("El mensaje es obligatorio")



def test_form_with_required_name_field_left_empty(page: Page):
    contact_page = ContactPage(page)
    print("Given the users enters contact page 'Contact| Vida Verde'")
    contact_page.open_contact_page()

    print ("fills required email with 'test@gmail.com'")
    contact_page.fill_contact_email("test@gmail.com")
   
    print ("fills required message with 'test mesage'")
    contact_page.fill_contact_message("test mensaje")

    print ("clicks send")
    contact_page.press_send_contact()

    print ("user should see the error message 'name is mandatory'")
    contact_page.verify_message_form("El nombre es obligatorio")

#Yohana
   
def test_empty_email_field_confirmation(page: Page):
    print("Given the user is on the contact page Contáctanos | Vida Verde  with the email field empty")
    contact_page = ContactPage(page)
    contact_page.open_contact_page()
    
    print("When the user fills the required fields name with 'Marta Diaz'")
    contact_page.fill_contact_name("Marta Diaz")
    
    print("And the user fills the required fields message")
    contact_page.fill_contact_message("Test")

    print("And the user  click on the button 'Enviar Mensaje'")
    contact_page.press_send_contact()
    
    print("Then the error message is displayed: El email es obligatorio ")
    contact_page.verify_message_form("El email es obligatorio")
    

def test_submit_form_with_invalid_emails(page: Page):
    print("Given the user is on the contact page Contáctanos | Vida Verde")
    contact_page = ContactPage(page)
    contact_page.open_contact_page()

    print("When the user fills the required fields name whith 'Marta Diaz'")
    contact_page.fill_contact_name("Marta Diaz")

    print("and the user fills the required fields whith an invalid email")
    contact_page.fill_contact_email("email")

    print("and the user fills the required fields test messaje with 'Test mensaje'")
    contact_page.fill_contact_message("Test mensaje")

    print("And the user  click on the button 'Enviar Mensaje'")
    contact_page.press_send_contact()

    print("Then the error message is displayed: El email no es válido")
    contact_page.verify_message_error("El email no es válido")
    

def test_submit_forms_with_valid_required_fields(page: Page):
    print("Given the user is on the contact page Contáctanos | Vida Verde")
    contact_page = ContactPage(page)
    contact_page.open_contact_page()

    print("When the user fills Fill in the name with 'Marta Diaz'")
    contact_page.fill_contact_name("Marta Diaz")

    print("And fill in the email with 'test_automation@test.com'")
    contact_page.fill_contact_email("test_automation@test.com")

    print("And fill in the message with 'test mensaje'")
    contact_page.fill_contact_message("test mensaje")

    print("And click on the button 'Enviar Mensaje'")
    contact_page.press_send_contact()

    print ("Then the user should see the confirmation message: ¡Mensaje enviado con éxito!")
    contact_page.verify_message_form("¡Mensaje enviado con éxito!")    
    
