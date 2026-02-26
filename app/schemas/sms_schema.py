from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

@dataclass(slots=True)
class SmsOneSignal:
    app_id: str
    target_channel: str = "sms"

    contents: Dict[str, str] = field(default_factory=dict)

    include_aliases: Optional[Dict[str, List[str]]] = None
    include_phone_numbers: Optional[List[str]] = None
    included_segments: Optional[List[str]] = None
    excluded_segments: Optional[List[str]] = None
    filters: Optional[List[Dict[str, Any]]] = None

    data: Optional[Dict[str, Any]] = None
    send_after: Optional[str] = None
    ttl: Optional[int] = None
    
def build_sms(
    app_id: str,
    message: str,
    external_ids: Optional[List[str]] = None,
    phone_numbers: Optional[List[str]] = None
) -> SmsOneSignal:

    sms = SmsOneSignal(
        app_id=app_id,
        contents={"en": message}
    )

    if external_ids:
        sms.include_aliases = {"external_id": external_ids}

    elif phone_numbers:
        sms.include_phone_numbers = phone_numbers

    else:
        sms.included_segments = ["All"]

    return sms

class SmsRequest(BaseModel):
    message: str = Field(min_length=1)
    external_id: List[str] = Field(default_factory=list)
    phone_numbers: List[str] = Field(default_factory=list)

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Seu código é 123456",
                "external_id": ["USER_1"],
                "phone_numbers": ["+5511999999999"]
            }
        }
    }
