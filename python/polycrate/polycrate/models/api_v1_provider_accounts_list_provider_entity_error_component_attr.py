from typing import Literal

ApiV1ProviderAccountsListProviderEntityErrorComponentAttr = Literal["provider_entity"]

API_V1_PROVIDER_ACCOUNTS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListProviderEntityErrorComponentAttr
] = {
    "provider_entity",
}


def check_api_v1_provider_accounts_list_provider_entity_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListProviderEntityErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
