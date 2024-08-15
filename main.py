from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int


user = User(name = "Rafi", email = "rafi@gmail.com", account_id = 1234)
print(user)


