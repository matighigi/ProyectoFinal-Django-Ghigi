# PyBlog – Proyecto Final Django (Coderhouse)

PyBlog es una aplicación web tipo blog desarrollada con **Python y Django** como Proyecto Final del curso de Python en **Coderhouse**.  
Permite a los usuarios registrarse, crear y administrar páginas con contenido enriquecido, gestionar su perfil y comunicarse mediante un sistema de mensajería interna.

---

## 🚀 Funcionalidades principales

### 🔐 Autenticación y cuentas
- Registro de usuarios (signup)
- Inicio y cierre de sesión (login / logout)
- Perfil de usuario con:
  - Avatar
  - Nombre y apellido
  - Biografía
  - Fecha de unión
- Edición de perfil
- Cambio de contraseña

### 📝 Páginas (Blog)
- Crear, listar, ver, editar y eliminar páginas
- Contenido enriquecido con **CKEditor**
- Imagen principal por página
- Fecha de creación automática
- Autor asociado a cada página
- **Solo el autor puede editar o eliminar su propia página**
- Listado con tarjetas y botón “Leer más”
- Mensaje “No hay páginas aún” cuando no existen registros

### 💬 Mensajería interna
- Envío de mensajes entre usuarios registrados
- Bandeja de entrada (Inbox)
- Bandeja de salida (Enviados)
- Indicador de mensajes leídos / no leídos
- Vista de detalle de cada mensaje

### 🎨 Diseño y experiencia de usuario
- Herencia de templates con `base.html`
- Navbar y footer consistentes en todo el sitio
- Bootstrap aplicado a **todos los formularios**
- Interfaz completamente en español
- Página de inicio con presentación del proyecto
- Página “Acerca de” accesible desde el footer

---

## 🗂️ Estructura del proyecto

~~~text
ProyectoFinal-Django-Ghigi/
│
├── accounts/        # Autenticación y perfiles
├── pages/           # Blog / Páginas
├── messenger/       # Mensajería interna
├── core/            # Utilidades comunes (forms)
├── templates/       # Templates HTML
├── static/          # Archivos estáticos
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
~~~

---

## ⚙️ Instalación y ejecución

### 1️⃣ Clonar el repositorio
~~~bash
git clone https://github.com/matighigi/ProyectoFinal-Django-Ghigi.git
cd ProyectoFinal-Django-Ghigi
~~~

### 2️⃣ Crear y activar entorno virtual
**Windows**
~~~bash
python -m venv .venv
.venv\Scripts\activate
~~~

**Linux / Mac**
~~~bash
python3 -m venv .venv
source .venv/bin/activate
~~~

### 3️⃣ Instalar dependencias
~~~bash
pip install -r requirements.txt
~~~

### 4️⃣ Migraciones
~~~bash
python manage.py makemigrations
python manage.py migrate
~~~

### 5️⃣ Crear superusuario (admin)
~~~bash
python manage.py createsuperuser
~~~

### 6️⃣ Ejecutar servidor
~~~bash
python manage.py runserver
~~~

Abrir en el navegador:
~~~text
http://127.0.0.1:8000/
~~~

---

## 🧪 Orden sugerido de prueba (para el corrector)

1. Ingresar al sitio (Home)
2. Ir a **Registrarse** y crear un usuario
3. Iniciar sesión
4. Acceder al **Perfil** y editar datos (avatar y bio)
5. Ir a **Páginas**
6. Crear una nueva página con:
   - Título
   - Subtítulo
   - Contenido enriquecido
   - Imagen
7. Ver el listado y el detalle de la página (botón “Leer más”)
8. Editar y eliminar la página creada
9. Crear un segundo usuario (por ejemplo “marce”)
10. Probar permisos:
   - Ver páginas de otros ✅
   - **NO** editar/eliminar páginas ajenas ✅
11. Ir a **Mensajes** y enviar un mensaje a otro usuario
12. Ver Inbox y Enviados + abrir el detalle del mensaje
13. Cerrar sesión

---

## 📌 Requisitos de la consigna (cumplidos)

- ✅ Web Django estilo blog
- ✅ Admin de Django configurado y modelos registrados
- ✅ Rutas obligatorias visibles en navegación:
  - `/about/` (Acerca de)
  - `/pages/` (Listado)
- ✅ `/pages/` con listado + “Leer más” al detalle
- ✅ Mensaje “No hay páginas aún” cuando no hay registros
- ✅ CRUD completo del modelo principal
- ✅ Modelo principal con:
  - mínimo 2 `CharField`
  - texto enriquecido con **CKEditor**
  - imagen
  - fecha
- ✅ Permisos: editar/borrar solo usuario logueado y **solo autor**
- ✅ Mínimo 2 Class Based Views
- ✅ Mínimo 1 mixin en CBV y 1 decorador en view function
- ✅ App `accounts` con signup/login/logout
- ✅ Perfil (vista + edición + cambio de contraseña)
- ✅ App de mensajería funcional entre usuarios
- ✅ `.gitignore` correcto (**no** se sube `db.sqlite3` ni `media/`)
- ✅ `requirements.txt` actualizado
- ✅ README con orden de prueba

---

## 🎥 Video de demostración (máx. 10 min)

El video muestra:
- Registro y login
- Perfil (ver/editar, avatar y bio)
- Páginas (crear, listar, detalle, editar, eliminar)
- Permisos (un usuario no puede editar/borrar páginas de otro)
- Mensajería (enviar, inbox, enviados, detalle)
- Navegación general del sitio

---

## 👨‍💻 Autor

**Matías Ghigi**  
Proyecto Final – Curso Python (Django)  
Coderhouse – 2026
