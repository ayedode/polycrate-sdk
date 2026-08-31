from typing import Literal

ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_apps_partial_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsPartialUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_PARTIAL_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
