from typing import Literal

ApiV1ProviderAccountsCreateArchivedByErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateArchivedByErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_provider_accounts_create_archived_by_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateArchivedByErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
