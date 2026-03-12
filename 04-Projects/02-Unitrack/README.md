# UniTrack – Sistema de Control de Asistencia

Sistema web para el **registro y control de asistencia universitaria**, desarrollado con **Python y Flask**.
La aplicación permite gestionar el acceso de **estudiantes, docentes, trabajadores y administradores**, registrando automáticamente las **entradas y salidas** en una base de datos segura.

Este proyecto fue desarrollado como parte de un **proyecto universitario**, con el objetivo de convertirse en un **producto real escalable**.

---

# Universidad

**Universidad Politécnica de Baja California (UPBC)**

Programa:
Ingeniería en Tecnologías de la Información e Innovación Digital

---
Año: **2026**
---

# Objetivo del Proyecto

El objetivo principal del sistema es **mejorar la seguridad institucional** y **automatizar el control de asistencia**, reemplazando métodos manuales o sistemas poco integrados.

El sistema permite:

* Registrar usuarios
* Autenticar accesos
* Controlar entradas y salidas
* Administrar usuarios
* Supervisar asistencia en tiempo real

---

# Tecnologías Utilizadas

## Backend

* Python
* Flask
* SQLAlchemy
* Flask-Login
* Werkzeug Security (Password Hashing)

## Frontend

* HTML5
* CSS3
* Bootstrap 5

## Base de Datos

* SQLite (versión actual)
* Preparado para migración futura a **PostgreSQL**

---

# Arquitectura del Sistema

El sistema sigue una arquitectura **Web Application** basada en Flask.

Componentes principales:

Backend

* Flask Application Server
* SQLAlchemy ORM
* Authentication System
* Role-Based Access Control (RBAC)

Frontend

* HTML Templates
* CSS Styling
* Bootstrap Responsive Layout

Database

* SQLite local database

---

# Estructura del Proyecto

```
Unitrack/
│
├── app.py
├── unitrack.db
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       ├── background.png
│       └── logo.png
│
└── venv/
```

---

# Funcionalidades del Sistema

## Registro de Usuarios

Los usuarios pueden registrarse con la siguiente información:

* Nombre(s)
* Apellido(s)
* Nombre de usuario
* Contraseña
* Confirmación de contraseña
* CURP
* Fotografía
* Número de celular (opcional)
* Correo electrónico (opcional)
* Rol de usuario

Roles disponibles:

* Estudiante
* Docente
* Trabajador
* Administrativo (requiere validación)

---

# Sistema de Validación Administrativa

Para registrar cuentas **administrativas**, el sistema requiere un:

**Código de Validación del Administrador**

Proceso:

1. Usuario introduce el código
2. Presiona botón **Validar**
3. Si el código es correcto:

   * El botón se vuelve **verde**
   * El rol administrativo se habilita
4. Si el código es incorrecto:

   * El botón se vuelve **rojo**
   * El registro no se permite

Esto añade una **capa adicional de seguridad**.

---

# Sistema de Asistencia

Los usuarios autenticados pueden registrar:

* **Entrada (Check-In)**
* **Salida (Check-Out)**

El sistema guarda automáticamente:

* Fecha
* Hora de entrada
* Hora de salida

Cada registro se almacena en la base de datos.

---

# Panel de Usuario

Cada usuario accede a un panel con:

* Nombre completo
* Estado (Activo / Inactivo)
* Fotografía
* Tipo de usuario
* Historial de asistencia

Acciones disponibles:

* Registrar Entrada
* Registrar Salida
* Ver historial
* Cambiar configuración
* Cerrar sesión

---

# Panel de Administrador

El administrador tiene acceso a funciones avanzadas:

* Ver todos los usuarios registrados
* Ver estudiantes
* Ver docentes
* Ver trabajadores
* Generar códigos de validación
* Activar / desactivar usuarios
* Consultar historial de asistencia
* Configuración del sistema

---

# Seguridad del Sistema

El sistema implementa varias medidas de seguridad:

* Contraseñas almacenadas con **hash**
* Validación de campos obligatorios
* Control de acceso por roles
* Protección contra múltiples registros simultáneos
* Sistema de validación para cuentas administrativas

Reglas de contraseña:

* Mínimo 8 caracteres
* 1 letra mayúscula
* 1 letra minúscula
* 1 número
* 1 carácter especial

---

# Flujo del Sistema

1. Administrador inicia sesión
2. Cambio obligatorio de credenciales
3. Generación de códigos de validación
4. Registro de usuarios
5. Inicio de sesión
6. Acceso según rol
7. Registro de asistencia (Entrada / Salida)

---

# Instalación del Proyecto

### 1. Clonar el repositorio

```
git clone https://github.com/your-repository/unitrack.git
```

### 2. Crear entorno virtual

```
python -m venv venv
```

### 3. Activar entorno virtual

Windows:

```
venv\Scripts\activate
```

### 4. Instalar dependencias

```
pip install flask
pip install flask-sqlalchemy
pip install flask-login
pip install flask-migrate
pip install werkzeug
```

### 5. Ejecutar la aplicación

```
python app.py
```

Luego abrir en el navegador:

```
http://127.0.0.1:5000
```

---

# Mejoras Futuras

* Migración a **PostgreSQL**
* Sistema de **códigos QR para identificación**
* Dashboard con **estadísticas de asistencia**
* Exportación de reportes (PDF / Excel)
* API REST para aplicación móvil
* Despliegue en servidor cloud
* Notificaciones automáticas

---

# Posible Uso Comercial

Este sistema está diseñado para evolucionar hacia un **producto real** que pueda ser utilizado por:

* Universidades
* Institutos
* Centros educativos
* Empresas

---

# Licencia

Proyecto desarrollado con fines **académicos y educativos**.

---

# Contacto
Numero Cellular : +526865090453
Whatsaap: +526865090453
Autor: **Peyman Miyandashti**
Universidad Politécnica de Baja California
Ingeniería en Tecnologías de la Información e Innovación Digital
Facebook : https://www.facebook.com/Peyman.Miyandashti 
Language :English , Persian , Spanish , turkish, 
