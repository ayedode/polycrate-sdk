from typing import Literal

ApiV1ProjectsUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PROJECTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_projects_update_platform_service_error_component_code(
    value: str,
) -> ApiV1ProjectsUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PROJECTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
