from typing import Literal

ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_organizations_discover_create_icon_filename_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
