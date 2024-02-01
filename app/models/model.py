from typing import Union
from pydantic import BaseModel

class first_model(BaseModel):
    city: Union[str, None] = None
    parameters: Union[dict, None] = None

class second_model(BaseModel):
    city: Union[list, None] = None
    parameters: Union[str, None] = None

class third_model(BaseModel):
    city: Union[str, None] = None
    par: Union[dict, None] = None