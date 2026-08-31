from typing import Literal

ApiV1ProviderAccountsUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_provider_accounts_update_metadata_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsUpdateMetadataErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
