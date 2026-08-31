from typing import Literal

ApiV1OrganizationsPartialUpdateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_organizations_partial_update_icon_filename_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateIconFilenameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
