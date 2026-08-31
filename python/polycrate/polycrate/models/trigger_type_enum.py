from typing import Literal

TriggerTypeEnum = Literal["reconciliation", "schedule"]

TRIGGER_TYPE_ENUM_VALUES: set[TriggerTypeEnum] = {
    "reconciliation",
    "schedule",
}


def check_trigger_type_enum(value: str) -> TriggerTypeEnum:
    if value in TRIGGER_TYPE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_TYPE_ENUM_VALUES!r}")
