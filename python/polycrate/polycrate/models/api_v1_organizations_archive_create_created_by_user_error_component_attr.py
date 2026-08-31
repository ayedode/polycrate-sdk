from typing import Literal

ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_organizations_archive_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
