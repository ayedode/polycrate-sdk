from typing import Literal

ApiV1ProviderAccountsPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
