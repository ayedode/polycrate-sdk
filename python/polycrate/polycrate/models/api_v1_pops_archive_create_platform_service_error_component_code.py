from typing import Literal

ApiV1PopsArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_POPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pops_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1PopsArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_POPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
