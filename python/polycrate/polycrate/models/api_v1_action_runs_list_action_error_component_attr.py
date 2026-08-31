from typing import Literal

ApiV1ActionRunsListActionErrorComponentAttr = Literal["action"]

API_V1_ACTION_RUNS_LIST_ACTION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsListActionErrorComponentAttr] = {
    "action",
}


def check_api_v1_action_runs_list_action_error_component_attr(
    value: str,
) -> ApiV1ActionRunsListActionErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_ACTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_ACTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
