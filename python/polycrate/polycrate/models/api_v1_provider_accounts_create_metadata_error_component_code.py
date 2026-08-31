from typing import Literal

ApiV1ProviderAccountsCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDER_ACCOUNTS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_provider_accounts_create_metadata_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateMetadataErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
