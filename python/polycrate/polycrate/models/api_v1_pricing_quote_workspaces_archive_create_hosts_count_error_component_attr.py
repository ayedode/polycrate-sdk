from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponentAttr = Literal["hosts_count"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponentAttr
] = {
    "hosts_count",
}


def check_api_v1_pricing_quote_workspaces_archive_create_hosts_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_HOSTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
