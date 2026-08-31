from typing import Literal

ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_loadbalancers_regions_update_criticality_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
