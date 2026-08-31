from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponentAttr = Literal["block_storage_gb"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_BLOCK_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponentAttr
] = {
    "block_storage_gb",
}


def check_api_v1_pricing_quote_workspaces_partial_update_block_storage_gb_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_BLOCK_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_BLOCK_STORAGE_GB_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
