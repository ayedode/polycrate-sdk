from typing import Literal

ApiV1ActionRunsListStatusErrorComponentAttr = Literal["status"]

API_V1_ACTION_RUNS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsListStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_action_runs_list_status_error_component_attr(
    value: str,
) -> ApiV1ActionRunsListStatusErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
