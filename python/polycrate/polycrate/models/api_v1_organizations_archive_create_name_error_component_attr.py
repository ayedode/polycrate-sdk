from typing import Literal

ApiV1OrganizationsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_organizations_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
