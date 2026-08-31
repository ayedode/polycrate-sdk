from typing import Literal

ApiV1OrganizationsIconUploadCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_organizations_icon_upload_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateDebugModeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
