from typing import Literal

Severity401Enum = Literal["critical", "high", "low", "medium", "none", "unknown"]

SEVERITY_401_ENUM_VALUES: set[Severity401Enum] = {
    "critical",
    "high",
    "low",
    "medium",
    "none",
    "unknown",
}


def check_severity_401_enum(value: str) -> Severity401Enum:
    if value in SEVERITY_401_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SEVERITY_401_ENUM_VALUES!r}")
