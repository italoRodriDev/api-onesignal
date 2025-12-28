import httpx
from app.core.settings import (
    ONESIGNAL_API_KEY,
    ONESIGNAL_APP_ID,
    ONESIGNAL_BASE_URL
)

HEADERS = {
    "Authorization": f"key {ONESIGNAL_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

async def send_sms(message: str, phones: list[str]):
    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "target_channel": "sms",
        "contents": {
            "en": message,
            "pt": message
        },
        "name": "Italo",
        "include_phone_numbers": phones
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ONESIGNAL_BASE_URL}/notifications?c=sms",
            json=payload,
            headers=HEADERS
        )
        
    response.raise_for_status()
    return response.json()