from typing import Literal

ApiV1LoadbalancersInstancesListRegionErrorComponentAttr = Literal["region"]

API_V1_LOADBALANCERS_INSTANCES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesListRegionErrorComponentAttr
] = {
    "region",
}


def check_api_v1_loadbalancers_instances_list_region_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesListRegionErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
