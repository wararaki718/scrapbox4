from pydantic import BaseModel


class IrisResponse(BaseModel):
    iris_class: str
