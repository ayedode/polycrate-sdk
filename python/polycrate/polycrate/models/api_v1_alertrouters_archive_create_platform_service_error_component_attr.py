from typing import Literal

ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_alertrouters_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
