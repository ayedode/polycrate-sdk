from typing import Literal

ApiV1ProviderAccountsPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_provider_accounts_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateKindErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
