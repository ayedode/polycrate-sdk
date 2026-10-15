from typing import Literal

ConditionInstanceDetailScope = Literal["system", "user"]

CONDITION_INSTANCE_DETAIL_SCOPE_VALUES: set[ConditionInstanceDetailScope] = {
    "system",
    "user",
}


def check_condition_instance_detail_scope(value: str) -> ConditionInstanceDetailScope:
    if value in CONDITION_INSTANCE_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_SCOPE_VALUES!r}")
