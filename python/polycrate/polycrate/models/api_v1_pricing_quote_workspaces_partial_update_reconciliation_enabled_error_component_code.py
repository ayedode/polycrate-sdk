from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_workspaces_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
