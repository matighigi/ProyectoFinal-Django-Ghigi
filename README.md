# Proyecto Final Python (Django) – Coderhouse

Proyecto Final del curso de Python utilizando el framework Django.
Aplicación web tipo blog con autenticación, perfiles, CRUD de páginas, mensajería interna y panel de administración.

---

## Tecnologías utilizadas
- Python 3
- Django
- SQLite (solo en desarrollo local)
- HTML y CSS
- Bootstrap (opcional)
- CKEditor (texto enriquecido)

---

## Instalación y ejecución del proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/matighigi/ProyectoFinal-Django-Ghigi.git
cd ProyectoFinal-Django-Ghigi
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Mac / Linux:
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor
```bash
python manage.py runserver
```

Abrir en el navegador:
http://127.0.0.1:8000/

---

## Orden recomendado para probar la aplicación

### 1. Home
- `/` → Página principal

### 2. About
- `/about/` → Acerca de mí

### 3. Autenticación (accounts)
- `/accounts/signup/` → Registro de usuario
- `/accounts/login/` → Login
- `/accounts/logout/` → Logout

### 4. Páginas (Blog)
- `/pages/` → Listado de páginas  
  Si no hay páginas creadas, se muestra el mensaje: "No hay páginas aún"
- Desde el listado, botón "Leer más" al detalle
- `/pages/<id>/` → Detalle
- `/pages/create/` → Crear página (requiere login)
- `/pages/<id>/update/` → Editar página (requiere login)
- `/pages/<id>/delete/` → Eliminar página (requiere login)

El modelo principal incluye:
- Mínimo 2 campos CharField
- 1 campo de texto enriquecido (CKEditor)
- 1 imagen
- 1 fecha

---

### 5. Perfil de usuario
- `/accounts/profile/` → Ver perfil
- `/accounts/profile/edit/` → Editar perfil
- `/accounts/password/` → Cambio de contraseña

Datos del perfil:
- Nombre
- Apellido
- Email
- Avatar
- Bio u otros campos adicionales

---

### 6. Mensajería
Sistema de mensajería interna entre usuarios:
- `/messenger/` → Bandeja de mensajes
- `/messenger/new/` → Enviar mensaje
- `/messenger/<id>/` → Ver mensaje

---

## Panel de administración
- `/admin/`

Desde el panel de admin se gestionan:
- Usuarios
- Perfiles
- Páginas / Posts
- Mensajes

---

## Video demostración (máx. 10 minutos)
Link al video: (agregar link acá)

---

## Notas importantes
- El archivo db.sqlite3 NO se sube al repositorio.
- La carpeta media/ NO se sube al repositorio.
- Ambos están ignorados mediante .gitignore.
- Proyecto realizado como Entrega Final del curso de Python – Coderhouse.
