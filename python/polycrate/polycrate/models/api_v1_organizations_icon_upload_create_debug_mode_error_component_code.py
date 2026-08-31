from typing import Literal

ApiV1OrganizationsIconUploadCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_icon_upload_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateDebugModeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
