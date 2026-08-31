from typing import Literal

ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponentAttr = Literal["total_price"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponentAttr
] = {
    "total_price",
}


def check_api_v1_pricing_quote_workspaces_create_total_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
