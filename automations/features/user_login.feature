@login
Feature: Login de Usuario
  Como un usuario registrado
  Quiero poder iniciar sesión en la plataforma
  Para acceder a mis funcionalidades

Background:

    Given el usuario está en la página inicio del login

Scenario: Iniciar sesión con datos válidos
    When ingresa su email y contraseña correctos
    And hace clic en "Iniciar sesión"
    Then el sistema debe redirigir al usuario a la página principal
    And debe mostrar el nombre del usuario en la parte superior "Sebastian felipe Sebastian"

Scenario: Validar que el formulario no se envíe con campos incompletos
    When deja el campo email o contraseña vacío
    And se dirige a darle click a "Iniciar sesion"
    Then el sistema debe mostrar un mensaje de error indicando que los campos son obligatorios
@12
Scenario: Cerrar sesión correctamente
    When el usuario se loguea en la plataforma
    When hace clic en "Cerrar sesión"
    When el sistema debe cerrar la sesión
    When redirigir al usuario a la página de login
