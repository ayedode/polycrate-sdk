from typing import Literal

ActionRunLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ACTION_RUN_LAST_STATE_VALUES: set[ActionRunLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_action_run_last_state(value: str) -> ActionRunLastState:
    if value in ACTION_RUN_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_LAST_STATE_VALUES!r}")
