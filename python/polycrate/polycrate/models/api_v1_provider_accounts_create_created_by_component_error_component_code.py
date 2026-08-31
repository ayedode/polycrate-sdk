from typing import Literal

ApiV1ProviderAccountsCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_PROVIDER_ACCOUNTS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_provider_accounts_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
