from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponentAttr = Literal["object_storage_quoted_price"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_OBJECT_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponentAttr
] = {
    "object_storage_quoted_price",
}


def check_api_v1_pricing_quote_workspaces_update_object_storage_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_OBJECT_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_OBJECT_STORAGE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
