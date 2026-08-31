from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_pricing_quote_workspaces_archive_create_loadbalancer_count_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
