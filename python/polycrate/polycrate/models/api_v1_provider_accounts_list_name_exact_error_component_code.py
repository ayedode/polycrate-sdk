from typing import Literal

ApiV1ProviderAccountsListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_PROVIDER_ACCOUNTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_provider_accounts_list_name_exact_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsListNameExactErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
