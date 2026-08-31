from typing import Literal

ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_LOADBALANCERS_INSTANCES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_loadbalancers_instances_list_loadbalancer_region_error_component_code(
    value: str,
) -> ApiV1LoadbalancersInstancesListLoadbalancerRegionErrorComponentCode:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
