from typing import Literal

APMStackLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

APM_STACK_LAST_STATE_VALUES: set[APMStackLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_apm_stack_last_state(value: str) -> APMStackLastState:
    if value in APM_STACK_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APM_STACK_LAST_STATE_VALUES!r}")
