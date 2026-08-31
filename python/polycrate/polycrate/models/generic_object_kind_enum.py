from typing import Literal

GenericObjectKindEnum = Literal["generic"]

GENERIC_OBJECT_KIND_ENUM_VALUES: set[GenericObjectKindEnum] = {
    "generic",
}


def check_generic_object_kind_enum(value: str) -> GenericObjectKindEnum:
    if value in GENERIC_OBJECT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GENERIC_OBJECT_KIND_ENUM_VALUES!r}")
