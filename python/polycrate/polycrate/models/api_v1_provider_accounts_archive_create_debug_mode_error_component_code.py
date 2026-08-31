from typing import Literal

ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_archive_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateDebugModeErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
