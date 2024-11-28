@register
Feature: Registro de Usuario
  Como un usuario
  Quiero poder registrarme en la plataforma
  Para acceder a sus funcionalidades

Background:

    Given el usuario está en la página de registro

Scenario: Registrar usuario con datos válidos
    When completa el formulario con nombre, email y contraseña válidos
    And hace clic en "Registrar"
    Then el sistema debe registrar al usuario exitosamente


Scenario: Validar que el campo nombre acepte mínimo 2 palabras
    When ingresa un nombre con menos de 2 palabras
    Then el sistema debe mostrar un mensaje de error indicando que el nombre no es válido


Scenario: Validar que el email tenga un formato estándar
    When ingresa un email en formato incorrecto
    Then el sistema debe mostrar un mensaje de error indicando que el email no es válido


Scenario: Verificar que el email sea único
    When ingresa un email ya registrado
    When hace clic en "Registrar"
    Then el sistema debe mostrar un mensaje de error indicando que el email ya está en uso


Scenario: Validar que la contraseña cumpla con los requisitos
    When ingresa una contraseña que no cumple con los requisitos
    Then el sistema debe mostrar un mensaje de error indicando los requisitos de la contraseña

Scenario: Comprobar que el formulario no se envíe con campos incompletos
    When deja campos obligatorios vacíos
    And hace clic en "Registrar"
    Then el sistema debe mostrar un mensaje indicando que todos los campos son obligatorios

Scenario: Verificar que el sistema informe si las contraseñas no coinciden
    When ingresa una contraseña en los campos "Contraseña" y "Confirmar Contraseña" que no coinciden
    Then el sistema debe mostrar un mensaje de error indicando que las contraseñas no coinciden
