from typing import Literal

ApiV1PricingProductsUpdateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_PRODUCTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingProductsUpdateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_products_update_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1PricingProductsUpdateReconciliationEnabledErrorComponentCode:
    if value in API_V1_PRICING_PRODUCTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_UPDATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
