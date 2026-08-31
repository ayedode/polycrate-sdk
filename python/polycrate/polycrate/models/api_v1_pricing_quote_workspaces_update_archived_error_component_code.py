from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_workspaces_update_archived_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
