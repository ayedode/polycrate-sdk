from typing import Literal

ApiV1ProjectsArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1ProjectsArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
