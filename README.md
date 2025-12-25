# TuPrimeraPagina+GHIGI

## Tercera Pre-Entrega – Curso Python – Coderhouse

Este proyecto corresponde a la tercera pre-entrega del curso Python de Coderhouse.  
Es una aplicación web desarrollada con **Django**, siguiendo el patrón **MVT**.

Incluye:

- Herencia de plantillas HTML  
- Tres modelos con formularios  
- Un formulario de búsqueda en base de datos  
- Proyecto completo y funcional  
- Subido a GitHub como se solicita  

---

## 🛠 Tecnologías utilizadas

- Python 3.10+
- Django 6.0
- HTML5
- SQLite

---

## 📁 Estructura del proyecto

```text
TuPrimeraPagina+GHIGI/
│
├── tuprimera_pagina/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── blog/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── blog/
│           ├── base.html
│           ├── inicio.html
│           ├── crear_autor.html
│           ├── crear_categoria.html
│           ├── crear_post.html
│           └── buscar_post.html
│
├── db.sqlite3
└── README.md
```

## 🧱 Modelos incluidos

### 🧍 Autor

| Campo   | Tipo                |
|---------|---------------------|
| nombre  | CharField           |
| apellido| CharField           |
| email   | EmailField (único)  |
| bio     | TextField (opcional)|

---

### 🗂️ Categoría

| Campo       | Tipo                |
|-------------|---------------------|
| nombre      | CharField           |
| descripcion | TextField (opcional)|

---

### 📝 Post

| Campo             | Tipo                          |
|-------------------|-------------------------------|
| titulo            | CharField                     |
| contenido         | TextField                     |
| fecha_publicacion | DateField (auto_now_add=True) |
| autor             | ForeignKey a Autor            |
| categoria         | ForeignKey a Categoría        |

---

## 🧾 Formularios

En `forms.py` se definieron formularios basados en **ModelForm**, que permiten crear registros desde la interfaz web:

- `AutorForm`
- `CategoriaForm`
- `PostForm`

Cada formulario incluye validación automática y se renderiza en los templates HTML.

---

## 🔍 Búsqueda en la base de datos

La aplicación incluye un formulario que permite buscar **posts por título**.

La consulta se realiza usando coincidencias parciales:

```python
Post.objects.filter(titulo__icontains=termino)
```

Ruta del buscador:

`/buscar/`

---

## 🌐 Rutas principales

| URL                 | Descripción        |
|---------------------|--------------------|
| `/`                 | Página de inicio   |
| `/autor/nuevo/`     | Crear autor        |
| `/categoria/nueva/` | Crear categoría    |
| `/post/nuevo/`      | Crear post         |
| `/buscar/`          | Buscar posts       |

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/matighigi/TuPrimeraPagina+GHIGI.git
```

### 2. Instalar Django

```bash
pip install django
```

### 3. Aplicar migraciones

```bash
python manage.py migrate
```

### 4. Ejecutar el servidor

```bash
python manage.py runserver
```

### 5. Abrir en el navegador

```cpp
http://127.0.0.1:8000/
```

---

## 🧪 Orden recomendado de prueba

1. Crear un **Autor**
2. Crear una **Categoría**
3. Crear un **Post**
4. Usar la página de **Buscar Post** para buscar por título
5. Confirmar funcionamiento de formularios y búsquedas

---

## 👤 Autor

**Matias Ghigi**