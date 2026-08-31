from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponentAttr = Literal["total_price"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponentAttr
] = {
    "total_price",
}


def check_api_v1_pricing_quote_workspaces_update_total_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
