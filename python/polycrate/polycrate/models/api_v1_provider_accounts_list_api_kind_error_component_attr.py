from typing import Literal

ApiV1ProviderAccountsListApiKindErrorComponentAttr = Literal["api_kind"]

API_V1_PROVIDER_ACCOUNTS_LIST_API_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListApiKindErrorComponentAttr
] = {
    "api_kind",
}


def check_api_v1_provider_accounts_list_api_kind_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListApiKindErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_API_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_API_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
