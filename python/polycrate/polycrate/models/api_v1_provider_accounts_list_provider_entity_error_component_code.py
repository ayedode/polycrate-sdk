from typing import Literal

ApiV1ProviderAccountsListProviderEntityErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_PROVIDER_ACCOUNTS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsListProviderEntityErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_provider_accounts_list_provider_entity_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsListProviderEntityErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
