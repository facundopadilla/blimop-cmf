# fastapi-dialogflow-telegram-bot

## Bot de Telegram con FastAPI y DialogFlow

[![Python version](https://img.shields.io/badge/python-%2B3.6-blue)](https://img.shields.io/badge/python-%2B3.6-blue)[![FastAPI version](https://img.shields.io/badge/fastapi-0.71.0-green)](https://img.shields.io/badge/fastapi-0.71.0-green)

---
#### Este proyecto didactico fue presentado para los chicos de Construyendo Mi Futuro en Jujuy y para la Feria Tecnologica de la Municipalidad de Salta (2022)

[![BLimop CMF](https://i.ibb.co/wzCPxcf/Nuevo-proyecto-1.jpg)](https://i.ibb.co/wzCPxcf/Nuevo-proyecto-1.jpg)

----
# Dependencias externas

> Ademas de tener instalada una version de Python, si vas a hacer pruebas locales, vas a necesitar de un software llamado Ngrok, el cual lo puedes googlear e instalar facilmente.

----
# Instalacion

```sh
 pip install -r requirements.txt (si estas en Windows, en el archivo requirements.txt quita la linea 'uvloop')
 uvicorn main:app --reload  # esto hara funcionar al servidor
```
---
# Forward con Ngrok

```sh
ngrok http http://127.0.0.1:8000/ 
```
---
