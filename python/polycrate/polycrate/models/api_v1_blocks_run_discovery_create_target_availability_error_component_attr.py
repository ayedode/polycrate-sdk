from typing import Literal

ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_blocks_run_discovery_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
