from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponentAttr = Literal["loadbalancer_count"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LOADBALANCER_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponentAttr
] = {
    "loadbalancer_count",
}


def check_api_v1_pricing_quote_workspaces_partial_update_loadbalancer_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LOADBALANCER_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_LOADBALANCER_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
