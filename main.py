from pydantic import BaseModel, EmailStr, field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    # Custom Field Validation
    @field_validator('account_id')
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value


user = User(name = "Rafi", email = "rafi@gmail.com", account_id = 1234)
print(user)


