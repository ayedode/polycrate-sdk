from typing import Literal

ApiV1OrganizationsDiscoverCreateEmailsErrorComponentAttr = Literal["emails"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateEmailsErrorComponentAttr
] = {
    "emails",
}


def check_api_v1_organizations_discover_create_emails_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateEmailsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_EMAILS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
