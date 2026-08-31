from typing import Literal

ApiV1ProviderAccountsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_provider_accounts_update_provider_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateProviderErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
