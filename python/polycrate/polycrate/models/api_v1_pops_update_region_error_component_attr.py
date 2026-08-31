from typing import Literal

ApiV1PopsUpdateRegionErrorComponentAttr = Literal["region"]

API_V1_POPS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateRegionErrorComponentAttr] = {
    "region",
}


def check_api_v1_pops_update_region_error_component_attr(value: str) -> ApiV1PopsUpdateRegionErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
