from typing import Literal

ApiV1ProviderAccountsListScope = Literal["system", "user"]

API_V1_PROVIDER_ACCOUNTS_LIST_SCOPE_VALUES: set[ApiV1ProviderAccountsListScope] = {
    "system",
    "user",
}


def check_api_v1_provider_accounts_list_scope(value: str) -> ApiV1ProviderAccountsListScope:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_SCOPE_VALUES!r}")
