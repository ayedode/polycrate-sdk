from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponentAttr = Literal["loadbalancer_quoted_price"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LOADBALANCER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponentAttr
] = {
    "loadbalancer_quoted_price",
}


def check_api_v1_pricing_quote_workspaces_update_loadbalancer_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LOADBALANCER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_LOADBALANCER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
