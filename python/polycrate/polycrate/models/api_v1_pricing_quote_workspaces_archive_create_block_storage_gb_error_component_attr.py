from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponentAttr = Literal["block_storage_gb"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_BLOCK_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponentAttr
] = {
    "block_storage_gb",
}


def check_api_v1_pricing_quote_workspaces_archive_create_block_storage_gb_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_BLOCK_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_BLOCK_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
