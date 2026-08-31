from typing import Literal

ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponentAttr = Literal["region_name"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_REGION_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponentAttr
] = {
    "region_name",
}


def check_api_v1_loadbalancers_regions_update_region_name_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateRegionNameErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_REGION_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_REGION_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
