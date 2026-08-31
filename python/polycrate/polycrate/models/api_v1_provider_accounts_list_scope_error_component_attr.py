from typing import Literal

ApiV1ProviderAccountsListScopeErrorComponentAttr = Literal["scope"]

API_V1_PROVIDER_ACCOUNTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_provider_accounts_list_scope_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListScopeErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
