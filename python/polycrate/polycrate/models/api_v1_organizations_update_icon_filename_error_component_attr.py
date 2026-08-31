from typing import Literal

ApiV1OrganizationsUpdateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_ORGANIZATIONS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_organizations_update_icon_filename_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateIconFilenameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
