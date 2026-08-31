from typing import Literal

ApiV1ActionRunsListStateErrorComponentAttr = Literal["state"]

API_V1_ACTION_RUNS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_action_runs_list_state_error_component_attr(value: str) -> ApiV1ActionRunsListStateErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
