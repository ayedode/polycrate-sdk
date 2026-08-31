from typing import Literal

ApiV1OrganizationsArchiveCreateIconFilenameErrorComponentAttr = Literal["icon_filename"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateIconFilenameErrorComponentAttr
] = {
    "icon_filename",
}


def check_api_v1_organizations_archive_create_icon_filename_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateIconFilenameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ICON_FILENAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
