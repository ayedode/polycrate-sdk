from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_quote_workspaces_update_criticality_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
