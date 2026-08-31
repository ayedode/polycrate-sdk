from typing import Literal

ApiV1CredentialsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_CREDENTIALS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_credentials_list_organizations_error_component_attr(
    value: str,
) -> ApiV1CredentialsListOrganizationsErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
