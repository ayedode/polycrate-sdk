from typing import Literal

ApiV1ProviderAccountsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PROVIDER_ACCOUNTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_provider_accounts_create_kind_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateKindErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
