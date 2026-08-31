from typing import Literal

ApiV1ProviderAccountsPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_provider_accounts_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateProviderErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
