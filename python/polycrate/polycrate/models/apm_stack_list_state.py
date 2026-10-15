from typing import Literal

APMStackListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

APM_STACK_LIST_STATE_VALUES: set[APMStackListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_apm_stack_list_state(value: str) -> APMStackListState:
    if value in APM_STACK_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APM_STACK_LIST_STATE_VALUES!r}")
