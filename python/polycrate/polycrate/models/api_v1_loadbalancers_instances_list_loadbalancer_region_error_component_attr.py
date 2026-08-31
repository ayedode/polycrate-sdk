from typing import Literal

ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponentAttr = Literal["loadbalancer_region"]

API_V1_LOADBALANCERS_INSTANCES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponentAttr
] = {
    "loadbalancer_region",
}


def check_api_v1_loadbalancers_instances_list_loadbalancer_region_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
