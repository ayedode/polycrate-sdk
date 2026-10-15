from typing import Literal

ActivityScope = Literal["system", "user"]

ACTIVITY_SCOPE_VALUES: set[ActivityScope] = {
    "system",
    "user",
}


def check_activity_scope(value: str) -> ActivityScope:
    if value in ACTIVITY_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_SCOPE_VALUES!r}")
