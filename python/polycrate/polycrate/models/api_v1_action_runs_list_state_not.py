from typing import Literal

ApiV1ActionRunsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_ACTION_RUNS_LIST_STATE_NOT_VALUES: set[ApiV1ActionRunsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_action_runs_list_state_not(value: str) -> ApiV1ActionRunsListStateNot:
    if value in API_V1_ACTION_RUNS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_STATE_NOT_VALUES!r}")
