from typing import Literal

ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
