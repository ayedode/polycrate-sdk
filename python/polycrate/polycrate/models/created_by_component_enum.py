from typing import Literal

CreatedByComponentEnum = Literal["api", "cli", "operator"]

CREATED_BY_COMPONENT_ENUM_VALUES: set[CreatedByComponentEnum] = {
    "api",
    "cli",
    "operator",
}


def check_created_by_component_enum(value: str) -> CreatedByComponentEnum:
    if value in CREATED_BY_COMPONENT_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATED_BY_COMPONENT_ENUM_VALUES!r}")
