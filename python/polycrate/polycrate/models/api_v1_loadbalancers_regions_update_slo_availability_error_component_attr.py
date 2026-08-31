from typing import Literal

ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_loadbalancers_regions_update_slo_availability_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateSloAvailabilityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
