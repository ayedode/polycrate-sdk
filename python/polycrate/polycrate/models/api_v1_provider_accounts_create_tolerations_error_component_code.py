from typing import Literal

ApiV1ProviderAccountsCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateTolerationsErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
