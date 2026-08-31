from typing import Literal

ApiV1OrganizationsCreateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_ORGANIZATIONS_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_organizations_create_icon_filename_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateIconFilenameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
