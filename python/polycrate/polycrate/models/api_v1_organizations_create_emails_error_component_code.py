from typing import Literal

ApiV1OrganizationsCreateEmailsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsCreateEmailsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_create_emails_error_component_code(
    value: str,
) -> ApiV1OrganizationsCreateEmailsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_EMAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
