from typing import Literal

ApiV1ProviderAccountsArchiveCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_provider_accounts_archive_create_metadata_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateMetadataErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
