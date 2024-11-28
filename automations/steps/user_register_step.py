from data.config import settings 
from behave import given, when, then
from framework.webapp import WebApp
from pages.user_register_page import user_register_page


@given(u'el usuario está en la página de registro')
def step_impl(context):
    web_app = WebApp(context.driver,context.evidence_path)
    driver = web_app.get_driver()
    web_app.load_website()
    driver = web_app.get_driver()
    context.register = user_register_page(driver,context.evidence_path)
    context.register.click_sign_up("xpath","//a[normalize-space()='Sign up']")


@when(u'completa el formulario con nombre, email y contraseña válidos')
def step_impl(context):
    context.register.valid_input("id","full-name","Sebastian Palencia")
    context.register.valid_input("id","email","sebastianfelipepalencia@gmail.com")
    context.register.valid_input("xpath","//input[@id='password']","Pruebas123*")
    context.register.valid_input("xpath","//input[@id='confirm-password']","Pruebas123*")

@when(u'hace clic en "Registrar"')
def step_impl(context):
    context.register.click_sign_up("xpath","//button[normalize-space()='Sign up']")


@then(u'el sistema debe registrar al usuario exitosamente')
def step_impl(context):
    context.register.detected_alert("Successful registration!","(//div[@class='ml-3 text-sm font-normal'])[1]")
#####


@when(u'ingresa un nombre con menos de 2 palabras')
def step_impl(context):
    context.register.valid_input("id","full-name","Sebastian")



@then(u'el sistema debe mostrar un mensaje de error indicando que el nombre no es válido')
def step_impl(context):
    context.register.detected_alert("Minimo dos palabras por nombre","//span[@class='label-text-alt text-error']")

####



@when(u'ingresa un email en formato incorrecto')
def step_impl(context):
    context.register.valid_input("id","email","esto no es un correo")



@then(u'el sistema debe mostrar un mensaje de error indicando que el email no es válido')
def step_impl(context):
    context.register.detected_alert("El crreo no cumple con el formato requerido","//span[@class='label-text-alt text-error']")


####


@when(u'ingresa un email ya registrado')
def step_impl(context):
    context.register.valid_input("id","full-name","Sebastian Palencia")
    context.register.valid_input("id","email","sebastianfelipepalencia@gmail.com")
    context.register.valid_input("xpath","//input[@id='password']","Pruebas123*")
    context.register.valid_input("xpath","//input[@id='confirm-password']","Pruebas123*")




@then(u'el sistema debe mostrar un mensaje de error indicando que el email ya está en uso')
def step_impl(context):
    context.register.detected_alert("Email registrado previamente","(//div[@class='ml-3 text-sm font-normal'])[1]")


####


@when(u'ingresa una contraseña que no cumple con los requisitos')
def step_impl(context):
    context.register.valid_input("id","full-name","Sebastian Palencia")
    context.register.valid_input("id","email","sebastianfelipepalencia@gmail.com")
    context.register.valid_input("xpath","//input[@id='password']","a*")


@then(u'el sistema debe mostrar un mensaje de error indicando los requisitos de la contraseña')
def step_impl(context):
    context.register.detected_alert("La contraseña debe tener al menos 8 caracteres, incluyendo una mayúscula, una minúscula, un número y un carácter especia","//span[@class='label-text-alt text-error']")

####



@when(u'ingresa una contraseña en los campos "Contraseña" y "Confirmar Contraseña" que no coinciden')
def step_impl(context):
    context.register.valid_input("xpath","//input[@id='password']","Pruebas*")
    context.register.valid_input("xpath","//input[@id='confirm-password']","Pruebas123*")




@then(u'el sistema debe mostrar un mensaje de error indicando que las contraseñas no coinciden')
def step_impl(context):
    context.register.detected_alert("Passwords do not match","//span[@class='label-text-alt text-error']")


####



@when(u'deja campos obligatorios vacíos')
def step_impl(context):
    pass




@then(u'el sistema debe mostrar un mensaje indicando que todos los campos son obligatorios')
def step_impl(context):
    context.register.detected_alert("Todos los campos estan vacios","//span[@class='label-text-alt text-error']")



