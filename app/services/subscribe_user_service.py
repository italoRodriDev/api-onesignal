import httpx
from app.core.settings import (
    ONESIGNAL_API_KEY,
    ONESIGNAL_APP_ID,
    ONESIGNAL_BASE_URL
)

HEADERS_USERS = {
    "Authorization": f"Basic {ONESIGNAL_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

async def subscribe_user_sms_email(
    external_id: str,
    phone_number: str | None = None,
    email: str | None = None
):
    subscriptions = []

    if phone_number:
        subscriptions.append({
            "type": "SMS",
            "token": phone_number,
        })

    if email:
        subscriptions.append({
            "type": "Email",
            "token": email,
        })

    payload = {
        "identity": { "external_id": external_id },
        "subscriptions": subscriptions
    }

    async with httpx.AsyncClient() as client:
        url = f"{ONESIGNAL_BASE_URL}/apps/{ONESIGNAL_APP_ID}/users"
        
        response = await client.post(
            url,
            json=payload,
            headers=HEADERS_USERS
        )

    response.raise_for_status()
    return response.json()