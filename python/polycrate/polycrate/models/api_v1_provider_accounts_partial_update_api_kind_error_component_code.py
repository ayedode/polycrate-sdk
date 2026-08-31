from typing import Literal

ApiV1ProviderAccountsPartialUpdateApiKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_API_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateApiKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_provider_accounts_partial_update_api_kind_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateApiKindErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_API_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_API_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
