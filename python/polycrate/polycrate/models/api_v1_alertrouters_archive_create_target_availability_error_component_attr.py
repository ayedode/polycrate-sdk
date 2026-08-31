from typing import Literal

ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_alertrouters_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
