from typing import Literal

ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponentAttr = Literal["region_config"]

API_V1_LOADBALANCERS_REGIONS_CREATE_REGION_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponentAttr
] = {
    "region_config",
}


def check_api_v1_loadbalancers_regions_create_region_config_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateRegionConfigErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_REGION_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_REGION_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
