from typing import Literal

ConditionInstanceDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONDITION_INSTANCE_DETAIL_LAST_STATE_VALUES: set[ConditionInstanceDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_condition_instance_detail_last_state(value: str) -> ConditionInstanceDetailLastState:
    if value in CONDITION_INSTANCE_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_DETAIL_LAST_STATE_VALUES!r}")
