from typing import Literal

ApiV1ProviderAccountsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_provider_accounts_update_kind_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateKindErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
