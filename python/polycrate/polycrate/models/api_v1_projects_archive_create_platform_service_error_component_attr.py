from typing import Literal

ApiV1ProjectsArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PROJECTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_projects_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
