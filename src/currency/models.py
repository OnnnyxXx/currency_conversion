from pydantic import BaseModel


class CurrencyParameter(BaseModel):
    from_: str
    to: str
    amount: int
