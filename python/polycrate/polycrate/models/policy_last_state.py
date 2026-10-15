from typing import Literal

PolicyLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

POLICY_LAST_STATE_VALUES: set[PolicyLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_policy_last_state(value: str) -> PolicyLastState:
    if value in POLICY_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLICY_LAST_STATE_VALUES!r}")
