from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_pricing_quote_workspaces_partial_update_archived_at_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
