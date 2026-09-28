# AWS Cloud Practitioner Assistant

Asistente conversacional especializado en la preparación para la certificación AWS Certified Cloud Practitioner.

## Tecnologías

* Python
* Streamlit
* Amazon Bedrock
* Amazon Nova Pro
* Amazon S3
* Docker

## Funcionalidades

* Interfaz de chat mediante Streamlit.
* Respuestas especializadas en AWS Cloud Practitioner.
* Historial de conversación.
* Persistencia de chats mediante Amazon S3.
* Generación de respuestas mediante Amazon Bedrock.
* Ejecución mediante Docker.

## Configuración

Crear un archivo `.env` en la raíz del proyecto:

```env
AWS_BEARER_TOKEN_BEDROCK=tu_api_key
```

La API key debe mantenerse únicamente en `.env` y no debe subirse al repositorio.

Para utilizar el almacenamiento de chats, es necesario tener configuradas las credenciales de AWS mediante AWS CLI.

## Ejecución con Docker

Iniciar la aplicación:

```bash
docker compose up --build
```

La aplicación estará disponible en:

```text
http://localhost:8501
```

## Almacenamiento

Los chats se almacenan como archivos JSON en un bucket privado de Amazon S3.

El bucket utilizado por la aplicación es:

```text
semillero-llmbedrock-lrm
```

## Seguridad

* La API key se almacena en `.env`.
* `.env` está incluido en `.gitignore`.
* El bucket de S3 no tiene acceso público.
* Las credenciales de AWS no se incluyen en el repositorio.
