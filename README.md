# Preparar pacotes e scripts
>>> python -m venv fastapienv

# Ativar script
>>> Scripts\activate

# Instalar FatsAPI
>>> pip install fastapi

# Instalr uvicorn
>>> pip install "uvicorn[s]"
Ele é o “motor” que executa aplicações criadas com frameworks modernos como FastAPI, Starlette e Django (modo async).

# Listar pacotes instalados
>>> pip list

# Rodar
>>> uvicorn books:app --reload

>>> pip install "fastapi[standard]"
>>> fastapi dev books.py
>>> fastapi run books.py

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
