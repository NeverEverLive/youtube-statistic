from pydantic import BaseModel


class ResponseSchema(BaseModel):
    success: bool = True
    message: str | None

    class Config:
        allow_population_by_field_name = True
