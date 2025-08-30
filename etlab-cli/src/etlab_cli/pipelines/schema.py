from typing import List, Any
from pydantic import BaseModel

class WithParams(BaseModel):
    params: List[Any]

class Step(BaseModel):
    id: str
    operator: str
    with_: List[WithParams]

class Pipeline(BaseModel):
    version: str
    name: str

