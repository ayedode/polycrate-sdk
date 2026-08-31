from typing import Literal

ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_provider_accounts_partial_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
