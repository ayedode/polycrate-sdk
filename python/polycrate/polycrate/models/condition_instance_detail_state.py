from typing import Literal

ConditionInstanceDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONDITION_INSTANCE_DETAIL_STATE_VALUES: set[ConditionInstanceDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_condition_instance_detail_state(value: str) -> ConditionInstanceDetailState:
    if value in CONDITION_INSTANCE_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_STATE_VALUES!r}")
