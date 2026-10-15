from typing import Literal

PrefixScope = Literal["system", "user"]

PREFIX_SCOPE_VALUES: set[PrefixScope] = {
    "system",
    "user",
}


def check_prefix_scope(value: str) -> PrefixScope:
    if value in PREFIX_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PREFIX_SCOPE_VALUES!r}")
