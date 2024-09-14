# Rick and Morty Flask API - 
## Versión y Dependencias

- pip 
- Python 3.9.13
- Flask & requests


## Pasos para correr el proyecto:

```bash
git clone https://github.com/madpsys/rick-and-morty
cd rick-and-morty
```

## Instalacion dependencias:

```bash
pip install Flask requests
```

## Como correr el proyecto

```bash
python app.py
```

## Esta aplicación solo tiene una ruta

#### `/character`

body:

{
    "character_id": 3
}

#### Respuesta:

```json
{
    "name": "Summer Smith",
    "status": "Alive"
}
```

## Colección de Postman para pruebas

Rick and Morty.postman_collection.json