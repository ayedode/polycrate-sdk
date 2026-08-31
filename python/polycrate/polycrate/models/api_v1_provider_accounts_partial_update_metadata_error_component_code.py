from typing import Literal

ApiV1ProviderAccountsPartialUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_partial_update_metadata_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateMetadataErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
