from typing import Literal

ApiV1LoadbalancersInstancesListScopeErrorComponentAttr = Literal["scope"]

API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_loadbalancers_instances_list_scope_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListScopeErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
