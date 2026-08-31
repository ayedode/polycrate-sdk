from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponentAttr = Literal["loadbalancer_count"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponentAttr
] = {
    "loadbalancer_count",
}


def check_api_v1_pricing_quote_workspaces_archive_create_loadbalancer_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
