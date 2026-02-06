from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    # Pydantic matches this to "API_KEY" in the .env file automatically
    alpaca_api_key: SecretStr 
    alpaca_api_secret_key: SecretStr

    wrds_username: str
    pgpassword: SecretStr

    database_path: str
    # This tells Pydantic to look at the .env file
    model_config = SettingsConfigDict(env_file=".env")

# Instantiate it
settings = Settings()