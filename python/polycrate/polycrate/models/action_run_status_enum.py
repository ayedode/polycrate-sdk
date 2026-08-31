from typing import Literal

ActionRunStatusEnum = Literal["cancelled", "failed", "pending", "running", "success"]

ACTION_RUN_STATUS_ENUM_VALUES: set[ActionRunStatusEnum] = {
    "cancelled",
    "failed",
    "pending",
    "running",
    "success",
}


def check_action_run_status_enum(value: str) -> ActionRunStatusEnum:
    if value in ACTION_RUN_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTION_RUN_STATUS_ENUM_VALUES!r}")
