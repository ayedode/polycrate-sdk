from typing import Literal

Source98DEnum = Literal["manual", "scheduler"]

SOURCE_98D_ENUM_VALUES: set[Source98DEnum] = {
    "manual",
    "scheduler",
}


def check_source_98d_enum(value: str) -> Source98DEnum:
    if value in SOURCE_98D_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SOURCE_98D_ENUM_VALUES!r}")
