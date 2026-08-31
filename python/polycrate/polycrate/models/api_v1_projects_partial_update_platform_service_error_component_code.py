from typing import Literal

ApiV1ProjectsPartialUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsPartialUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_partial_update_platform_service_error_component_code(
    value: str,
) -> ApiV1ProjectsPartialUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
