import os
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from colorama import Fore
from allure_commons.types import AttachmentType

class global_function:
    def __init__(self, driver, evidence_path):
        self.driver = driver
        self.evidence_path = evidence_path

    def select_element_xpath(self, element, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, element)))
        except TimeoutException as e:
            self.attach_screenshot_to_report("error_message_timeout")
            raise e

    def select_element_id(self, element, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, element)))
        except TimeoutException as e:
            self.attach_screenshot_to_report("error_message_timeout")
            raise e

    def click(self, selector_type, selector_name, timeout=10):
        selectors = {
            "xpath": self.select_element_xpath,
            "id": self.select_element_id,
        }

        selector_method = selectors.get(selector_type)
        if selector_method:
            try:
                if selector_type == "xpath":
                    WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, selector_name)))
                elif selector_type == "id":
                    WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.ID, selector_name)))

                element = selector_method(selector_name, timeout)
                element.click()

            except (TimeoutException, NoSuchElementException) as ex:
                print(Fore.RED + f"----- Error al encontrar o hacer click en el elemento {selector_name} ({selector_type}): {str(ex)}" + Fore.RESET)
                self.attach_screenshot_to_report(name=f"click_error_{selector_name}")
                raise ex
            except Exception as ex:
                print(Fore.RED + f"----- Error desconocido al intentar hacer click en el elemento {selector_name}: {str(ex)}" + Fore.RESET)
                self.attach_screenshot_to_report(name=f"click_error_{selector_name}")
                raise ex
        else:
            print(Fore.RED + f"----- Tipo de selector inválido: {selector_type}" + Fore.RESET)

    def text(self, selector_type, selector_name, input_text, timeout=10):
        selectors = {
            "xpath": self.select_element_xpath,
            "id": self.select_element_id,
        }

        selector_method = selectors.get(selector_type)
        if selector_method:
            try:
                element = selector_method(selector_name, timeout)
                if element:
                    element.clear()
                    element.send_keys(input_text)
                else:
                    raise NoSuchElementException(f"Could not find element {selector_name} ({selector_type})")

            except (TimeoutException, NoSuchElementException) as ex:
                print(Fore.RED + f"----- Error al encontrar o interactuar con el elemento {selector_name} ({selector_type}): {str(ex)}" + Fore.RESET)
                self.attach_screenshot_to_report(name=f"text_error_{selector_name}")
                raise ex
            except Exception as ex:
                print(Fore.RED + f"----- Error desconocido al interactuar con el elemento {selector_name}: {str(ex)}" + Fore.RESET)
                self.attach_screenshot_to_report(name=f"text_error_{selector_name}")
                raise ex
        else:
            print(Fore.RED + f"----- Tipo de selector inválido: {selector_type}" + Fore.RESET)
            
    def message_matches(self, expected_message, xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            message = element.text
            if message == expected_message:
                return True
            else:
                self.attach_screenshot_to_report("error_message_mismatch")
                raise AssertionError(f"The message does not match. Expected: '{expected_message}', Actual: '{message}'")
        except TimeoutException as e:
            self.attach_screenshot_to_report("error_message_timeout")
            raise e

    def attach_screenshot_to_report(self, name="screenshot"):
        try:
            screenshot_path = os.path.join(self.evidence_path, f"{name}.png")
            self.driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name=name, attachment_type=AttachmentType.PNG)
        except TimeoutException as ex:
            print(Fore.RED + "-----Failed to attach screenshot to report: " + str(ex) + Fore.RESET)
            raise ex
