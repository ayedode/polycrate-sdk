from typing import Literal

ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponentAttr = Literal["hosts_count"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponentAttr
] = {
    "hosts_count",
}


def check_api_v1_pricing_quote_workspaces_create_hosts_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
