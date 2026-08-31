from typing import Literal

ApiV1ProviderAccountsCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROVIDER_ACCOUNTS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_provider_accounts_create_kind_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateKindErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
