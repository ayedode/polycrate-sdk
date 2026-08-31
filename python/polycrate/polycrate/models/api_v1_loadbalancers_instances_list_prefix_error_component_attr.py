from typing import Literal

ApiV1LoadbalancersInstancesListPrefixErrorComponentAttr = Literal["prefix"]

API_V1_LOADBALANCERS_INSTANCES_LIST_PREFIX_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListPrefixErrorComponentAttr
] = {
    "prefix",
}


def check_api_v1_loadbalancers_instances_list_prefix_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListPrefixErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_PREFIX_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_PREFIX_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
