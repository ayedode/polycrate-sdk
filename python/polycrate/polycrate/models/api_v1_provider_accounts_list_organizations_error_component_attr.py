from typing import Literal

ApiV1ProviderAccountsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_PROVIDER_ACCOUNTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_provider_accounts_list_organizations_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListOrganizationsErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
