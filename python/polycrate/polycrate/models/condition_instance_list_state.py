from typing import Literal

ConditionInstanceListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONDITION_INSTANCE_LIST_STATE_VALUES: set[ConditionInstanceListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_condition_instance_list_state(value: str) -> ConditionInstanceListState:
    if value in CONDITION_INSTANCE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONDITION_INSTANCE_LIST_STATE_VALUES!r}")
