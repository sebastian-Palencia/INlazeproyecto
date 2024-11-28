from selenium.common.exceptions import TimeoutException
from pages.global_functions import global_function
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from data.config import settings 
from colorama import Fore
class user_login_page:

    def __init__(self, driver, evidence_path):
        self.driver = driver
        self.evidence_pathh = evidence_path
        self.global_function = global_function(self.driver,self.evidence_pathh)
        self.wait = WebDriverWait(self.driver, 50)

    def click_login(self,selector,valor):
        try:
            self.global_function.click(selector,valor)
        except TimeoutException as e:
            print(Fore.RED + "----- Timeout when click sign up" + Fore.RESET)
            self.global_function.attach_screenshot_to_report(name="click_sign_up_timeout")
            raise TimeoutException("El boton no esta activo'Sign up'.") from e

    def valid_input(self,type,id,text):
        try:
            self.global_function.text(type,id,text)
        except TimeoutException as e:
            print(Fore.RED + "----- Timeout when going to the valid_input" + Fore.RESET)
            self.global_function.attach_screenshot_to_report(name="valid_input_page_timeout")
            raise TimeoutException("could not be found valid_input.") from e
        
    def detected_alert(self,message,element):
        try:
            self.global_function.message_matches(message,element)
        except TimeoutException as e:
            print(Fore.RED + "----- Time when going to the detected_alert" + Fore.RESET)
            self.global_function.attach_screenshot_to_report(name="detected_alert_page_timeout")
            raise TimeoutException(f"No se encontro el mensaje esperado {message}") from e
        
    def click_button_deactive(self, selector, valor):
        try:
            self.global_function.click(selector, valor)
            print(Fore.GREEN + "El botón estaba activo y se hizo clic con éxito." + Fore.RESET)
        except TimeoutException:
            print(Fore.YELLOW + "El botón no estaba activo, lo cual es el comportamiento esperado." + Fore.RESET)
            self.global_function.attach_screenshot_to_report(name="button_inactive_expected")
