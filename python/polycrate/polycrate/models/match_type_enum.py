from typing import Literal

MatchTypeEnum = Literal["contains", "contains_all", "exact", "prefix"]

MATCH_TYPE_ENUM_VALUES: set[MatchTypeEnum] = {
    "contains",
    "contains_all",
    "exact",
    "prefix",
}


def check_match_type_enum(value: str) -> MatchTypeEnum:
    if value in MATCH_TYPE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATCH_TYPE_ENUM_VALUES!r}")
