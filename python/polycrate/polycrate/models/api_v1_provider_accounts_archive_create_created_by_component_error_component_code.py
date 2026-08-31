from typing import Literal

ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_provider_accounts_archive_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
