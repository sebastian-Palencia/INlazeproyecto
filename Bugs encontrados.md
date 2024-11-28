# Casos de Prueba de Autenticación de Usuarios

## Casos de Prueba para Registro e Inicio de Sesión

### Errores Encontrados

#### Página de Inicio de Sesión
- **Falta de Indicadores de Error:**
  - Los campos carecen de etiquetas o mensajes de error que indiquen si el correo electrónico o la contraseña son incorrectos o requeridos.
  - **Entorno:** Navegador Chrome , Sistema Operativo Windows 10.
  - **Pasos para Reproducir:**
    1. Abrir la página de inicio de sesión.
    2. Intentar enviar el formulario con campos vacíos o datos incorrectos.
  - **Comportamiento Esperado:**
    - Deberían aparecer mensajes indicando que los campos son obligatorios o que los datos ingresados son incorrectos.
  - **Comportamiento Actual:**
    - No se muestra ningún mensaje de error.
- **Textos Placeholder:**
  - La plataforma muestra textos de relleno "Lorem Ipsum" en lugar de contenido significativo.
  - **Entorno:** Navegador Chrome, Sistema Operativo Windows 10.
  - **Pasos para Reproducir:**
    1. Navegar a la página de inicio de sesión.
    2. Observar los textos en los campos y botones.
  - **Comportamiento Esperado:**
    - Textos descriptivos claros que indiquen la funcionalidad de los elementos.
  - **Comportamiento Actual:**
    - Textos placeholder genéricos "Lorem Ipsum".

#### Página de Registro
- **Problemas de Validación:**
  - Los campos no validan la entrada más allá de comprobar si están vacíos.
  - Los campos de contraseña solo validan si las contraseñas coinciden, pero no muestran label informativos de  (por ejemplo, longitud mínima, letras mayúsculas, etc.).
  - **Entorno:** Navegador Chrome, Sistema Operativo Windows 10.
  - **Pasos para Reproducir:**
    1. Abrir la página de registro.
    2. Introducir datos incorrectos o no cumplir los requisitos de contraseña.
  - **Comportamiento Esperado:**
    - Validaciones claras para cada campo y guiar mejores practicas.
  - **Comportamiento Actual:**
    - El formulario solo verifica  si las contraseñas coinciden.
- **Manejo de Usuarios Duplicados:**
  - La plataforma no muestra errores para entradas de usuario duplicadas. En su lugar, indica erróneamente que el usuario fue creado con éxito, aunque el usuario anterior persiste.
  - **Entorno:** Navegador Chrome, Sistema Operativo Windows 10.
  - **Pasos para Reproducir:**
    1. Registrar un usuario con un correo electrónico ya existente.
    2. Observar el mensaje de éxito.
  - **Comportamiento Esperado:**
    - Mostrar un error indicando que el correo electrónico ya está registrado.
  - **Comportamiento Actual:**
    - Se muestra un mensaje de éxito, pero no se registra un nuevo usuario.

#### Funcionalidad de la Plataforma
- **Botones No Funcionales:**
  - Ninguno de los botones funciona excepto el botón de perfil.
  - El botón de perfil abre un menú desplegable (elemento select), pero solo la opción de cerrar sesión funciona correctamente.
  - Las demás opciones del menú no funcionan y muestran textos placeholder "Lorem Ipsum".
  - **Entorno:** Navegador Chrome, Sistema Operativo Windows 10.
  - **Pasos para Reproducir:**
    1. Iniciar sesión en la plataforma.
    2. Intentar utilizar los botones de la interfaz.
  - **Comportamiento Esperado:**
    - Todos los botones deberían ejecutar las acciones correspondientes.
  - **Comportamiento Actual:**
    - Solo el botón de cerrar sesión funciona; los demás no responden y tienen textos placeholder.
