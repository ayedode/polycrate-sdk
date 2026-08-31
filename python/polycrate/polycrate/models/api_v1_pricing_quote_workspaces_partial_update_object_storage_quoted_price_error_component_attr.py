from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponentAttr = Literal[
    "object_storage_quoted_price"
]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_OBJECT_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponentAttr
] = {
    "object_storage_quoted_price",
}


def check_api_v1_pricing_quote_workspaces_partial_update_object_storage_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_OBJECT_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_OBJECT_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
