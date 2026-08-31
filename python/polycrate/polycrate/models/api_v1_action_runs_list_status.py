from typing import Literal

ApiV1ActionRunsListStatus = Literal["failed", "pending", "running", "success"]

API_V1_ACTION_RUNS_LIST_STATUS_VALUES: set[ApiV1ActionRunsListStatus] = {
    "failed",
    "pending",
    "running",
    "success",
}


def check_api_v1_action_runs_list_status(value: str) -> ApiV1ActionRunsListStatus:
    if value in API_V1_ACTION_RUNS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_STATUS_VALUES!r}")
