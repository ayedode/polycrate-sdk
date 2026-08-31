from typing import Literal

PopProviderKindEnum = Literal["hardware", "infrastructure", "software"]

POP_PROVIDER_KIND_ENUM_VALUES: set[PopProviderKindEnum] = {
    "hardware",
    "infrastructure",
    "software",
}


def check_pop_provider_kind_enum(value: str) -> PopProviderKindEnum:
    if value in POP_PROVIDER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_PROVIDER_KIND_ENUM_VALUES!r}")
