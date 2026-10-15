from typing import Literal

ActionRunListStatus = Literal["cancelled", "failed", "pending", "running", "success"]

ACTION_RUN_LIST_STATUS_VALUES: set[ActionRunListStatus] = {
    "cancelled",
    "failed",
    "pending",
    "running",
    "success",
}


def check_action_run_list_status(value: str) -> ActionRunListStatus:
    if value in ACTION_RUN_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_LIST_STATUS_VALUES!r}")
