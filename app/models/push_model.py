from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@dataclass(slots=True)
class PushOneSignal:
    app_id: str
    target_channel: str = "push"

    contents: Dict[str, str] = field(default_factory=dict)
    headings: Dict[str, str] = field(default_factory=dict)

    include_aliases: Optional[Dict[str, List[str]]] = None
    include_subscription_ids: Optional[List[str]] = None
    included_segments: Optional[List[str]] = None
    excluded_segments: Optional[List[str]] = None
    filters: Optional[List[Dict[str, Any]]] = None

    data: Optional[Dict[str, Any]] = None
    url: Optional[str] = None
    ttl: Optional[int] = None
    send_after: Optional[str] = None
    priority: Optional[int] = None
    
def build_push(
    app_id: str,
    title: str,
    message: str,
    external_ids: Optional[List[str]] = None
) -> PushOneSignal:

    push = PushOneSignal(
        app_id=app_id,
        headings={"en": title, "pt": title},
        contents={"en": message, "pt": message}
    )

    if external_ids:
        push.include_aliases = {"external_id": external_ids}
    else:
        push.included_segments = ["All"]

    return push
        
class PushRequest(BaseModel):
    title: str = Field(min_length=1)
    message: str = Field(min_length=1)
    external_id: list[str] = Field(default_factory=list)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Titulo",
                "message": "Mensagem",
                "external_id": ["ID_1","ID_2"]
            }
        }
    }