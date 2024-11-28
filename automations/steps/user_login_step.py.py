from data.config import settings 
from behave import given, when, then
from framework.webapp import WebApp
from pages.user_login_page import user_login_page



@given(u'el usuario está en la página inicio del login')
def step_impl(context):
    web_app = WebApp(context.driver,context.evidence_path)
    driver = web_app.get_driver()
    web_app.load_website()
    driver = web_app.get_driver()
    context.login = user_login_page(driver,context.evidence_path)


@when(u'deja el campo email o contraseña vacío')
def step_impl(context):
    pass

@when(u'hace clic en "Iniciar sesión"')
def step_impl(context):
    context.login.click_login("xpath","//button[normalize-space()='Sign in']")
    
@when(u'se dirige a darle click a "Iniciar sesion"')
def step_impl(context):
    context.login.click_button_deactive("xpath","//button[normalize-space()='Sign in']")


@then(u'el sistema debe mostrar un mensaje de error indicando que los campos son obligatorios')
def step_impl(context):
    context.login.detected_alert("Todos los campos son obligatorios","(//div[@class='Error_alert'])")





@when(u'hace clic en "Cerrar sesión"')
def step_impl(context):
    context.login.click_login("xpath","//label[@class='btn btn-ghost btn-circle avatar']")
    context.login.click_login("xpath","//a[normalize-space()='Logout']")


@when(u'el sistema debe cerrar la sesión')
def step_impl(context):
    pass


@when(u'redirigir al usuario a la página de login')
def step_impl(context):
    context.login.detected_alert("Sign in","//h1[normalize-space()='Sign in']")




@when(u'ingresa su email y contraseña correctos')
def step_impl(context):
    context.login.valid_input("id","email","sebastianfelipepalencia@gmail.com")
    context.login.valid_input("xpath","//input[@id='password']","Pruebas123*")


@when(u'el usuario se loguea en la plataforma')
def step_impl(context):
    context.login.valid_input("id","email","sebastianfelipepalencia@gmail.com")
    context.login.valid_input("xpath","//input[@id='password']","Pruebas123*")
    context.login.click_login("xpath","//button[normalize-space()='Sign in']")

@then(u'el sistema debe redirigir al usuario a la página principal')
def step_impl(context):
    context.login.detected_alert("Welcome to Lorem","//h2[normalize-space()='Welcome to Lorem']")


@then(u'debe mostrar el nombre del usuario en la parte superior {name}')
def step_impl(context,name):
    name2 = name.strip('"')
    context.login.detected_alert(name2,f"//h2[normalize-space()='{name2}']")