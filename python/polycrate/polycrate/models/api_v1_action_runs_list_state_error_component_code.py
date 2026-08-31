from typing import Literal

ApiV1ActionRunsListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_ACTION_RUNS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActionRunsListStateErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_action_runs_list_state_error_component_code(value: str) -> ApiV1ActionRunsListStateErrorComponentCode:
    if value in API_V1_ACTION_RUNS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
