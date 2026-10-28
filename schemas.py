
from typing import Literal

from pydantic import BaseModel, Field


class SummaryRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Texte à résumer",
    )

    length: Literal["court", "moyen", "long"] = Field(
        default="moyen",
        description="Longueur souhaitée du résumé",
    )


class SummaryResponse(BaseModel):
    summary: str = Field(
        ...,
        description="Texte résumé par l'agent",
    )
