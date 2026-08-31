from typing import Literal

ApiV1LoadbalancersInstancesListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_loadbalancers_instances_list_scope_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesListScopeErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
