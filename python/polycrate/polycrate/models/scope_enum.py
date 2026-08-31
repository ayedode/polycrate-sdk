from typing import Literal

ScopeEnum = Literal["system", "user"]

SCOPE_ENUM_VALUES: set[ScopeEnum] = {
    "system",
    "user",
}


def check_scope_enum(value: str) -> ScopeEnum:
    if value in SCOPE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SCOPE_ENUM_VALUES!r}")
