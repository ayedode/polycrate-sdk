from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponentAttr = Literal["support_quoted_price"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_SUPPORT_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponentAttr
] = {
    "support_quoted_price",
}


def check_api_v1_pricing_quote_workspaces_update_support_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_SUPPORT_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_SUPPORT_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
