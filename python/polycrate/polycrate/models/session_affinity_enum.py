from typing import Literal

SessionAffinityEnum = Literal["cookie", "ip", "none"]

SESSION_AFFINITY_ENUM_VALUES: set[SessionAffinityEnum] = {
    "cookie",
    "ip",
    "none",
}


def check_session_affinity_enum(value: str) -> SessionAffinityEnum:
    if value in SESSION_AFFINITY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SESSION_AFFINITY_ENUM_VALUES!r}")
