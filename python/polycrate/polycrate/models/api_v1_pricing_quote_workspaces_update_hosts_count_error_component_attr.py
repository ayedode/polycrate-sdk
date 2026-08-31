from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponentAttr = Literal["hosts_count"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponentAttr
] = {
    "hosts_count",
}


def check_api_v1_pricing_quote_workspaces_update_hosts_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
