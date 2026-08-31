from typing import Literal

ApiV1ProviderAccountsUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_update_metadata_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsUpdateMetadataErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
