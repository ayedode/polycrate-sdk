from typing import Literal

ApiV1ActionRunsListKindErrorComponentAttr = Literal["kind"]

API_V1_ACTION_RUNS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_action_runs_list_kind_error_component_attr(value: str) -> ApiV1ActionRunsListKindErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
