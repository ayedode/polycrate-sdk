from typing import Literal

ApiV1OrganizationsArchiveCreateEmailsErrorComponentAttr = Literal["emails"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_organizations_archive_create_emails_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateEmailsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
