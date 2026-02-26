import re
from typing import Optional
from pydantic import BaseModel, Field, field_validator, EmailStr

class SubscribeUserRequest(BaseModel):
    external_id: str = Field(min_length=1)
    email: Optional[EmailStr] = None 
    phone_number: str | None = None

    @field_validator("phone_number")
    @classmethod
    def validate_e164(cls, value: str):
        if not re.match(r"^\+[1-9]\d{7,14}$", value):
            raise ValueError(
                "phone_number deve estar no formato E.164 (ex: +5511999999999)"
            )
        return value

    model_config = {
        "json_schema_extra": {
            "example": {
                "external_id": "USER_123",
                "phone_number": "+5511999999999",
                "email": "user@email.com"
            }
        }
    }
