from typing import Literal

ApiV1ProviderAccountsListApiKindErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_PROVIDER_ACCOUNTS_LIST_API_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsListApiKindErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_provider_accounts_list_api_kind_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsListApiKindErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_API_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_API_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
