# Proyecto Final Django - Coderhouse

Aplicación web estilo **blog** desarrollada en **Python + Django**, con sistema de usuarios, perfiles, páginas tipo post y mensajería interna entre usuarios.

Proyecto realizado como **Entrega Final** del curso de Python en Coderhouse.

---

## 🚀 Funcionalidades principales

- Página de inicio
- Página **About**
- Sistema de registro, login y logout
- Perfiles de usuario con:
  - nombre
  - apellido
  - avatar
  - biografía
  - fecha de registro
- CRUD completo de páginas (posts):
  - listado
  - detalle
  - crear
  - editar
  - eliminar
- Editor de texto enriquecido (**CKEditor**)
- Carga de imágenes
- Sistema de mensajería interna:
  - inbox
  - enviados
  - detalle del mensaje
  - mensajes no leídos
- Panel de administración de Django
- Herencia de templates y navbar global

---

## 🧭 Rutas principales para probar

### Públicas
- `/` → Home
- `/about/` → Acerca de mí
- `/pages/` → Listado de páginas
- `/pages/<id>/` → Detalle de página

### Autenticación
- `/accounts/signup/` → Registro de usuario
- `/accounts/login/` → Login
- `/accounts/logout/` → Logout

### Perfil
- `/accounts/profile/` → Ver perfil
- `/accounts/profile/edit/` → Editar perfil
- `/accounts/password/` → Cambiar contraseña

### Páginas (requieren login)
- `/pages/create/` → Crear página
- `/pages/<id>/update/` → Editar página
- `/pages/<id>/delete/` → Eliminar página

### Mensajería (requiere login)
- `/messages/` → Inbox
- `/messages/send/` → Enviar mensaje
- `/messages/sent/` → Mensajes enviados
- `/messages/<id>/` → Detalle del mensaje

### Admin
- `/admin/`

---

## 🛠️ Instalación y ejecución local

### 1) Clonar el repositorio
```bash
git clone "https://github.com/matighigi/ProyectoFinal-Django-Ghigi"
cd ProyectoFinal-Django-Ghigi
```

### 2) Crear y activar entorno virtual
```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3) Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4) Ejecutar migraciones
```bash
python manage.py migrate
```

### 5) Crear superusuario
```bash
python manage.py createsuperuser
```

### 6) Levantar el servidor
```bash
python manage.py runserver
```

Abrir en el navegador:
```
http://127.0.0.1:8000/
```

---

## 📦 Tecnologías utilizadas

- Python 3
- Django
- SQLite
- Bootstrap
- CKEditor
- Pillow

---

## 🎥 Video demostración

El proyecto incluye un video demostación mostrando:
- Registro y login
- Perfil de usuario
- CRUD de páginas
- Mensajería interna
- Panel de administración

---

## 👤 Autor

**Matías Ghigi**  
Proyecto Final – Coderhouse
