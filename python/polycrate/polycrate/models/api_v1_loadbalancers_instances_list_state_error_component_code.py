from typing import Literal

ApiV1LoadbalancersInstancesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_loadbalancers_instances_list_state_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesListStateErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
