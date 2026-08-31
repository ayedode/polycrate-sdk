from typing import Literal

ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_PRICING_QUOTE_APPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_pricing_quote_apps_update_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
