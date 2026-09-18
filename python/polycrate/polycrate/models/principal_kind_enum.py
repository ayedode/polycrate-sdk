from typing import Literal

PrincipalKindEnum = Literal["microservice", "org_api_key", "system_api_key", "user"]

PRINCIPAL_KIND_ENUM_VALUES: set[PrincipalKindEnum] = {
    "microservice",
    "org_api_key",
    "system_api_key",
    "user",
}


def check_principal_kind_enum(value: str) -> PrincipalKindEnum:
    if value in PRINCIPAL_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRINCIPAL_KIND_ENUM_VALUES!r}")
