from typing import Literal

ApiV1OrganizationsPartialUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_organizations_partial_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateDebugModeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
