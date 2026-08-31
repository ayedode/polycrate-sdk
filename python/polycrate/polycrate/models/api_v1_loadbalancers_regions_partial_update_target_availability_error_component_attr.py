from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_loadbalancers_regions_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
