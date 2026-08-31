from typing import Literal

ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_icon_upload_create_platform_service_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
