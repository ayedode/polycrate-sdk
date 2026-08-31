from typing import Literal

ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
