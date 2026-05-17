from pydantic import BaseModel
from pydantic import EmailStr

class userRegister(BaseModel):
    email: EmailStr
    password: str

class userLogin(BaseModel):
    email: EmailStr
    password: str

class tokenResponse(BaseModel):
    access_token: str
    token_type: str
