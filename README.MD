# TECNOLOGIA: FastAPI

# AUTOR: Instructor Jhonny Guerrero

# DESCRIPCION: Sistema de Gestión de Facturación y Transacciones (API de Aprendizaje)

## Contexto

El proyecto simula el núcleo financiero de una plataforma comercial. Trabajaremos con tres entidades principales, simulando al inicio una relación como BD:

1. **Clientes:** (id, nombre, email, descripcion)
2. **Facturas:** (id, fecha, vr_total, cliente)
3. **Transacciones:** (id, cantidad, vr_unitario, id_factura)

---

## REQUISITOS 

1- PYTHON 3,12
2- GIT RECOMENDADO
3- Gestion de entornos virtuales ('venv')
4- Instalar Fastapi[standard]

## CREAR LOS ENDPOINT DEL PROYECTO CLIENTES PARA REALIZAR EL CRUD: EDITANDO EL ARCHIVO MAIN.PY 

## Creamos una lista_clientes de python (estatica)

1. Crear el endpoint listar_clientes, obtener todos los clientes de la lista_clientes. #CHECK

2. Crear el endpoint listar_cliente, obtener un solo cliente de la lista_clientes.
   NOTA: se puede ir borrando los datos de la lista_clientes, pero no la variable.

3. Crear endpoint crear_clientes, enviar datos del cliente y guardarlos en la lista_clientes.
   NOTA: Tener en cuenta el typing o tipado de datos para la lista_clientes y el modelo que se construirá.

4. Crear una **clase o modelo** llamado `clientes` como se indica en la línea 13 de este archivo.

5. Editar la lista_clientes aplicando typing.

6. Editar endpoint crear_clientes aplicando typing.

7. Comprobar el funcionamiento de crear_clientes.

Se edito el endpoint listar una sola factura , y el manej de excepciones

# 9 =================

# Editar el endpoint crear factura, segun el modelo 

1. Editar el endpoint crear_facutra

2. comprobar el funcionamiento  

#10 =================

# Editar el endpoint crear_factura, según el modelo -- Continuación

1. Edición del método vr_total del modelo facturas, para que haga el cálculo a las transacciones que pertenecen a esa factura.
   Para comprobar el funcionamiento del método vr_total debemos:
2. Editar endpoint de crear transacciones, también puede editar el de listar todas las transacciones.
3. Comprobar funcionamiento.

**Ejercicio Terminar, los endpoint de modificar y eliminar**

proyecto_clientes/
│
├── app/
│   ├── __init__.py
│   ├── main.py                # Punto de entrada de FastAPI
│   ├── conexion_bd.py         # Configuración de la base de datos
│   │
│   ├── modelos/               # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── esquemas/              # Modelos Pydantic
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── enrutador/             # Endpoints (APIRouter)
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── crud/                  # Funciones para acceder a la BD
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   └── dependencias.py        # Dependencias (get_db, autenticación, etc.)
│
├── .venv/
├── requirements.txt
├── README.md
└── .gitignore

fastapi dev app/main.py

