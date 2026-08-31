from typing import Literal

ApiV1ActionRunsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ACTION_RUNS_LIST_STATE_VALUES: set[ApiV1ActionRunsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_action_runs_list_state(value: str) -> ApiV1ActionRunsListState:
    if value in API_V1_ACTION_RUNS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_STATE_VALUES!r}")
