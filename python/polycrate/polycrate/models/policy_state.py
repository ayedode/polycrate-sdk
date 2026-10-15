from typing import Literal

PolicyState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

POLICY_STATE_VALUES: set[PolicyState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_policy_state(value: str) -> PolicyState:
    if value in POLICY_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_STATE_VALUES!r}")
