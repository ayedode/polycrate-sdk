from typing import Literal

ApiV1OrganizationsArchiveCreateOwnerIdErrorComponentAttr = Literal["owner_id"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateOwnerIdErrorComponentAttr
] = {
    "owner_id",
}


def check_api_v1_organizations_archive_create_owner_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateOwnerIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
