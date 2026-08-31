from typing import Literal

ApiV1ProviderAccountsUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_update_tolerations_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsUpdateTolerationsErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
