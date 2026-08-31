from typing import Literal

ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_provider_accounts_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
