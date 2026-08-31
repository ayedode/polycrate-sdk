from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponentAttr = Literal["region_config"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_REGION_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponentAttr
] = {
    "region_config",
}


def check_api_v1_loadbalancers_regions_partial_update_region_config_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateRegionConfigErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_REGION_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_REGION_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
