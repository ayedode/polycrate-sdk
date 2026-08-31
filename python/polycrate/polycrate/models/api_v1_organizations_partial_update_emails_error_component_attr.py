from typing import Literal

ApiV1OrganizationsPartialUpdateEmailsErrorComponentAttr = Literal["emails"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_organizations_partial_update_emails_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateEmailsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
