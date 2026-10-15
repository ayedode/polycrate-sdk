from typing import Literal

ActionRunState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ACTION_RUN_STATE_VALUES: set[ActionRunState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_action_run_state(value: str) -> ActionRunState:
    if value in ACTION_RUN_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_STATE_VALUES!r}")
