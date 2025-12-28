from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

@dataclass(slots=True)
class EmailOneSignal:
    app_id: str
    target_channel: str = "email"

    email_subject: str | None = None
    email_body: str | None = None
    email_preheader: Optional[str] = None

    include_aliases: Optional[Dict[str, List[str]]] = None
    email_to: Optional[List[str]] = None
    include_subscription_ids: Optional[List[str]] = None
    included_segments: Optional[List[str]] = None
    excluded_segments: Optional[List[str]] = None
    filters: Optional[List[Dict[str, Any]]] = None

    custom_data: Optional[Dict[str, Any]] = None

    email_from_name: Optional[str] = None
    email_from_address: Optional[str] = None
    email_reply_to_address: Optional[str] = None

    include_unsubscribed: Optional[bool] = None
    disable_email_click_tracking: Optional[bool] = None

    send_after: Optional[str] = None
    idempotency_key: Optional[str] = None
    
def build_email(
    app_id: str,
    subject: str,
    html: str,
    external_ids: Optional[List[str]] = None,
    emails: Optional[List[str]] = None
) -> EmailOneSignal:

    email = EmailOneSignal(
        app_id=app_id,
        email_subject=subject,
        email_body=html
    )

    if external_ids:
        email.include_aliases = {"external_id": external_ids}

    elif emails:
        email.email_to = emails

    else:
        email.included_segments = ["All"]

    return email

class EmailRequest(BaseModel):
    subject: str = Field(min_length=1)
    html: str = Field(min_length=1)
    external_id: List[str] = Field(default_factory=list)
    emails: List[str] = Field(default_factory=list)

    model_config = {
        "json_schema_extra": {
            "example": {
                "subject": "Bem-vindo 🎉",
                "html": "<h1>Olá!</h1><p>Cadastro realizado com sucesso.</p>",
                "external_id": ["USER_1"],
                "emails": ["italo@email.com"]
            }
        }
    }