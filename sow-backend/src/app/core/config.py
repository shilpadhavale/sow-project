# pydantic v2 moved BaseSettings to the separate `pydantic-settings` package.
# To support both environments, try to import from pydantic first and fall back
# to pydantic_settings. Prefer the new `model_config` style for pydantic v2.
try:
    # pydantic v1 (legacy) may expose BaseSettings here
    from pydantic import BaseSettings  # type: ignore
    _USING_PYDANTIC_SETTINGS = False
except Exception:
    from pydantic_settings import BaseSettings  # type: ignore
    _USING_PYDANTIC_SETTINGS = True


from typing import Optional


class Settings(BaseSettings):
    ENV: str = "development"
    PORT: int = 8000
    ACS_CONNECTION_STRING: Optional[str] = None

    # pydantic v2 / pydantic-settings uses `model_config` for settings
    model_config = {"env_file": ".env"}


settings = Settings()