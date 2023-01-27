from pydantic import Field
from pydantic import BaseSettings
from pydantic import BaseModel

origins = [ "https://localhost",
            "https://localhost:8080",
            "http://localhost:8080"
]

class Settings(BaseSettings):
    db_url:str= 'postgresql://postgres:ags009@localhost:5433/demo1'

settings = Settings()