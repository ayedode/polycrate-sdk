from typing import Literal

ApiV1PopsArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_POPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pops_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PopsArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_POPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
