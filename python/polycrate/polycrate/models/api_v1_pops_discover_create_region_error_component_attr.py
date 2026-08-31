from typing import Literal

ApiV1PopsDiscoverCreateRegionErrorComponentAttr = Literal["region"]

API_V1_POPS_DISCOVER_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsDiscoverCreateRegionErrorComponentAttr] = {
    "region",
}


def check_api_v1_pops_discover_create_region_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateRegionErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
