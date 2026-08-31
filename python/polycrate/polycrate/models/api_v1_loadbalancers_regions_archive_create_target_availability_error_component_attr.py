from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_loadbalancers_regions_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
