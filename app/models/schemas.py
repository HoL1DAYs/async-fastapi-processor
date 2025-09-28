from pydantic import BaseModel
from typing import Any

class CatFact(BaseModel):
    fact: str
    length: int

class ProcessResponse(BaseModel):
    input_data: Any
    cat_fact: CatFact
