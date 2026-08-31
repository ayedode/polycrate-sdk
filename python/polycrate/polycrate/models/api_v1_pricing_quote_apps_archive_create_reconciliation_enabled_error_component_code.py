from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_apps_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
