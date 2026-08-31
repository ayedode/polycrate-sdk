from typing import Literal

ApiV1ProviderAccountsListKindItem = Literal["generic"]

API_V1_PROVIDER_ACCOUNTS_LIST_KIND_ITEM_VALUES: set[ApiV1ProviderAccountsListKindItem] = {
    "generic",
}


def check_api_v1_provider_accounts_list_kind_item(value: str) -> ApiV1ProviderAccountsListKindItem:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_KIND_ITEM_VALUES!r}")
