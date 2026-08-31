from typing import Literal

ConditionSeverityEnum = Literal["critical", "info", "warning"]

CONDITION_SEVERITY_ENUM_VALUES: set[ConditionSeverityEnum] = {
    "critical",
    "info",
    "warning",
}


def check_condition_severity_enum(value: str) -> ConditionSeverityEnum:
    if value in CONDITION_SEVERITY_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_SEVERITY_ENUM_VALUES!r}")
