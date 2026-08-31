from typing import Literal

ApiV1ProviderAccountsUpdateApiKindErrorComponentAttr = Literal["api_kind"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_API_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateApiKindErrorComponentAttr
] = {
    "api_kind",
}


def check_api_v1_provider_accounts_update_api_kind_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateApiKindErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_API_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_API_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
