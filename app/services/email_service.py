import httpx
from app.core.settings import (
    ONESIGNAL_API_KEY,
    ONESIGNAL_APP_ID,
    ONESIGNAL_BASE_URL
)

HEADERS = {
    "Authorization": f"Key {ONESIGNAL_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

async def send_email(
    subject: str,
    html: str,
    external_ids: list[str] | None = None,
    emails: list[str] | None = None
):
    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "target_channel": "email",
        "email_subject": subject,
        "email_body": html,
    }

    if external_ids:
        payload["include_aliases"] = {
            "external_id": external_ids
        }

    elif emails:
        payload["email_to"] = emails

    else:
        payload["included_segments"] = ["All"]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ONESIGNAL_BASE_URL}/notifications?c=email",
            json=payload,
            headers=HEADERS
        )

    response.raise_for_status()
    return response.json()