from typing import Literal

APMStackState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

APM_STACK_STATE_VALUES: set[APMStackState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_apm_stack_state(value: str) -> APMStackState:
    if value in APM_STACK_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APM_STACK_STATE_VALUES!r}")
