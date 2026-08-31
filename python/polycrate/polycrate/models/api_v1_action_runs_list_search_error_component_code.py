from typing import Literal

ApiV1ActionRunsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ACTION_RUNS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActionRunsListSearchErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_action_runs_list_search_error_component_code(
    value: str,
) -> ApiV1ActionRunsListSearchErrorComponentCode:
    if value in API_V1_ACTION_RUNS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
