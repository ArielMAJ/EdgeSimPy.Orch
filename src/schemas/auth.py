from pydantic import BaseModel


class VerifyTokenResponse(BaseModel):
    valid: bool
    reason: str | None = None
