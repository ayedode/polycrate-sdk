from typing import Literal

ApiV1ActionRunsListActionErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ACTION_RUNS_LIST_ACTION_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActionRunsListActionErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_action_runs_list_action_error_component_code(
    value: str,
) -> ApiV1ActionRunsListActionErrorComponentCode:
    if value in API_V1_ACTION_RUNS_LIST_ACTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_ACTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
