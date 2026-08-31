from typing import Literal

ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_provider_accounts_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
