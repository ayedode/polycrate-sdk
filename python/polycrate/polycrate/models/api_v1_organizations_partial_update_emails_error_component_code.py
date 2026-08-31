from typing import Literal

ApiV1OrganizationsPartialUpdateEmailsErrorComponentCode = Literal["invalid"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateEmailsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_organizations_partial_update_emails_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateEmailsErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
