from typing import Literal

ApiV1WorkspacesCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_create_platform_service_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreatePlatformServiceErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
