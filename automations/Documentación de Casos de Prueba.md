## Resumen del Repositorio

Este repositorio incluye:
- Documentación detallada de los casos de prueba diseñados para el registro e inicio de sesión de usuarios.
- Scripts automatizados para la ejecución de pruebas utilizando Selenium y Docker.
- Reportes generados automáticamente en formato HTML, disponibles en la carpeta `outputs` tras la ejecución de las pruebas.

## Herramientas y Versiones Utilizadas
- **Python:** Versión 3.7 o superior.
- **Selenium:** Última versión disponible en el archivo `requirements.txt`.
- **Docker:** Para la configuración de entornos de prueba consistentes.
- **Docker Compose:** Para orquestar los contenedores necesarios.
- **Behave:** Para la implementación de pruebas BDD (Behavior-Driven Development).

# Casos de Prueba - Registro y Login de Usuario

## **TC001 - Registro de Usuario con Datos Válidos**
**Descripción:** Validar que el sistema permita registrar un usuario exitosamente con datos válidos.

**Precondiciones:** La base de datos no debe contener emails duplicados.

**Pasos a seguir:**
1. Abrir el formulario de registro.
2. Ingresar el nombre "Sebastian".
3. Ingresar el email "sebastian@example.com".
4. Ingresar la contraseña "Password123!".
5. Confirmar la contraseña con "Password123!".
6. Presionar el botón "Registrar".

**Datos de Prueba:**
- Nombre: Sebastian 
- Email: sebastian@example.com  
- Contraseña: Password123!

**Resultado esperado:** El usuario es registrado exitosamente y mostrara una alerta de usuario creado existosamente.

---

## **TC002 - Validación de Nombre en Registro**
**Descripción:** Validar que el campo de nombre acepte mínimo 2 palabras (nombre y apellido).

**Precondiciones:** El formulario debe estar abierto.

**Pasos a seguir:**
1. Abrir el formulario de registro.
2. Ingresar "Sebastian" en el campo de nombre.
3. Completar los demás campos con datos válidos.
4. Intentar enviar el formulario.

**Datos de Prueba:**
- Nombre: Sebastian

**Resultado esperado:** El sistema muestra un mensaje de error indicando que el campo de nombre debe contener al menos 2 palabras.

---

## **TC003 - Validación de Formato de Email en Registro**
**Descripción:** Verificar que el sistema valide el formato estándar de email.

**Precondiciones:** El formulario debe estar abierto.

**Pasos a seguir:**
1. Abrir el formulario de registro.
2. Ingresar "Sebastian.perez.com" en el campo de email.
3. Completar los demás campos con datos válidos.
4. Intentar enviar el formulario.

**Datos de Prueba:**
- Email: Sebastian.perez.com

**Resultado esperado:** El sistema muestra un mensaje de error indicando que el email no es válido.

---

## **TC004 - Validación de Contraseña en Registro**
**Descripción:** Validar que la contraseña cumpla con los requisitos de longitud y caracteres.

**Precondiciones:** El formulario debe estar abierto.

**Pasos a seguir:**
1. Abrir el formulario de registro.
2. Ingresar una contraseña de menos de 8 caracteres (por ejemplo, "abc123").
3. Completar los demás campos con datos válidos.
4. Intentar enviar el formulario.

**Datos de Prueba:**
- Contraseña: abc123

**Resultado esperado:** El sistema muestra un mensaje de error indicando que la contraseña no cumple con los requisitos.

---

## **TC005 - Validación de Contraseñas No Coincidentes**
**Descripción:** Verificar que el sistema valide si las contraseñas ingresadas no coinciden.

**Precondiciones:** El formulario debe estar abierto.

**Pasos a seguir:**
1. Abrir el formulario de registro.
2. Ingresar "Password123!" en el campo de contraseña.
3. Ingresar "Password456!" en el campo de confirmación de contraseña.
4. Completar los demás campos con datos válidos.
5. Intentar enviar el formulario.

**Datos de Prueba:**
- Contraseña: Password123!  
- Confirmación de contraseña: Password456!

**Resultado esperado:** El sistema muestra un mensaje de error indicando que las contraseñas no coinciden.

---

## **TC006 - Login con Credenciales Válidas**
**Descripción:** Verificar que el usuario pueda loguearse con el email y contraseña correctos.

**Precondiciones:** El usuario debe estar registrado previamente.

**Pasos a seguir:**
1. Abrir el formulario de login.
2. Ingresar el email "Sebastian.perez@example.com".
3. Ingresar la contraseña "Password123!".
4. Presionar el botón "Login".

**Datos de Prueba:**
- Email: Sebastian.perez@example.com  
- Contraseña: Password123!

**Resultado esperado:** El usuario accede a la plataforma y se muestra su nombre en la página principal.

---

## **TC007 - Validación de Campos Vacíos en Login**
**Descripción:** Validar que el formulario de login no se envíe si los campos no están completos.

**Precondiciones:** El formulario de login debe estar abierto.

**Pasos a seguir:**
1. Abrir el formulario de login.
2. Ingresar "Sebastian.perez@example.com" en el campo de email y dejar la contraseña vacía.
3. Intentar enviar el formulario.

**Datos de Prueba:**
- Email: Sebastian.perez@example.com  
- Contraseña: (vacío)

**Resultado esperado:** El sistema muestra un mensaje de error indicando que todos los campos son obligatorios.

---

## **TC008 - Logout de Usuario**
**Descripción:** Verificar que el usuario pueda cerrar sesión correctamente.

**Precondiciones:** El usuario debe estar logueado.

**Pasos a seguir:**
1. Iniciar sesión con credenciales válidas.
2. Hacer clic en el botón "Cerrar sesión".

**Resultado esperado:** El usuario es redirigido a la página de login y su sesión queda cerrada.
