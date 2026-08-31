from typing import Literal

ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_organizations_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
