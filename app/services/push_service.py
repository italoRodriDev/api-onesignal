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

async def send_push(title: str, message: str, external_ids: list[str]):
    if len(external_ids) > 0:
        return await send_push_external_ids(
            title=title,
            message=message,
            external_ids=external_ids
        )
    return await send_push_all_users(title=title, message=message)


async def send_push_external_ids(
    title: str,
    message: str,
    external_ids: list[str]
):
    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "target_channel": "push",
        "include_aliases": {
            "external_id": external_ids
        },
        "headings": {"en": title, "pt": title},
        "contents": {"en": message, "pt": message}
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ONESIGNAL_BASE_URL}/notifications?c=push",
            json=payload,
            headers=HEADERS
        )

    response.raise_for_status()
    return response.json()


async def send_push_all_users(title: str, message: str):
    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "target_channel": "push",
        "headings": {"en": title, "pt": title},
        "contents": {"en": message, "pt": message},
        "included_segments": ["All"]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ONESIGNAL_BASE_URL}/notifications?c=push",
            json=payload,
            headers=HEADERS
        )

    response.raise_for_status()
    return response.json()
