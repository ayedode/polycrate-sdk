from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponentAttr = Literal[
    "block_storage_quoted_price"
]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_BLOCK_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponentAttr
] = {
    "block_storage_quoted_price",
}


def check_api_v1_pricing_quote_workspaces_partial_update_block_storage_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_BLOCK_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_BLOCK_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
