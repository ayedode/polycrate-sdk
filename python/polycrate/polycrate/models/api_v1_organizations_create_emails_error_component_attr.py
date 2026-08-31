from typing import Literal

ApiV1OrganizationsCreateEmailsErrorComponentAttr = Literal["emails"]

API_V1_ORGANIZATIONS_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_organizations_create_emails_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateEmailsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
