from typing import Literal

ApiV1OrganizationsUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_update_platform_service_error_component_code(
    value: str,
) -> ApiV1OrganizationsUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
