from typing import Literal

ApiV1OrganizationsArchiveCreateEmailsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateEmailsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_archive_create_emails_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateEmailsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
