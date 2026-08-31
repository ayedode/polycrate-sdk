from typing import Literal

ApiV1ProviderAccountsPartialUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_provider_accounts_partial_update_metadata_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateMetadataErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
