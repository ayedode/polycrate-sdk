from typing import Literal

ActionRunListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ACTION_RUN_LIST_STATE_VALUES: set[ActionRunListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_action_run_list_state(value: str) -> ActionRunListState:
    if value in ACTION_RUN_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_LIST_STATE_VALUES!r}")
