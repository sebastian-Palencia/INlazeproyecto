
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from framework.webapp import WebApp
from data.config import settings


def before_scenario(context, scenario):
    try:
        # URL del hub remoto de Selenium Grid
        grid_url = 'http://localhost:4444/wd/hub'

        # Configurar opciones del navegador
        if settings['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-gpu')
            driver = webdriver.Remote(
                command_executor=grid_url,
                desired_capabilities=DesiredCapabilities.CHROME.copy(),
                options=options
            )
        elif settings['browser'] == 'firefox':
            driver = webdriver.Remote(
                command_executor=grid_url,
                desired_capabilities=DesiredCapabilities.FIREFOX.copy()
            )
        else:
            # Navegador por defecto
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-gpu')
            driver = webdriver.Remote(
                command_executor=grid_url,
                desired_capabilities=DesiredCapabilities.CHROME.copy(),
                options=options
            )

        # Aumentar el tiempo de espera para los comandos
        driver.implicitly_wait(10)  # Tiempo de espera implícito de 10 segundos
        driver.set_script_timeout(30)  # Tiempo de espera para ejecutar scripts de 30 segundos

        
        # Inicializar la aplicación web
        context.driver = driver
        evidence = context.evidence_path
        context.app = WebApp(context.driver,evidence)
    except Exception as ex:
        print("{}".format(ex))



def after_scenario(context, scenario):
    print("Executing after_scenario()")

    if hasattr(context, 'driver'):
        try:
            # Capturar logs del navegador si hay algún error
            if scenario.status == 'failed':
                logs = context.driver.get_log('browser')
                for entry in logs:
                    print(f"Log entry: {entry}")

            # Cerrar el navegador
            context.driver.quit()
        except Exception as e:
            print(f"Error closing the browser: {e}")
    else:
        print("Error: context.driver is not defined")
