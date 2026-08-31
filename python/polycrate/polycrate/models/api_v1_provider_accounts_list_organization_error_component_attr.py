from typing import Literal

ApiV1ProviderAccountsListOrganizationErrorComponentAttr = Literal["organization"]

API_V1_PROVIDER_ACCOUNTS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_provider_accounts_list_organization_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListOrganizationErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
