from typing import Literal

PolicyListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

POLICY_LIST_STATE_VALUES: set[PolicyListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_policy_list_state(value: str) -> PolicyListState:
    if value in POLICY_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_LIST_STATE_VALUES!r}")
