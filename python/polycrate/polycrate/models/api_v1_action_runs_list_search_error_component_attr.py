from typing import Literal

ApiV1ActionRunsListSearchErrorComponentAttr = Literal["search"]

API_V1_ACTION_RUNS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_action_runs_list_search_error_component_attr(
    value: str,
) -> ApiV1ActionRunsListSearchErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
