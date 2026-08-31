from typing import Literal

ApiV1PrefixesListLoadbalancerRegionErrorComponentAttr = Literal["loadbalancer_region"]

API_V1_PREFIXES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PrefixesListLoadbalancerRegionErrorComponentAttr
] = {
    "loadbalancer_region",
}


def check_api_v1_prefixes_list_loadbalancer_region_error_component_attr(
    value: str,
) -> ApiV1PrefixesListLoadbalancerRegionErrorComponentAttr:
    if value in API_V1_PREFIXES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_LOADBALANCER_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
