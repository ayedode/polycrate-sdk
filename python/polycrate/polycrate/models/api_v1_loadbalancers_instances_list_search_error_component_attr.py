from typing import Literal

ApiV1LoadbalancersInstancesListSearchErrorComponentAttr = Literal["search"]

API_V1_LOADBALANCERS_INSTANCES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_loadbalancers_instances_list_search_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListSearchErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
