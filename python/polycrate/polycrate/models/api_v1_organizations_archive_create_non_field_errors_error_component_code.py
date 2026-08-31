from typing import Literal

ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_archive_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
