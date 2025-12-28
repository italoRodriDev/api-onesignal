from fastapi import FastAPI, HTTPException, status
from app.models.email_model import EmailRequest
from app.models.push_model import PushRequest
from app.models.sms_model import SmsRequest
from app.models.subscribe_user_model import SubscribeUserRequest
from app.services.push_service import send_push
from app.services.sms_service import send_sms
from app.services.email_service import send_email
from app.services.subscribe_user import subscribe_user_sms_email
import httpx

app = FastAPI(title="API de Notificacao - OneSignal")

@app.post("/notifications/subscribe-user")
async def subscribe_user_endpoint(body: SubscribeUserRequest):
    try:
        return await subscribe_user_sms_email(
            external_id=body.external_id,
            phone_number=body.phone_number,
            email=body.email
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.post(
    "/notifications/sms",
    status_code=status.HTTP_202_ACCEPTED
)
async def send_sms_endpoint(body: SmsRequest):
    try:
        return await send_sms(
            message=body.message,
            phones=body.phone_numbers
        )
    
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"{e}"
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao processar notificação"
        )


@app.post(
    "/notifications/push",
    status_code=status.HTTP_202_ACCEPTED
)
async def send_push_endpoint(body: PushRequest):
    try:
        return await send_push(
            title=body.title,
            message=body.message,
            external_ids=body.external_id,
        )

    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"{e}"
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao processar notificação"
        )

@app.post(
    "/notifications/email",
    status_code=status.HTTP_202_ACCEPTED
)
async def send_email_endpoint(body: EmailRequest):
    try:
        return await send_email(
            subject=body.title,
            html=body.html,
            external_ids=body.external_id
        )

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao processar notificação"
        )
