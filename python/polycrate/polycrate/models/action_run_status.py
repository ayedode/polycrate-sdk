from typing import Literal

ActionRunStatus = Literal["cancelled", "failed", "pending", "running", "success"]

ACTION_RUN_STATUS_VALUES: set[ActionRunStatus] = {
    "cancelled",
    "failed",
    "pending",
    "running",
    "success",
}


def check_action_run_status(value: str) -> ActionRunStatus:
    if value in ACTION_RUN_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_STATUS_VALUES!r}")
