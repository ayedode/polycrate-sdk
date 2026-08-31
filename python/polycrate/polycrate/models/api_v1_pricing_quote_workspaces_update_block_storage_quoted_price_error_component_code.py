from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_BLOCK_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pricing_quote_workspaces_update_block_storage_quoted_price_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_BLOCK_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_BLOCK_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
