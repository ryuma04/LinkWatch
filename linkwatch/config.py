from typing import List

import tomllib
from pydantic import BaseModel, field_validator, ConfigDict


class Site(BaseModel):
    name: str
    url: str

    model_config = ConfigDict(anystr_strip_whitespace=True)

    @field_validator("name")
    def name_not_empty(cls, value):
        if not value:
            raise ValueError("site name can not be empty")
        return value

    @field_validator("url")
    def url_has_scheme(cls, value):
        if not value.startswith(("http://", "https://")):
            raise ValueError("url must start with http:// or https://")
        return value


class Settings(BaseModel):
    title: str = "linkwatch"
    output: str = "status.html"
    sites: List[Site] = []

    model_config = ConfigDict(extra="forbid")


def load_settings(path="sites.toml"):
    data = tomllib.load(open(path, "rb"))
    return Settings(**data)
