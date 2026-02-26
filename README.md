# By Italo Rodri. Dev.

# Preparar pacotes e scripts
>>> python -m venv fastapienv

# Ativar script
>>> Scripts\activate

# Instalar FatsAPI
>>> pip install fastapi

# Instalr uvicorn
>>> pip install "uvicorn[s]"

# Listar pacotes instalados
>>> pip list

# Rodar
>>> uvicorn main:app --reload

>>> pip install "fastapi[standard]"
>>> fastapi dev app\main.py
>>> fastapi run app\main.py

uvicorn app.main:app --reload


# API ONE-SIGNAL REFERENCE:

PUSH NOTIFICATION:
>>> https://documentation.onesignal.com/reference/push-notification
EMAIL:
>>> https://documentation.onesignal.com/reference/email
SMS: 
>>> https://documentation.onesignal.com/reference/sms

CADASTRAR EXTERNAL_ID:
>>> https://documentation.onesignal.com/reference/create-user

ATUALIZAR EXTERNAL_ID:
>>> https://documentation.onesignal.com/reference/update-user

DELETAR EXTERNAL_ID:
>>> https://documentation.onesignal.com/reference/delete-user
